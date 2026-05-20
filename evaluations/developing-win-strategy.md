# Evaluations: developing-win-strategy

## Eval 1 — Table stakes are not discriminators

**Scenario:** A user lists their strengths and calls them all discriminators, including "we have a mature PMO" and "our staff are cleared" — strengths every competitor in the field also has.

**Inputs:** `03-competitive-assessment.md` exists with the competitive field.

**Expected behavior:**
- Runs every candidate strength through the four-part discriminator test (valuable, true, provable, rare).
- Classifies the strengths every competitor shares as table stakes, not discriminators.
- Builds win themes only on validated discriminators.
- Writes `05-win-strategy.md`.

**Anti-behavior:**
- Does not accept table stakes as win themes because the user labeled them discriminators.

## Eval 2 — Themes carry benefit and proof

**Scenario:** A user asks for win themes and provides strengths but little supporting evidence.

**Inputs:** Customer hot buttons and candidate strengths supplied.

**Expected behavior:**
- Builds each theme as hot button → discriminator → customer benefit → proof → Section M factor.
- Flags themes that lack proof and asks for substantiation or downgrades them.
- Maps each theme to a Section M factor and flags factors with thin coverage.

**Anti-behavior:**
- Does not produce feature-only themes that stop at "we have X".
- Does not fabricate proof points.

## Eval 3 — Exposures get responses

**Scenario:** The competitive assessment lists two exposures the team will be ghosted on. The user asks for the win strategy.

**Inputs:** `03-competitive-assessment.md` with named exposures.

**Expected behavior:**
- Carries every exposure into the win strategy with a concrete response (fix, pre-empt, or reframe).
- Does not leave an exposure unaddressed.

**Anti-behavior:**
- Does not ignore exposures or assume the evaluator will overlook them.
