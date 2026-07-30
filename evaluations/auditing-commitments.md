# Evaluations: auditing-commitments

## Eval 1 — A promise stronger than the requirement is caught and priced

**Scenario:** The SLA in Section C requires 99.5% monthly availability. The draft technical volume states "we guarantee 100% availability and zero unplanned downtime."

**Inputs:** The draft technical volume and `10-compliance-matrix.md` containing the 99.5% requirement.

**Expected behavior:**
- Extracts "guarantee", "100%" and "zero" as separate candidate items.
- Quotes the 99.5% requirement verbatim and classifies the promise as **stronger** than required.
- States what the delta costs to perform over the period of performance.
- Notes that Section M awards no credit for exceeding 99.5%.
- Recommends a bounded form with a measurement window and stated exclusions.
- Writes `19-commitment-audit.md`.

**Anti-behavior:**
- Does not edit the draft to say 99.5%.
- Does not report the delta without a cost consequence.

## Eval 2 — The absolute is treated as its own category

**Scenario:** A draft contains "zero defects", "at all times", and "any and all data" in three different sections.

**Inputs:** The draft; no requirement uses absolute language.

**Expected behavior:**
- Classifies all three as absolutes rather than ordinary obligations.
- States that each is uninsurable as written and that one counter-example is a documented failure.
- Records `NONE FOUND` for the requirement on each.

**Anti-behavior:**
- Does not fold absolutes into the general obligation count without flagging them separately.
- Does not treat "no requirement found" as a reason to skip the row.

## Eval 3 — A number the staffing plan does not fund

**Scenario:** The draft commits to a fifteen-minute response time around the clock. `08-solution-design.md` funds a single 8×5 shift.

**Inputs:** The draft, the compliance matrix, and the solution design.

**Expected behavior:**
- Identifies the mismatch between the commitment and what is staffed.
- Places the item on the "promises the solution does not support" list.
- States explicitly that this is a solution or bid decision, not a wording fix, and assigns it for escalation.

**Anti-behavior:**
- Does not propose rewording the response time to match the staffing plan without flagging that the requirement may then go unmet.
- Does not pass it as compliant because the language sounds strong.

## Eval 4 — Volunteered scope is identified as give-away

**Scenario:** The draft offers a free public dashboard. The solicitation never requests one and Section M does not evaluate it.

**Inputs:** The draft and the compliance matrix.

**Expected behavior:**
- Records `NONE FOUND` for the requirement.
- Names the recurring cost over the period of performance and the additional obligations it carries, including data exposure.
- Checks `05-win-strategy.md` to see whether it is a deliberate differentiator; if not, recommends cutting it or pricing it as an option.

**Anti-behavior:**
- Does not silently keep it because it sounds generous.
- Does not assume it must be a differentiator because it appears in the draft.

## Eval 5 — Omitted conditions on a technical performance figure

**Scenario:** The draft states the system removes 95% of a contaminant. Performance depends on inlet composition the customer supplies.

**Inputs:** The draft and any available test data description.

**Expected behavior:**
- Flags the figure as an unconditional promise as written.
- Adds a row to the conditions register naming the dependency outside the offeror's control.
- Suggests a bounded form that binds the figure to the conditions under which it was demonstrated.

**Anti-behavior:**
- Does not accept the figure as safe because it is below 100%.
- Does not invent a test condition or a standard that was not supplied.

## Eval 6 — The skill declines to rewrite the proposal

**Scenario:** The user asks the skill to "just fix all the overcommitments" in the draft.

**Inputs:** The draft with several stronger-than-required promises.

**Expected behavior:**
- Produces the audit and the recommended bounded forms in the register.
- Explains that editing the draft belongs to `running-review-recovery`, and that each stronger promise may be a deliberate differentiator the capture lead should decide on.
- Shows before and after for any recommended change rather than applying it.

**Anti-behavior:**
- Does not silently rewrite the draft.
- Does not soften a promise without recording what was changed and why.
