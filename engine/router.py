"""Route a described problem to an analysis method, not to a final choice.

Pure Python stdlib, deterministic outputs, no network access, no LLM inference.
This is an explicit hypothesis-driven router; the user supplies evidence flags.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
KINDS = {"one_shot", "research", "sequential", "strategic", "system", "behavior", "learning", "focus", "search"}
STAKES = {"low", "medium", "high", "critical"}
REVERSIBILITY = {"reversible", "partial", "irreversible"}
UNCERTAINTY = {"known", "estimable", "ambiguous"}
SIGNALS = {
    "probabilities_defensible", "information_can_change_action", "information_obtainable",
    "opponent_adaptive", "perception_mismatch_evidence", "feedback_loop_evidence",
    "behavior_cue_observed", "skill_gap_measured", "attention_switch_cost_observed",
    "search_random_order", "search_no_recall", "search_fixed_horizon",
    "search_best_only_objective", "risk_of_ruin", "evidence_independent",
    "emotionally_activated", "irreversible_externalities"
}


def registry() -> dict:
    with (ROOT / "data" / "model_registry.json").open(encoding="utf-8") as fp:
        document = json.load(fp)
    models = document["models"]
    ids = [item["id"] for item in models]
    if len(ids) != len(set(ids)):
        raise ValueError("Duplicate model IDs in registry")
    return {item["id"]: item for item in models}


def validate(problem: dict) -> dict:
    if not isinstance(problem, dict):
        raise ValueError("Problem must be a JSON object")
    required = {"schema_version", "id", "objective", "decision"}
    if missing := required - problem.keys():
        raise ValueError(f"Missing fields: {sorted(missing)}")
    if problem["schema_version"] != "1.0":
        raise ValueError("Unsupported problem schema version")
    if not isinstance(problem["id"], str) or not problem["id"].strip():
        raise ValueError("id must be nonempty text")
    if not isinstance(problem["objective"], str) or not problem["objective"].strip():
        raise ValueError("objective must be nonempty text")
    allowed_top = required | {"signals", "constraints", "evidence_refs"}
    if extra := problem.keys() - allowed_top:
        raise ValueError(f"Unknown top-level fields: {sorted(extra)}")
    d = problem["decision"]
    if not isinstance(d, dict):
        raise ValueError("decision must be an object")
    allowed_decision = {"kind", "stakes", "reversibility", "uncertainty", "alternatives"}
    if extra := d.keys() - allowed_decision:
        raise ValueError(f"Unknown decision fields: {sorted(extra)}")
    for field, accepted in [("kind", KINDS), ("stakes", STAKES), ("reversibility", REVERSIBILITY), ("uncertainty", UNCERTAINTY)]:
        if d.get(field) not in accepted:
            raise ValueError(f"decision.{field} must be one of {sorted(accepted)}")
    opts = d.get("alternatives")
    if not isinstance(opts, list) or len(opts) < 2 or any(not isinstance(a, str) or not a.strip() for a in opts):
        raise ValueError("decision.alternatives must contain at least two named alternatives")
    flags = problem.get("signals", {})
    if not isinstance(flags, dict):
        raise ValueError("signals must be an object")
    if unknown := flags.keys() - SIGNALS:
        raise ValueError(f"Unknown signals: {sorted(unknown)}; update the schema first")
    if any(type(value) is not bool for value in flags.values()):
        raise ValueError("Every signal must be boolean; uncertainty is not a boolean signal")
    if "constraints" in problem and (not isinstance(problem["constraints"], list) or any(not isinstance(c, str) for c in problem["constraints"])):
        raise ValueError("constraints must be an array of strings")
    if "evidence_refs" in problem and (not isinstance(problem["evidence_refs"], list) or any(not isinstance(r, str) for r in problem["evidence_refs"])):
        raise ValueError("evidence_refs must be an array of strings")
    return problem


def _depth(decision: dict, flags: dict) -> str:
    if (decision["stakes"] == "critical" or flags.get("risk_of_ruin") or
        (decision["stakes"] == "high" and decision["reversibility"] == "irreversible")):
        return "R"
    if (decision["stakes"] == "high" or decision["uncertainty"] == "ambiguous" or
        decision["reversibility"] != "reversible" or flags.get("irreversible_externalities") or
        decision["kind"] in {"sequential", "strategic", "system"}):
        return "M"
    return "F"


def route(problem: dict) -> dict:
    """Use explicit structural features. No named people, inference of motives, or fabricated probabilities."""
    validate(problem)
    models = registry()
    d, f = problem["decision"], problem.get("signals", {})
    kind = d["kind"]
    yes = lambda key: f.get(key, False)
    blocked = []
    auxiliaries = []
    guardrails = []
    gaps = []

    # Layer 0: irreversible downside constraints always precede optimization.
    if yes("risk_of_ruin"):
        guardrails.append("RUIN_VETO: reject options with intolerable permanent losses before maximizing averages")
    if d["reversibility"] == "irreversible" or yes("irreversible_externalities"):
        guardrails.append("COMMITMENT_GATE: investigate staging, exit rights, and consequences before committing")
    if yes("emotionally_activated") and d["reversibility"] != "reversible":
        guardrails.append("HOT_STATE_REVIEW: defer irreversible action where possible, or obtain independent review")

    # Layer 1-3: select a primary method from problem topology, not keyword associations.
    if kind == "one_shot":
        if yes("risk_of_ruin") or d["uncertainty"] == "ambiguous":
            primary = "ROBUST_CHOICE"
        elif d["stakes"] == "low" and d["reversibility"] == "reversible":
            primary = "SATISFICING"
        elif yes("probabilities_defensible"):
            primary = "EXPECTED_UTILITY"
        else:
            primary = "ROBUST_CHOICE"
            gaps.append("Elicit probabilities or scenarios before assigning expected values")
        if primary != "EXPECTED_UTILITY" and not yes("probabilities_defensible"):
            blocked.append({"model": "EXPECTED_UTILITY", "reason": "Probabilities are not sufficiently defensible"})
    elif kind == "research":
        if yes("information_can_change_action") and yes("information_obtainable"):
            primary = "VALUE_OF_INFORMATION"
            if not yes("probabilities_defensible"):
                gaps.append("Use qualitative decision reversal thresholds; do not invent numerical EVSI")
        else:
            primary = "SATISFICING"
            blocked.append({"model": "VALUE_OF_INFORMATION", "reason": "No obtainable information shown likely to alter the action"})
    elif kind == "sequential":
        primary = "SEQUENTIAL_PLANNING"
        if d["uncertainty"] == "ambiguous":
            gaps.append("Specify state transitions and plausible transition scenarios; Bellman outputs are not identified yet")
    elif kind == "strategic":
        if not yes("opponent_adaptive"):
            primary = "STAKEHOLDER_DIAGNOSIS"
            blocked.append({"model": "GAME_THEORY", "reason": "Strategic response is not established"})
            blocked.append({"model": "HYPERGAME", "reason": "Strategic response is not established"})
        elif yes("perception_mismatch_evidence"):
            primary = "HYPERGAME"
            auxiliaries.append("GAME_THEORY")
        else:
            primary = "GAME_THEORY"
            blocked.append({"model": "HYPERGAME", "reason": "No evidence for materially different perceived games"})
    elif kind == "system":
        if yes("feedback_loop_evidence"):
            primary = "SYSTEM_DYNAMICS"
        else:
            primary = "CAUSAL_DIAGNOSIS"
            blocked.append({"model": "SYSTEM_DYNAMICS", "reason": "Feedback loop is hypothetical, not observed"})
    elif kind == "behavior":
        if yes("behavior_cue_observed"):
            primary = "HABIT_INTERVENTION"
        else:
            primary = "BEHAVIOR_DIAGNOSIS"
            blocked.append({"model": "HABIT_INTERVENTION", "reason": "Do not assume a cue-routine-reward mechanism"})
    elif kind == "learning":
        if yes("skill_gap_measured"):
            primary = "DELIBERATE_PRACTICE"
        else:
            primary = "SKILL_DIAGNOSIS"
            blocked.append({"model": "DELIBERATE_PRACTICE", "reason": "Target skill deficit has not been measured"})
    elif kind == "focus":
        primary = "ATTENTION_DESIGN" if yes("attention_switch_cost_observed") else "ATTENTION_AUDIT"
    else:  # search
        strict = ["search_random_order", "search_no_recall", "search_fixed_horizon", "search_best_only_objective"]
        if all(yes(flag) for flag in strict):
            primary = "SECRETARY_STOPPING"
        else:
            primary = "GENERAL_STOPPING"
            blocked.append({"model": "SECRETARY_STOPPING", "reason": "37% rule requires random order, no recall, known horizon and selecting the absolute best"})

    # Layer 2: evidence quality only motivates verification; not automatic Bayesian arithmetic.
    if f.get("evidence_independent") is False and problem.get("evidence_refs"):
        gaps.append("Confirm source independence; repeated reports are not independent evidence")
    if yes("risk_of_ruin") and primary != "ROBUST_CHOICE":
        auxiliaries.append("ROBUST_CHOICE")
    if primary not in models:
        raise ValueError(f"Registry missing model {primary}")
    for name in auxiliaries:
        if name not in models:
            raise ValueError(f"Registry missing auxiliary model {name}")

    return {
        "schema_version": "1.0",
        "case_id": problem["id"],
        "depth": _depth(d, f),
        "primary_model": primary,
        "supporting_models": auxiliaries,
        "rejected_models": blocked,
        "guardrails": guardrails,
        "information_gaps": gaps,
        "method": models[primary]["method"],
        "stop_condition": models[primary]["stop_when"],
        "model_limit": models[primary]["failure_mode"],
        "decision_made": False,
        "epistemic_status": "RULE_BASED_ROUTING_HYPOTHESIS",
    }


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python -m engine.router examples/sample_case.json")
    with open(sys.argv[1], encoding="utf-8") as fp:
        problem = json.load(fp)
    print(json.dumps(route(problem), indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
