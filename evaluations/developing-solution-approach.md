# Evaluations: developing-solution-approach

## Eval 1 — Designs against requirements, themes, and cost together

**Scenario:** A user asks for a solution design. The compliance matrix, win strategy, and price-to-win artifacts all exist.

**Inputs:** `10-compliance-matrix.md`, `05-win-strategy.md`, `04-price-to-win.md`.

**Expected behavior:**
- Designs each solution element (technical, staffing, management, transition, risk, quality) concretely.
- Checks the design against all three standards: requirements coverage, win-theme delivery, and cost fit.
- Writes `08-solution-design.md`.

**Anti-behavior:**
- Does not design against requirements only and ignore themes or cost.
- Does not produce slogan-level elements with no concrete decisions.

## Eval 2 — A discriminator the design does not deliver

**Scenario:** The win strategy claims a discriminator (a proven zero-downtime transition method), but the candidate solution's transition approach does not actually use it.

**Inputs:** `05-win-strategy.md` with the discriminator; the in-progress design.

**Expected behavior:**
- Detects that the design does not deliver the claimed discriminator.
- Flags it and either redesigns the transition approach to deliver it or surfaces that the win strategy is wrong.

**Anti-behavior:**
- Does not leave the win theme standing while the design fails to support it.

## Eval 3 — Design-to-cost

**Scenario:** The first-pass solution design is richer than the price-to-win target can fund.

**Inputs:** `04-price-to-win.md` with the target; a design that exceeds it.

**Expected behavior:**
- Identifies that the design exceeds the price-to-win target.
- Redesigns toward the target (leaner labor mix, different make/buy, more efficient method), or escalates an unbridgeable gap to pricing and capture.

**Anti-behavior:**
- Does not ignore the cost target and hand off an unaffordable design.
