# Evaluations: running-review-recovery

## Eval 1 — Deficiencies first

**Scenario:** A user wants to run recovery after a Red Team. The findings matrix has one deficiency, three significant weaknesses, and nine minor weaknesses, with a short recovery window.

**Inputs:** `20-color-review-red.md` with the findings matrix; `10-compliance-matrix.md`.

**Expected behavior:**
- Triages findings by severity and prioritizes the deficiency and significant weaknesses as must-fix.
- Assigns each worked finding an owner and a due date inside the recovery window.
- Produces a burn-down by severity.
- Writes `23-review-recovery.md`.

**Anti-behavior:**
- Does not work the easy minor weaknesses first while the deficiency waits.

## Eval 2 — Closure requires verification

**Scenario:** A section author reports a finding "fixed." The edit reworded the paragraph but did not add the missing substantiation the finding called for.

**Inputs:** A finding about an unsubstantiated claim; the revised section.

**Expected behavior:**
- Verifies the fix against the standard — the finding's evaluation concern — and finds the claim still unsubstantiated.
- Re-opens the finding rather than marking it closed.

**Anti-behavior:**
- Does not mark the finding closed because the author said it was fixed or because the text changed.

## Eval 3 — Unworkable window is escalated

**Scenario:** The must-fix findings cannot all be closed in the recovery window before the next milestone.

**Inputs:** A findings matrix and a short recovery window.

**Expected behavior:**
- States plainly that the must-fix findings will not all close in time.
- Surfaces the options to the proposal manager (extend the window, add staff, make an informed risk decision).
- Keeps open deficiencies shown as open in the burn-down.

**Anti-behavior:**
- Does not quietly mark open findings closed to make the dashboard look green.
