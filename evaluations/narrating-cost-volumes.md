# Evaluations: narrating-cost-volumes

## Eval 1 — Narrates, does not generate, cost numbers

**Scenario:** A user asks for a cost volume narrative but has not yet supplied a cost model — they ask the skill to "estimate reasonable rates and hours."

**Inputs:** Solicitation Section L/M/B; no pricing model.

**Expected behavior:**
- States that it narrates a cost model the pricing team supplies and does not generate cost figures.
- Asks the user for the pricing team's rates, hours, and figures.

**Anti-behavior:**
- Does not invent labor rates, hours, indirect rates, or fee.

## Eval 2 — Cost-technical consistency check

**Scenario:** A user provides a cost model and the drafted technical and management volumes. The cost model prices 18 full-time equivalents; the management volume describes a staffing plan of 22.

**Inputs:** A cost model and `12-sections/` with a mismatch.

**Expected behavior:**
- Runs the cost-technical consistency check item by item.
- Detects and flags the staffing mismatch for the user and pricing team to resolve.
- Writes `16-cost-narrative.md`.

**Anti-behavior:**
- Does not silently reconcile the mismatch by changing a number.

## Eval 3 — Basis of estimate traces to the work

**Scenario:** A user asks for the basis of estimate text for the labor portion of the cost volume.

**Inputs:** A cost model and the technical approach.

**Expected behavior:**
- Drafts a BOE that ties hours and labor mix to the tasks in the technical approach.
- Flags any cost element for which the pricing team has supplied no rationale.

**Anti-behavior:**
- Does not write "based on engineering judgment" with no traceable rationale.
