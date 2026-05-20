# Evaluations: writing-executive-summaries

## Eval 1 — Persuasion, not a recap

**Scenario:** A user asks for an executive summary and a win strategy artifact exists.

**Inputs:** `05-win-strategy.md`, `10-compliance-matrix.md`.

**Expected behavior:**
- Opens on the customer's mission and problem, not on the offeror.
- Organizes around customer hot buttons and win themes, not the proposal's volume order.
- Gives each theme a benefit-led block with proof.
- Addresses the customer's main risk concern directly.
- Writes `13-executive-summary.md`.

**Anti-behavior:**
- Does not produce a volume-by-volume recap of the proposal.
- Does not open with the offeror's founding date, revenue, or size.

## Eval 2 — The "only here" trap

**Scenario:** Section L states that requirement responses appearing only in the executive summary will not be credited.

**Inputs:** Section L with the restriction.

**Expected behavior:**
- Detects the restriction during intake.
- Ensures every substantive claim in the executive summary is also made and supported in the owning volume.

**Anti-behavior:**
- Does not place a requirement response solely in the executive summary.

## Eval 3 — No win strategy yet

**Scenario:** A user asks for an executive summary but no `05-win-strategy.md` exists.

**Inputs:** Solicitation only.

**Expected behavior:**
- Notes that the executive summary needs win themes to be done well.
- Recommends running `developing-win-strategy` first, or runs intake to establish at least working themes before drafting.

**Anti-behavior:**
- Does not produce a themeless, generic executive summary as if it were complete.
