# Stage I architecture and epistemic contract

The system is **a method selector, not an autonomous decision-maker or a simulated mind**. It never selects the real-world action and never contacts external parties. This distinction protects human authority and makes tests falsifiable.

## Hierarchy

- **L0 Governance:** value priorities, hard constraints, unacceptable/irreversible harm and authority. In code, ruin, commitment and hot-state review gates operate before model selection.
- **L1 Problem representation:** objective, alternatives, stakes, reversibility, uncertainty and structural kind. Unknown classifications require explicit clarification rather than invented labels.
- **L2 Epistemic:** source independence, probability defensibility and information gaps. Report unverified assumptions; no inferred probabilities.
- **L3 Model routing:** problem topology chooses one primary method; auxiliary models only close specific gaps. Never equate graph proximity with applicability.
- **L4 Countercheck:** model exclusions, scenario sensitivity, stopping condition and evidence that would reverse selection.
- **L5 Action:** user/agent applies the chosen method, keeps human decision authority and logs forecasts where appropriate; this module performs no external action.
- **L6 Evolution:** adversarial fixtures, source validation, calibrated feedback and versioned rule promotion. All models/rules currently have status `candidate`.

## Routing invariants

1. **Risk-of-ruin gate precedes optimization.** Risk is not traded against attractive averages without permission/constraints.
2. **The 37% stopping rule is a special case, never a universal search rule.** Requires random order, no recall, fixed horizon and top-one objective.
3. **Hypergame analysis requires evidence of perception mismatch plus adaptive actors.** Unknown motives alone do not suffice.
4. **Feedback loops require evidence; diagrams alone are hypotheses.**
5. **Habit intervention requires observed cue evidence; effort-only advice requires a measured skill gap.**
6. **Information value differs from entropy reduction.** Additional research must have a plausible action-changing result.
7. **Unjustified probabilities are not supplied by the router.** `EXPECTED_UTILITY` is blocked under insufficient probability evidence.
8. **No hindsight substitution.** When adding prediction/evaluation logs, preserve original pre-outcome forecasts.

## Model selection is not calculation

For an eligible one-shot decision, a practitioner may use `max_a E[U(a, theta) | evidence]` subject to constraints. For a sequential decision, a sufficiently specified Markov model can use a Bellman recurrence. Neither formula can be evaluated from a problem label alone.

The return value is a transparent recommendation for **analysis method** with exclusions, risk checks, information gaps and stop conditions. Its `decision_made` remains `false`.

## Evidence taxonomy

- `DIRECT_VERIFIED`: primary source passage actually inspected; requires stable locator and claim-level annotation.
- `TEXT_OCCURRENCE`: keyword located in a source; does **not** establish an interpretation.
- `GENERAL_THEORY`: standard formal notion independent of a particular book.
- `CROSS_BOOK_INFERENCE`: an inferred synthesis or application, not attributed to a book.
- `OPEN_QUESTION`: unsettled or speculative claim.

The seed model registry uses `GENERAL_THEORY` and stable `C####` references to the previously supplied master-knowledge snapshot; **these are reference IDs, not fully migrated evidence records**. `HYPERGAME` is exploratory and must not be mistaken for established observation.

## Public-repository boundary

Store only generic theories, schemas, synthetic example cases and tests. Do not commit personal decision journals, resumes, contact information, credentials, private conversations, immigration documents or copyrighted book PDFs here. Personal working material belongs in a separate controlled private store if ever needed.

## Evaluation and evolution

- Current tests are **structural invariants**: a human-authored set of adversarial inputs with predeclared expected model routes. Passing them demonstrates conformity to the explicit routing spec, **not improved human decision outcomes**.
- Later evaluation should use blinded held-out scenarios, human review, calibration, retrieval-provenance audits, and falsifiable counterexamples before changing rule status from `candidate` to `tested` or `operational`.
- For each revision, record why the change happened, impacted cases, regression tests, and any source correction. Never silently overwrite an established claim.
- Preserve the smallest sufficient model. If the incremental cost of analysis exceeds plausible decision benefit, stop.
