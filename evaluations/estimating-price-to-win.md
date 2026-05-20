# Evaluations: estimating-price-to-win

## Eval 1 — PTW is not the cost estimate

**Scenario:** A user gives their bottom-up cost estimate and asks "so what should we bid?"

**Inputs:** `03-competitive-assessment.md` exists; the user provides a cost estimate and budget signals.

**Expected behavior:**
- Estimates the customer budget and competitor prices as ranges with a stated basis.
- Sets a price-to-win target derived from budget and competition, not from the team's own cost.
- Reconciles the cost estimate against the target and reports the gap.
- Writes `04-price-to-win.md`.

**Anti-behavior:**
- Does not simply return the user's bottom-up cost as the recommended bid price.
- Does not present budget or competitor prices as single confident numbers.

## Eval 2 — Posture follows the evaluation type

**Scenario:** A user asks for price-to-win on an LPTA task order.

**Inputs:** Section M indicating LPTA; competitor information.

**Expected behavior:**
- Identifies the evaluation as LPTA and sets the posture accordingly.
- Targets at or just below the lowest credible competitor price, with a realism floor.
- Notes that exceeding requirements earns nothing and warns against gold-plating.

**Anti-behavior:**
- Does not recommend a value-premium price posture appropriate to best-value tradeoff.

## Eval 3 — Unbridgeable gap is reported

**Scenario:** The team's realistic cost is well above the customer's likely budget and every competitor's likely price, and no combination of levers closes the gap without making the bid unrealistic.

**Inputs:** Cost estimate, budget, and competitor prices supplied.

**Expected behavior:**
- Identifies and quantifies the pricing levers.
- Concludes plainly that the gap cannot be closed profitably and realistically.
- States that this finding belongs back in the bid/no-bid decision.

**Anti-behavior:**
- Does not bury the unbridgeable gap or recommend an unrealistically low price to force a fit.
