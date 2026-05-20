---
name: developing-solution-approach
description: Designs the proposal-ready solution for a US Federal bid. Use when the user needs a solution approach, a technical solution design, solutioning, a solutioning workshop, a staffing or management model, a transition or risk or quality approach, or needs to turn requirements, win themes, and constraints into a designed solution before drafting. Produces the solution design that storyboards and section drafts are built from.
---

# Developing Solution Approach

Design the solution before anyone drafts a section. Storyboarding and section
drafting both assume a solution already exists — a technical approach, a
staffing model, a transition plan, a management structure, a risk and quality
approach. Solutioning is the work of designing those, deliberately, from the
requirements, the win themes, and the cost constraints. Skipping it means the
solution gets invented one paragraph at a time by separate authors, and the
proposal describes something incoherent.

## When to use this skill

Use this skill after the win strategy is set and the solicitation has been
shredded (between capture and full proposal development) to design the
solution the proposal will sell. It feeds `outlining-proposals` (the storyboards
need a solution to storyboard) and `drafting-proposal-sections` (the sections
need a solution to describe). On a fast task order it may run in a single
solutioning session; on a large bid it is an iterative workshop series.

It does not write proposal narrative (`drafting-proposal-sections`) and does not
set win themes (`developing-win-strategy`). It designs the *what* and *how* that
the narrative will then present persuasively.

## Inputs

**Preferred upstream artifacts:**
- `10-compliance-matrix.md`: the requirements the solution must satisfy.
- `05-win-strategy.md`: the win themes and discriminators the solution must
  embody. A solution that does not deliver the discriminators makes the win
  themes empty.
- `04-price-to-win.md`: the cost target the solution must be designed to hit.
- `03-competitive-assessment.md`: what the solution must beat.
- `00-opportunity-profile.md` and `02-capture-plan.md` — customer context.

**Without the compliance matrix**, run `shredding-solicitations` first — the
solution must be designed against real requirements.

Read `../../shared/glossary.md` and `../../shared/pursuit-workspace.md` if not
already read this session.

## Intake

Ask these as a numbered list. Skip what upstream artifacts answer.

1. **The requirement.** What is the work — the scope, the performance standards,
   the constraints (period of performance, place, security, contract type)?
2. **The win themes.** What discriminators and win themes must the solution
   embody (from `05-win-strategy.md`)?
3. **The cost target.** What price-to-win target must the solution be designed
   to hit (from `04-price-to-win.md`)? Is the evaluation best-value or LPTA?
4. **The customer's hot buttons.** What risks and priorities must the solution
   visibly address — transition risk, staffing, performance, mission urgency?
5. **Constraints and assets.** What does the team bring — existing capability,
   tools, methods, people, partners — and what hard constraints bound the design
   (clearances, facilities, mandated standards)?

## Workflow

```
Solution Design:
- [ ] Step 1: Read upstream artifacts; complete intake
- [ ] Step 2: Frame the design problem — requirements, themes, cost, constraints
- [ ] Step 3: Design each solution element
- [ ] Step 4: Check the design against requirements, themes, and cost
- [ ] Step 5: Resolve trade-offs and record decisions
- [ ] Step 6: Write the solution design (08-solution-design.md)
```

**Step 1: Read and intake.** Read the upstream artifacts; run intake for the
rest.

**Step 2: Frame the problem.** State what the solution must do: satisfy the
compliance-matrix requirements, embody the win themes, fit the price-to-win
target, and address the customer's hot buttons. Use
`references/solutioning-method.md`. A solution designed against only the
requirements is compliant and undifferentiated; a solution designed against only
the themes is differentiated and non-compliant. It must do all of it.

**Step 3: Design each element.** Design the solution elements
(`solutioning-method.md` defines them): the technical approach, the staffing and
management model, the transition approach, the risk approach, and the quality
approach. Each element is designed concretely enough that a section author could
describe it (named methods, defined structure, specific decisions) not left as
a slogan.

**Step 4: Check the design.** Verify the design against three standards:
- Requirements: every compliance-matrix requirement is satisfied by some
  element of the design.
- Win themes: every discriminator in the win strategy is actually delivered
  by the design. A discriminator the design does not deliver is a theme the
  proposal cannot honestly make.
- Cost: the design can be delivered within the price-to-win target. This is
  the design-to-cost discipline: a solution that cannot be priced to win is not
  a solution. Where it cannot, redesign or flag it back to pricing and capture.

**Step 5: Trade-offs.** Solutioning involves trade-offs — richness vs. cost,
innovation vs. risk, scope of the offered approach. Resolve each consciously,
guided by the evaluation approach (best-value rewards value; LPTA rewards clean,
lean acceptability), and record the decision and its rationale so the proposal
is internally consistent and the team does not relitigate it mid-draft.

**Step 6: Write.** Write `08-solution-design.md` using
`templates/solution-design.md`.

## Output

One artifact: `08-solution-design.md` in the pursuit workspace — the designed
solution the storyboards and section drafts build from.

Present the user with: the solution design by element, confirmation that it
covers the requirements and delivers the discriminators, the cost-fit check, and
the trade-off decisions made.

## References

- `references/solutioning-method.md`: the solutioning workshop, the solution elements, designing against requirements/themes/cost, trade-offs, and the design-to-cost discipline.
- `templates/solution-design.md`: the solution design artifact template.

## Guardrails

- **Design before drafting.** The solution is designed here, deliberately, not
  improvised by authors during drafting. If asked to skip solutioning, produce
  the design first and explain why.
- **Design against requirements, themes, and cost together.** All three. A
  solution missing any one of them fails.
- **Deliver the discriminators.** A win theme the design does not actually
  deliver is a claim the proposal cannot support. Either the design delivers it
  or the win strategy is wrong.
- **Design to cost.** A solution that cannot be delivered within the
  price-to-win target is not done. Redesign, or escalate to pricing and capture.
- **Concrete, not aspirational.** Design the solution the team can actually
  deliver and staff. An aspirational design becomes a performance failure.
