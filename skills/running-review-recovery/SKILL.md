---
name: running-review-recovery
description: Runs proposal review recovery for a US Federal bid. Use when the user needs to work color team findings, run recovery after a Pink, Red, or Gold review, assign and track finding closure, verify fixes against Section M and the compliance matrix, or produce a recovery status dashboard. Turns review findings into assigned, completed, and verified corrections before the next milestone.
---

# Running Review Recovery

Turn review findings into fixed proposal. A color team review produces a
findings matrix; recovery is the disciplined work of closing every finding that
matters before the next milestone. A Red Team without recovery is theater — the
weaknesses were found and then shipped anyway. This skill owns the recovery
process: assign each finding, drive the rewrites, verify each fix against the
standard, and report a burn-down the team can trust.

## When to use this skill

Use this skill immediately after a color team review (`reviewing-color-teams`),
in the recovery window the schedule reserves. Run it after a Pink, Red, or Gold
review — any review that produced findings to work.

It does not perform the reviews (`reviewing-color-teams`) and does not write
proposal content (the drafting skills). It manages the closure of findings and
verifies it.

## Inputs

**Required:**
- The color review artifact (`20-color-review-<team>.md`) with its findings
  matrix.
- `10-compliance-matrix.md`: the standard each fix is verified against.
- The proposal content the findings point to — `12-sections/` and the volume
  artifacts.

**Preferred upstream artifacts:**
- The solicitation Section M — the scoring standard the fixes must satisfy.
- `09-proposal-management/`: the schedule, so recovery fits the window, and the
  action register, which recovery actions feed into.

Read `../../shared/glossary.md` and `../../shared/pursuit-workspace.md` if not
already read this session.

## Intake

Ask these as a numbered list.

1. **Which review.** Which color review's findings is this recovery working, and
   where is the findings matrix?
2. **The recovery window.** How much time is there before the next milestone
   (the next review, or submission)?
3. **The team.** Who is available to make the fixes — the section authors,
   volume leads?
4. **Scope.** Recover all findings, or a defined subset (for example,
   deficiencies and significant weaknesses only, given a short window)?

## Workflow

```
Review Recovery:
- [ ] Step 1: Load the findings matrix; complete intake
- [ ] Step 2: Triage and prioritize the findings
- [ ] Step 3: Assign each finding to an owner with a due date
- [ ] Step 4: Drive the fixes (the rewrite loop)
- [ ] Step 5: Verify each fix against the standard
- [ ] Step 6: Maintain the recovery dashboard; report status
- [ ] Step 7: Write the recovery artifact (23-review-recovery.md)
```

**Step 1: Load.** Read the color review's findings matrix and the compliance
matrix.

**Step 2: Triage.** Sort the findings by severity using
`references/recovery-method.md`: deficiencies first (the proposal is unawardable
until each is closed), then significant weaknesses, then weaknesses, then
strength opportunities, then administrative items. Against the recovery window,
decide what *must* close before the next milestone and what can wait. If the
window cannot fit the must-fix findings, that is a schedule problem to escalate
now (see the method file).

**Step 3: Assign.** Give every finding to be worked an owner and a due date
inside the recovery window. Each finding becomes a tracked recovery item. Feed
these into the `09-proposal-management/` action register if it exists.

**Step 4: Drive the fixes.** For each finding, the owner makes the correction —
using `drafting-proposal-sections` (or the relevant volume skill) for content
fixes. The recovery skill tracks the rewrite loop: in progress, drafted, ready
for verification.

**Step 5: Verify closure.** A finding is not closed because someone edited the
section. It is closed when the fix is *verified against the standard*: the
corrected content satisfies the requirement (compliance matrix) and answers the
evaluation concern (Section M) the finding raised. Verify each fix explicitly.
A deficiency is closed only when the requirement is demonstrably met. Re-open any
fix that does not actually resolve the finding.

**Step 6: Dashboard.** Maintain a recovery dashboard: per finding, the
severity, owner, status, and verification result; and a burn-down — how many
findings of each severity remain open against the time left. The dashboard tells
the proposal manager, honestly, whether recovery is on track.

**Step 7: Write.** Write `23-review-recovery.md` using
`templates/recovery-dashboard.md`. Update the compliance matrix status for every
requirement a fix touched.

## Output

One artifact: `23-review-recovery.md` — the recovery dashboard and verification
record. (Re-running after a later review appends or supersedes per the merge
protocol.)

Present the user with: the burn-down (open findings by severity vs. time left),
every deficiency or significant weakness still open, any fix that failed
verification, and an honest statement of whether recovery will complete before
the next milestone.

## References

- `references/recovery-method.md`: triaging findings, assignment, the rewrite loop, verifying closure against the standard, the burn-down, and recognizing when recovery itself is at risk.
- `templates/recovery-dashboard.md`: the recovery dashboard artifact template.

## Guardrails

- **Verified, not just edited.** A finding closes only when the fix is verified
  to satisfy the requirement and answer the evaluation concern. "The author
  changed it" is not closure.
- **Deficiencies first, always.** A deficiency makes the proposal unawardable.
  Every deficiency closes before lower-severity work, regardless of how easy the
  easy items are.
- **Honest burn-down.** Report recovery status truthfully. A dashboard that
  shows green while deficiencies are open denies the team the chance to react.
- **Escalate an unworkable window.** If the must-fix findings cannot be closed
  in the time available, say so immediately — it is a schedule decision for the
  proposal manager, not something to absorb silently.
- **Recovery manages fixes; it does not invent content.** The corrections are
  made by the drafting skills, by named owners.
