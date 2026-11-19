# Knowledge and reasoning charter

## Identity

**brain-of-shuchii is the canonical external knowledge and reasoning repository** for an ongoing human–AI intellectual collaboration. It stores the durable results of research, philosophical discourse, theoretical analysis, lateral thinking, competing mental models, decisions, failed hypotheses, and lessons from outcomes.

It is **not merely a software project or a prompt archive**. The Stage I Python router is one instrument in this larger knowledge system. The chat is the active forum for inquiry; this GitHub repository is the durable, version-controlled reference. The assistant does not possess independent continuous access or a persistent background process: retrieval and updates happen through authorized connected tools during active work.

## Intended content

- **Epistemology and evidence:** claims, hypotheses, citations, counterevidence, uncertainty, calibration and revisions.
- **Formal theories:** decision theory, probability, causal inference, information theory, algorithms, game theory, hypergames, systems and control.
- **Cognitive mechanisms:** attention, memory, learning, behavioral distortions, habits and metacognition.
- **Strategic reasoning:** incentives, perception mismatch, bargaining, commitment, signaling, positioning and second-order effects.
- **Exploration:** original analogies, lateral hypotheses, conceptual inventions, theory combinations and unresolved contradictions.
- **Discourse:** the strongest arguments on competing sides, cruxes, objections, predictions and what evidence could settle disagreement.
- **Practical reasoning:** bounded decision procedures, applicability tests, failure modes, case analyses and action policies.
- **Evolution:** predictions, evaluations, empirical outcomes, model corrections, version history and retired rules.

The aim is better **problem representation, model selection, inference, action, and self-correction**, not maximal graph density or indiscriminate note capture.

## Conceptual hierarchy

1. **Purpose and boundaries** — values, objectives, permissible actions, irreversible loss and affected parties.
2. **Representation** — problem type, state, actors, incentives, options, time horizon, uncertainty and constraints.
3. **Epistemic layer** — evidence, provenance, hypotheses, disagreement, causal validity and unknowns.
4. **Model selection** — minimal sufficient formal or qualitative tool, plus scope tests and rejected alternatives.
5. **Reasoning and discourse** — derivations, adversarial hypotheses, lateral alternatives and sensitivity.
6. **Decision and action** — options, thresholds, stop condition, execution and reversible experiments.
7. **Learning and revision** — calibrated predictions, outcome reviews, corrections and candidate-rule promotion.

This is an authority hierarchy, **not** a requirement to execute all seven layers for every question.

## Storage contracts

Every reusable entry should answer some subset of: **What does it assert? Under what conditions? Why believe it? How could it fail? What changes when it is used?**

- Give stable IDs to concepts, models, rules, claims and cases. Preserve imported B1–B5 IDs as aliases until reconciled.
- Distinguish **definition**, **author claim**, **empirically verified claim**, **formal theorem**, **original inference**, **analogy**, **counterexample**, and **open question**.
- Store provenance at claim level where material: book, edition, physical PDF page or primary research locator, quote-length-limited paraphrase, verification status, date.
- A text occurrence is not evidence that the passage supports a claim. Multiple summaries of one source are not independent evidence.
- Link nodes with precise relations (e.g. prerequisite, operationalizes, qualifies, contradicts, source_for, applies_when, fails_when). Never inflate link counts for their own sake.
- Store disagreements faithfully, especially different definitions, incompatible assumptions and unresolved values.
- Prefer concise derived discourse records (question, candidate positions, evidence, decisive crux, current conclusion, unresolved issues), not indiscriminate full-chat copies.
- A practical rule must include preconditions, exclusions, observable success criteria and a reversal/retirement condition.

## Epistemic lifecycle

`candidate -> investigated -> supported/contested -> operational (when tested) -> revised/superseded/retired`

A formal mathematical result may be accepted under proved assumptions without experiential testing; a practical intervention needs appropriate evidence of effectiveness. Do not conflate logical coherence, empirical accuracy or ethical desirability.

When new evidence arrives: retain the previous record, identify its decisive assumption, record the update and propagate consequences to dependent rules and indices. Never rewrite the old forecast after observing the outcome.

## Working protocol

1. Start with the user's question, not with a random tour of the repository.
2. Retrieve just the relevant concepts, evidence, models, past cases and unresolved contradictions.
3. Build competing interpretations, identify what would change the answer, and apply the smallest sufficient method.
4. Give the answer or deliberate with the user. Only then promote reusable discoveries through a reviewed repository update.
5. Favor corrections, cross-domain tests and evidence over more taxonomy.

## Public-repository safety

This repository is presently **public**. Keep sensitive or identifying personal decision histories, private correspondence, credentials, nonpublic employer material and copyrighted source-book PDFs out of it. Use generic or synthetic examples and original short paraphrases with citations. If personal records are desired, decide on appropriate repository access controls before publishing them.

## Evolution roadmap

- **Stage I:** tested reasoning router, schemas and adversarial cases (implemented).
- **Stage II:** reconcile master knowledge and B1–B5 concepts with provenance and stable IDs.
- **Stage III:** decision cases, claim verification, calibration and feedback-driven rule refinement.
- **Stage IV:** retrieval improvements, richer lateral synthesis and evaluation against difficult out-of-domain cases.

These are priorities, not permission for unsupervised background execution.
