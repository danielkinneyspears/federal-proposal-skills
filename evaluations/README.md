# Evaluations

Evaluations are the source of truth for whether a skill works and whether a
change to it helps or hurts. Each skill should ship with at least three.

## Structure

One file per skill, `evaluations/<skill-name>.md`, containing at least three
evaluation scenarios. Synthetic fixture files, if any, go in
`evaluations/fixtures/`.

## Evaluation format

Each evaluation file holds three or more scenarios in this structure:

```markdown
# Evaluations: <skill-name>

## Eval 1 — <short name>

**Scenario:** <One paragraph describing a representative task, as a user request.>

**Inputs:** <files or context the skill is given>

**Expected behavior:**
- <Observable, verifiable thing the skill should do — one bullet per check.>

**Anti-behavior:**
- <Things the skill must NOT do.>
```

Be specific and verifiable in the expected/anti-behavior bullets: "asks intake
questions before drafting", "writes 10-compliance-matrix.md", "flags the missing
page limit", "does not invent a competitor name".

## Rules for fixtures

All fixtures are **synthetic**. Never use real solicitation text, real
competitor data, or real proprietary information as a fixture. Synthetic
fixtures should be realistic in structure (a fake RFP with real-looking Section
L and M) but fictional in content.

## Running evaluations

There is no automated runner — checking a skill's behavior requires judgment.
Use the harness in [`run-evals.md`](run-evals.md): it explains the run process,
maps evaluations to the synthetic fixtures in [`fixtures/`](fixtures/), and
gives a result-record template so pass/fail outcomes are captured and
comparable across skill revisions. Result records are written to
`evaluations/results/` (git-ignored).
