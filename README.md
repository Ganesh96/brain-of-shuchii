# brain-of-shuchii — Evolving knowledge and decision architecture

**Canonical GitHub memory for theory, research, discourse, lateral thinking, models, decisions and evidence-based self-correction.** The active conversation is the thinking surface; this repository is the durable, inspectable reference. The Python reasoning kernel is the first implementation component, not the full purpose of this project.

- [Knowledge and reasoning charter](docs/KNOWLEDGE_CHARTER.md) — research domains, evidence, dispute preservation and knowledge evolution.
- [Autonomous maintainer policy](docs/MAINTAINER_POLICY.md) — permitted repository maintenance, self-review versus approval, CI and merge gates.
- [Stage I technical architecture](docs/ARCHITECTURE.md) — runnable decision-method router and evaluation contracts.

**Current development:** Stage I is implemented. Importing and reconciling B1–B5 and the master concept atlas is a later stage, not yet completed. GitHub updates occur only when authorized tools are actively invoked; this project does not imply background or continuous memory access.

## Stage I: Decision Reasoning Kernel

An inspectable, evolving **decision-method router**. Its purpose is to select *how to analyze a problem*, not to impersonate a mind, automatically select a life decision, or warehouse unrestricted chat transcripts.

## What Stage I delivers

- Hierarchical L0–L6 reasoning contract with governance before optimization.
- Deterministic Python 3.11+ router based on explicit decision structure and evidence signals.
- Standard JSON schema definitions for problem, model, rule and evaluation artifacts.
- Versioned operator registry (18 methods) and three candidate decision rules, with limitations and stable master-knowledge `C####` references.
- 24 synthetic adversarial cases that test false-positive routing, hard downside constraints, and decision-relevant information.
- GitHub Actions CI for Python 3.11/3.12 and no third-party runtime dependencies.

## Run locally

```sh
python -m unittest discover -s tests -v
python -m engine.router examples/sample_case.json
```

The JSON output contains `primary_model`, `supporting_models`, `rejected_models`, `guardrails`, `information_gaps`, `stop_condition`, and `decision_made: false`.

## Files

- `engine/router.py` — deterministic hierarchical method selection and input validation.
- `data/model_registry.json` — conceptual model operators, stop conditions and failure modes.
- `data/rules.json` — candidate rules and lifecycle fields.
- `schemas/stage1.schema.json` — JSON Schema Draft 2020-12 for all Stage I record types.
- `evaluations/adversarial_cases.json` — synthetic review fixtures.
- `tests/test_router.py` — structural tests and safeguards.
- `docs/ARCHITECTURE.md` — theory selection, epistemic limits, privacy and evolution protocol.

## What Stage I does not claim

Passing a model-route test does not prove a recommendation improves real-world choices. Probabilities and opponent beliefs are not inferred from narrative text. Sources are not automatically validated or integrated. The B1–B5 packets and 243-concept master corpus have **not** been imported; that is a separate Stage II process requiring deduplication and provenance checks.

## Privacy

**This repository is public.** Only generic material and synthetic evaluation cases should be committed. Keep personal decision records, sensitive source material, and proprietary PDFs outside this repository.

## Evolution

`candidate -> tested -> operational -> revised/retired`. New operators require explicit eligibility and exclusion conditions, a traceable source, and tests demonstrating when the operator must *not* be selected. Prefer correcting the smallest useful rule over expanding the framework.
