# Evaluations: managing-proposal-operations

## Eval 1 — Backward scheduling surfaces a crunch

**Scenario:** A user wants to kick off a proposal. The RFP is due in 18 days and they want Pink, Red, and Gold reviews.

**Inputs:** The solicitation with the due date; team roster supplied at intake.

**Expected behavior:**
- Builds the schedule backward from the fixed due date.
- Places a recovery window after each review.
- States explicitly whether the work fits between kickoff and submission, and flags the schedule as at risk if 18 days cannot hold three reviews plus recovery plus production.
- Writes the `09-proposal-management/` artifact set.

**Anti-behavior:**
- Does not forward-schedule from today and leave the crunch hidden.
- Does not present an infeasible schedule as workable.

## Eval 2 — Every section gets one accountable owner

**Scenario:** A user asks for a volume plan and author assignments; the compliance matrix exists.

**Inputs:** `10-compliance-matrix.md`, team roster.

**Expected behavior:**
- Builds a RACI mapping volumes and sections to owners.
- Assigns exactly one accountable author per section.
- Lists any section with no accountable author as an assignment gap.

**Anti-behavior:**
- Does not leave sections unassigned silently or assign shared accountability.

## Eval 3 — Amendment impact analysis

**Scenario:** Mid-proposal, the government issues an amendment that moves the due date earlier by a week and changes a Section L page limit.

**Inputs:** The amendment; an existing `09-proposal-management/` artifact set.

**Expected behavior:**
- Acknowledges the amendment and logs it in the amendment log.
- Rebuilds the schedule backward from the new due date.
- Flags the changed page limit for re-shred and notifies affected section owners.
- Updates the proposal management artifacts per the merge protocol.

**Anti-behavior:**
- Does not treat the amendment as a minor note or leave the schedule unchanged.
