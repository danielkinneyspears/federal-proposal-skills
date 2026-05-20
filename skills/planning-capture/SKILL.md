---
name: planning-capture
description: Builds and maintains a living capture plan for a US Federal opportunity in the pre-RFP capture phase. Use when the user needs a capture plan, capture strategy, customer call plan, customer engagement or shaping plan, or wants to organize pre-RFP positioning work, intelligence gaps, teaming actions, and capture milestones. Produces a capture plan artifact with assigned, dated action items aimed at raising probability of win before the RFP releases.
---

# Planning Capture

Build and maintain the capture plan — the living document that drives pre-RFP
work to raise probability of win. A capture plan is not a report. It is an
action system: its real output is a set of assigned, dated actions that change
the team's position before the RFP releases. A capture plan with no actions, or
actions with no owners and no dates, is decoration.

## When to use this skill

Use this skill after a pursuit decision (see `qualifying-opportunities`) when
the opportunity will be actively pursued and the team needs to organize capture
work: understanding the customer, shaping the requirement, closing intelligence
gaps, securing teaming partners, and tracking it all to gate reviews.

Re-run it throughout the capture phase to update the plan as intelligence
arrives and actions close.

Related skills this one does not replace:
- `analyzing-competitors`: the deep Black Hat competitive assessment. The
  capture plan summarizes and links to it.
- `estimating-price-to-win`: the price-to-win analysis.
- `developing-win-strategy`: the win themes and discriminators. The capture
  plan references the win strategy; it does not derive it.

This skill is the hub; those three are spokes. The capture plan integrates them.

## Inputs

**Preferred upstream artifacts:**
- `00-opportunity-profile.md` and `01-bid-decision.md` — the opportunity facts
  and the pursuit rationale. Read them first; do not re-ask what they answer.
- `03-competitive-assessment.md`, `04-price-to-win.md`, `05-win-strategy.md` —
  if they exist, summarize and link them. If they do not, the capture plan
  records them as planned capture actions.

**Without them**, run the intake below to establish the opportunity facts, then
build the plan, flagging the missing analyses as actions to commission.

Read `../../shared/glossary.md`, `../../shared/proposal-lifecycle.md`, and
`../../shared/pursuit-workspace.md` if not already read this session.

## Intake

Ask these as a numbered list. Skip what upstream artifacts already answer.

1. **The customer.** Which agency, program office, and end user? What is their
   mission and the problem this acquisition is meant to solve? Who are the known
   decision-makers, influencers, and the likely contracting officer?
2. **Customer relationship and engagement to date.** What contact has the team
   had? Any meetings, RFI responses, white papers, capability briefings, or
   draft-RFP comments? What is the current access?
3. **The requirement and acquisition.** What is known about scope, likely
   contract type and value, anticipated RFP timing, set-aside status, and
   contract vehicle? Is a draft RFP, RFI, or sources-sought notice available?
4. **Position and gaps.** What are the team's strengths and weaknesses for this
   pursuit? Where is past performance thin? What capability or qualification
   gaps would require teaming?
5. **What is unknown.** What does the team *not* know about the customer's hot
   buttons, budget, incumbent satisfaction, evaluation intent, or competitive
   field? These unknowns become intelligence actions.
6. **Capture resources and timeline.** Who is on the capture team, and what gate
   reviews and dates are the pursuit working toward?

Unknowns are the most valuable answers here. The capture plan's job is to close
them.

## Workflow

```
Capture Planning:
- [ ] Step 1: Read upstream artifacts; complete intake
- [ ] Step 2: Analyze the customer and the requirement
- [ ] Step 3: Assess our position; identify intelligence gaps
- [ ] Step 4: Define the customer engagement / call plan
- [ ] Step 5: Define teaming actions
- [ ] Step 6: Build the capture action list (owners, dates, gates)
- [ ] Step 7: Write the capture plan (02-capture-plan.md) and validate
```

**Step 1: Read and intake.** Read the upstream artifacts. Run intake only for
what they do not cover.

**Step 2: Customer and requirement.** Build the customer analysis using
`references/capture-plan-structure.md`: mission, organization, decision-makers,
known hot buttons and biases, budget signals, and how the requirement is likely
to evolve. Mark each item as *known*, *assessed* (inferred), or *unknown*.

**Step 3: Position and gaps.** Record the team's strengths and weaknesses for
this specific customer and requirement. Then list **intelligence gaps** — the
specific things the team does not know that would change the win strategy or
pWin. Each gap becomes a capture action in Step 6.

**Step 4: Customer engagement plan.** Build the call plan using
`references/customer-engagement.md`: which customer contacts to engage, the
objective of each engagement, the legitimate shaping vehicles available (RFI
responses, white papers, capability briefings, draft-RFP comments), and the
timing relative to RFP release. Stay within the ethical and legal limits stated
in that file.

**Step 5: Teaming.** From the capability and past-performance gaps in Step 3,
define what the team needs from partners, candidate partners, and the actions to
secure teaming agreements before they constrain the bid.

**Step 6: Capture action list.** Convert every gap, engagement, and teaming
need into a concrete action with an **owner**, a **due date**, and the **gate**
it supports. This list is the heart of the plan. An action without an owner and
a date is not an action.

**Step 7: Write and validate.** Write `02-capture-plan.md` using
`templates/capture-plan.md`. Run that template's validation checklist: every
plan section is present, every customer fact is marked known/assessed/unknown,
every intelligence gap has a corresponding action, and every action has an owner
and a date. Revise until it passes.

## Output

One artifact: `02-capture-plan.md` in the pursuit workspace — a living document
updated throughout capture.

Present the user with: the capture plan summary, the most important intelligence
gaps, the next customer engagements, and the highest-priority actions due before
the next gate.

## References

- `references/capture-plan-structure.md`: the full capture plan structure and what each section must contain.
- `references/customer-engagement.md`: building a customer call plan, legitimate requirement-shaping vehicles, and the ethical and legal limits on customer contact.
- `templates/capture-plan.md`: the capture plan artifact template and its validation checklist.

## Guardrails

- **Actions, not prose.** The plan's value is the action list. Resist producing
  a polished narrative with no assigned, dated actions.
- **Mark what is known vs. assumed.** Never present an inferred customer hot
  button as established fact. Label assessments as assessments.
- **Stay inside the ethical line.** Requirement shaping and customer engagement
  are legitimate, but procurement integrity rules are strict. Follow the limits
  in `references/customer-engagement.md`; never recommend seeking
  source-selection-sensitive or non-public competitor information.
- **The capture plan is sensitive.** It holds competitive and customer
  intelligence. It stays in the git-ignored pursuit workspace.
