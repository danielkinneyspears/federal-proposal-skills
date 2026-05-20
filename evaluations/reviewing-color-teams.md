# Evaluations: reviewing-color-teams

## Eval 1 — Red Team scores against Section M

**Scenario:** A user asks for a Red Team review of a near-final technical volume.

**Inputs:** `12-sections/`, `10-compliance-matrix.md`, Section L and M.

**Expected behavior:**
- Confirms the review type as Red Team given the ~90% maturity.
- Rates each Section M factor with an adjectival rating, documenting the strengths, weaknesses, significant weaknesses, and deficiencies behind it.
- Records every finding with a location, a severity, and a specific recommended fix.
- Gives an integrated verdict on whether the proposal would win.
- Writes `20-color-review-red.md`.

**Anti-behavior:**
- Does not score against reviewer taste instead of Section M.
- Does not produce vague findings with no location or fix.

## Eval 2 — A deficiency is called a deficiency

**Scenario:** The proposal entirely fails to address a mandatory PWS requirement.

**Inputs:** A draft with a missing mandatory requirement.

**Expected behavior:**
- Identifies the omission as a deficiency, not a weakness.
- States that a deficiency makes the proposal unawardable as written and ranks it the top recovery priority.

**Anti-behavior:**
- Does not soften a deficiency into a minor finding.

## Eval 3 — Reviews, does not rewrite

**Scenario:** A user asks the skill to Red Team a section and "fix it while you're at it."

**Inputs:** A drafted section.

**Expected behavior:**
- Produces the review with findings and recommended fixes.
- Explains that the fixes are recovery work for the drafting skill and does not rewrite the section itself.

**Anti-behavior:**
- Does not silently rewrite the proposal in place of reviewing it.

## Eval 4 — Green Team on the cost volume

**Scenario:** A user asks for a Green Team review of the cost volume. A cost narrative and the technical and management volumes exist.

**Inputs:** `16-cost-narrative.md`, `12-sections/`, Section L cost instructions.

**Expected behavior:**
- Identifies the review type as Green Team and applies the cost/price lens.
- Checks pricing strategy, basis-of-estimate sufficiency, cost realism, and cost-technical consistency against the technical and management volumes.
- Records findings with location, severity, and recommended fix; gives a readiness assessment rather than a Section M adjectival score.

**Anti-behavior:**
- Does not treat a Green Team like a Red Team and assign Section M factor ratings to the cost volume.
- Does not skip the cost-technical consistency check.
