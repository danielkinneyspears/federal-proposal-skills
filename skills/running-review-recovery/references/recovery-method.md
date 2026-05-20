# Recovery Method

How to turn a findings matrix into closed, verified corrections.

## Contents
- Why recovery is a discipline
- Triage and prioritization
- Assignment
- The rewrite loop
- Verifying closure
- The burn-down
- When recovery is at risk

## Why recovery is a discipline

A color team review only adds value if its findings are worked. The review is
the diagnosis; recovery is the treatment. Teams routinely run a rigorous Red
Team and then, under deadline pressure, fix the easy findings, wave at the hard
ones, and submit — which means the review found the proposal's weaknesses and
the team shipped them anyway. Recovery is the discipline that prevents that.

## Triage and prioritization

Sort every finding by severity (the severities come from the color review):

1. **Deficiencies** — the proposal is unawardable until each is closed. Highest
   priority, without exception.
2. **Significant weaknesses** — appreciably increase risk or lose significant
   credit. Close before the next milestone.
3. **Weaknesses** — cost credit or add risk. Close if the window allows.
4. **Strength opportunities** — places to earn a strength not yet earned.
   Amplify if the window allows.
5. **Administrative** — format and consistency items. Fix in production.

Then size the work against the recovery window. The window is fixed by the
schedule. Decide what must close before the next milestone — at minimum every
deficiency and significant weakness. If the must-fix set does not fit the
window, see "When recovery is at risk" below; do not silently drop findings.

## Assignment

Every finding to be worked gets a single owner and a due date inside the
recovery window. The owner is normally the section's author. Each finding is now
a tracked recovery item with a status. Feed recovery items into the proposal
management action register (`09-proposal-management/`) so recovery is visible in
the one place the team already watches.

## The rewrite loop

For each assigned finding:

1. The owner makes the correction, using `drafting-proposal-sections` or the
   relevant volume skill. The recommended fix in the finding is the starting
   point, not necessarily the final answer — the owner may find a better fix.
2. The recovery item moves through statuses: open → in progress → drafted →
   verified (or re-opened).
3. A fix that touches a requirement updates the compliance matrix.

## Verifying closure

This is the step that separates recovery from the appearance of recovery. A
finding is closed only when its fix is **verified against the standard**:

- **Compliance** — the corrected content satisfies the requirement the finding
  cited. Check it against the compliance matrix row.
- **Evaluation concern** — the fix actually answers the scoring concern the
  finding raised. A weakness about an unsubstantiated claim is closed when the
  claim is now substantiated — not when the paragraph was merely reworded.
- **Deficiencies** — closed only when the requirement is demonstrably,
  completely met. A partially addressed deficiency is still a deficiency.

Verification is done by someone other than the person who made the fix where
possible. A fix that does not resolve the finding is re-opened, not marked
closed. Recording "closed" on an unresolved finding is the most damaging thing
recovery can do, because it removes the finding from view while the weakness
remains in the proposal.

## The burn-down

Maintain a burn-down: the count of open findings, by severity, against the time
remaining in the recovery window. It answers one question for the proposal
manager — will recovery finish in time? Update it as findings close. The
burn-down is honest or it is worthless: an open deficiency is shown as an open
deficiency.

## When recovery is at risk

If the must-fix findings cannot be closed in the recovery window:

- Say so immediately and explicitly. This is a schedule problem, and it is
  manageable only while there is still time to manage it.
- Surface the options to the proposal manager: extend the window (compressing a
  later phase), add people to recovery, or — for a finding that genuinely cannot
  be fixed — make a deliberate, informed decision about the risk of submitting
  with it open.
- Never resolve a recovery crunch by quietly marking open findings closed. A
  hidden open deficiency is a near-certain loss; an acknowledged one is at least
  a decision the team made with its eyes open.
