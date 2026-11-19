# Autonomous repository maintenance policy

Effective 2026-11-18. Applies to **Ganesh96/brain-of-shuchii**.

## Delegated authority

The repository owner authorizes the connected assistant, during active conversations and authorized tool sessions, to develop, maintain, test, document and integrate routine repository changes without asking for separate approval for each pull request. Scope includes the reasoning kernel, knowledge architecture, research notes, discourse syntheses, theory records, schema improvements, tests and provenance corrections.

This is an authorization to perform work **when invoked**, not a promise of continuous autonomous monitoring, future work while the conversation is inactive, or bypassing GitHub permissions.

## Change workflow

1. Read the latest default branch, existing issue/PR state, relevant files and stated objective.
2. Create a descriptive feature branch. Avoid direct edits to `main`, force pushes and unrelated refactors.
3. Implement a bounded change. Update relevant tests, schema checks, source references and changelog/records.
4. Run available local validation and review the resulting diff. Include negative cases for reasoning-model changes; check privacy, safety, source attribution and backwards compatibility.
5. Open a pull request explaining purpose, significant assumptions, test evidence, risk, and how to revert.
6. Inspect actual GitHub CI results, branch protections, and required independent reviews; do not assume a passing status from the existence of a workflow file.
7. If the PR is eligible, the assistant **may merge its own PR** using a head-SHA guard and a reversible merge strategy (usually squash). Verify merge status and inspect the result.
8. If blocked, leave the PR open, explain the exact blocker and correct it if authorized. Never weaken checks simply to merge.

## Approval distinction

**GitHub does not permit an author to approve their own PR as an independent review.** The assistant can perform self-review and leave comments, but must not claim a GitHub approval that was not granted. It can merge an eligible self-authored PR only when GitHub permits the merge without an independent approval. All repository rules take precedence.

## Changes allowed without another approval

- New or corrected theoretical concepts, models, examples, original discourse syntheses and citations that respect evidence/provenance rules.
- Incremental router, evaluation, schema, documentation and testing improvements.
- Narrow bug fixes and compatible refactors with demonstrably passing checks.
- Additions and corrections to the knowledge index or versioned rule lifecycle.

## Changes requiring a new explicit user decision

- Publishing private, identifying, sensitive or confidential content to this **public** repository.
- Changing repository visibility, collaborators, access policies, credentials, secrets or organization settings.
- Weakening security measures, required tests or independent-review protections.
- Force-updating branches, destroying history, deleting substantial knowledge, changing the license or making irreversible architectural migrations.
- Deploying externally, enabling paid services, connecting new data sources, or operating on systems beyond this repository.

## Reasoning-quality gates

An update is not accepted solely because it sounds insightful. Substantive model changes must record:
- the trigger conditions and assumptions;
- a counterexample or known failure mode;
- whether the material is theorem, primary-source claim, observed finding, inference or speculative hypothesis;
- at least one test that would detect an incorrect application;
- how a future reviewer could correct or retire it.

Do not hide contradictory evidence, overwrite original forecasts after outcomes, or manufacture bibliographic certainty.

## Operational reporting

For every completed work session, report PR/commit links, what changed, checks actually observed, whether the PR merged, and unresolved limitations. Silence or a tool attempt does not constitute a successful update.
