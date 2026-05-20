---
name: managing-proposal-operations
description: Runs a US Federal proposal as a managed project. Use when the user needs a proposal management plan, a proposal schedule or calendar, a proposal kickoff, volume plan, author assignments or RACI, an action item register, a question log, amendment impact tracking, review logistics, or production planning. Owns the operational backbone that turns the proposal artifacts into a coordinated, on-time, compliant submission.
---

# Managing Proposal Operations

Run the proposal as a project. The other proposal skills produce artifacts — a
compliance matrix, an outline, drafted sections. This skill produces the
*operating system* that gets those artifacts written, reviewed, corrected, and
submitted on time by the right people. In real proposal shops this is where bids
are won or lost operationally: a strong solution that misses the schedule, skips
a review, or fumbles an amendment still loses.

## When to use this skill

Use this skill at proposal kickoff — when the RFP releases (or a draft RFP makes
kickoff worthwhile) — and throughout the proposal phase to keep the effort on
track. It is the hub skill for proposal development: it coordinates the work
that `shredding-solicitations`, `outlining-proposals`, the drafting skills, the
review skills, and `checking-submission-compliance` perform.

It does not produce proposal content. It produces the plan, schedule,
assignments, action register, question log, and review logistics that the
content skills run inside.

## Inputs

**Required:** the solicitation, including Section L (volumes, format, due date)
and any submission instructions.

**Preferred upstream artifacts:**
- `10-compliance-matrix.md`: the requirement inventory the volume plan and
  assignments are built around.
- `00-opportunity-profile.md`, `05-win-strategy.md` — orienting context.

Read `../../shared/glossary.md`, `../../shared/proposal-lifecycle.md`, and
`../../shared/pursuit-workspace.md` if not already read this session. Perform the
workspace bootstrap described in `pursuit-workspace.md` if this is the first
artifact in the pursuit.

## Intake

Ask these as a numbered list. Skip what the solicitation answers.

1. **The deadline.** What is the exact proposal due date, time, and time zone?
2. **The volumes.** What volumes does Section L require, and what are their page
   limits?
3. **The team.** Who is available — proposal manager, capture manager, volume
   leads, authors, reviewers, pricing, production, contracts — and what is each
   person's availability?
4. **The schedule constraints.** What review milestones does the team intend
   (Pink, Red, Gold, others)? Are there holidays, competing deadlines, or
   approval gates that constrain the calendar?
5. **State of the pursuit.** Has the solicitation been shredded? Does a
   compliance matrix exist? Have any amendments or Q&A been issued?

## Workflow

```
Proposal Operations Setup:
- [ ] Step 1: Run kickoff intake; perform workspace bootstrap if first artifact
- [ ] Step 2: Build the proposal schedule backward from the deadline
- [ ] Step 3: Build the volume plan and author assignments (RACI)
- [ ] Step 4: Stand up the action item register
- [ ] Step 5: Stand up the question log and amendment process
- [ ] Step 6: Build the review and production plan
- [ ] Step 7: Write the proposal management plan; maintain it through the phase
```

**Step 1: Kickoff.** Run intake. Confirm the deadline and the team. This is the
kickoff: the moment the proposal becomes a managed effort.

**Step 2: Schedule.** Build the schedule *backward* from the due date, using
`references/proposal-management-plan.md`: submission, production buffer, Gold
Team, recovery, Red Team, recovery, drafting, Pink Team, storyboards,
compliance matrix. Backward scheduling is the only honest way — it shows whether
the available time is enough, and surfaces a schedule crisis while it can still
be managed.

**Step 3: Volume plan and assignments.** Map the volumes and their sections to
named owners. Build a RACI (responsible, accountable, consulted, informed) for
each volume and major section. Every section has exactly one accountable author.
Cross-check against the compliance matrix `Owner` column.

**Step 4: Action register.** Stand up the action item register: every open
action with an owner, a due date, and a status. The action register is the
team's shared list of what is not yet done.

**Step 5: Question log and amendments.** Stand up the question log and the
amendment process using `references/question-and-amendment-control.md`: capture
every question the team has for the contracting officer, draft them for
submission by the deadline, log every government answer, and run an impact
analysis on every amendment (what changed in Section L, M, C, the due date, and
which requirements and artifacts must update).

**Step 6: Review and production plan.** Schedule the color reviews (timing,
participants, materials, logistics) and the production process (assembly,
formatting, the final compliance check, submission mechanics). Coordinate with
`reviewing-color-teams`, `running-review-recovery`, and
`checking-submission-compliance`.

**Step 7: Write and maintain.** Write the `09-proposal-management/` artifact
set using `templates/proposal-management-plan.md`. Then *maintain* it: the
schedule, action register, and question log are living and are updated daily.
Re-running this skill updates them per the merge protocol in
`pursuit-workspace.md`.

## Output

A directory `09-proposal-management/` in the pursuit workspace containing the
proposal management plan, schedule, assignments/RACI, action register, question
log, and review plan.

Present the user with: the schedule with its critical milestones, the
assignment gaps (sections with no owner), the open high-priority actions, the
status of outstanding questions and amendments, and any point where the
schedule is at risk.

## References

- `references/proposal-management-plan.md`: what the proposal management plan contains, backward scheduling from the deadline, the volume plan and RACI, and the daily operating cadence.
- `references/question-and-amendment-control.md`: the question log, drafting formal questions to the contracting officer, processing government answers, and amendment impact analysis.
- `templates/proposal-management-plan.md`: the proposal management artifact set template.

## Guardrails

- **Schedule backward from the deadline.** The due date is fixed; everything
  else is derived from it. Forward scheduling hides the crunch until it is too
  late to manage.
- **Every section has one accountable owner.** Unassigned sections and shared
  accountability are how requirements get missed.
- **The plan is living.** A proposal management plan written once and never
  updated is worse than none — it creates false confidence. Maintain it daily.
- **Amendments are not minor.** Every amendment gets an impact analysis. A
  changed due date or Section L rule that the team does not absorb is a
  predictable loss.
- **This skill coordinates; it does not write content.** Proposal narrative is
  the drafting skills' work.
