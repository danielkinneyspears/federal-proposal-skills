---
name: outlining-proposals
description: Builds a compliant annotated outline and storyboards for a US Federal proposal. Use when the user needs a proposal outline, annotated outline, storyboards, a proposal structure, section plans, a page budget, or wants to plan a proposal before drafting. Builds the structure directly from Section L and the compliance matrix, and annotates each section with the requirements it covers, the Section M factors it is scored under, the win themes to thread, proof points, graphics concepts, page allocation, and author.
---

# Outlining Proposals

Turn the compliance matrix into a proposal structure: a Section L-compliant
annotated outline and a storyboard for each section. This is the planning step
that proposal teams most often skip and most often regret. Drafting straight
from a requirements list produces a compliant document with no strategy.
Outlining and storyboarding first means every section has a defined job — its
requirements, its evaluation factors, its theme, its proof — before anyone
writes a paragraph.

## When to use this skill

Use this skill after `shredding-solicitations` has produced the compliance
matrix and before `drafting-proposal-sections`. The outline is what the Pink
Team reviews, so it must exist before any serious drafting.

It does not write narrative — that is `drafting-proposal-sections`. It produces
the plan that drafting executes.

## Inputs

**Required:** `10-compliance-matrix.md` — the outline is built from it.

**Preferred upstream artifacts:**
- `05-win-strategy.md`: the win themes and proof points to assign to sections.
- The solicitation Section L — the authoritative structure and page limits.

**Without the win strategy**, the outline is structurally complete but cannot
assign themes; flag every section's theme slot as "to be assigned" and recommend
running `developing-win-strategy`.

Read `../../shared/glossary.md` and `../../shared/pursuit-workspace.md` if not
already read this session.

## Intake

Ask these as a numbered list. Skip what the matrix and solicitation answer.

1. **Volumes and structure.** What volumes does Section L require, and does it
   prescribe the section order and headings within each? (The outline must match
   Section L exactly; Section L wins over any default structure.)
2. **Page limits.** What is the page limit per volume, and what counts against
   it? This drives the page budget.
3. **Win themes.** Is `05-win-strategy.md` available with themes and proof
   points to assign?
4. **Authors.** Are section authors known, so the outline can assign ownership?
5. **Graphics intent.** Does the team have an action-caption and graphics
   convention, or should the outline simply propose graphic concepts per section?

## Workflow

```
Proposal Outline and Storyboards:
- [ ] Step 1: Read the matrix and win strategy; complete intake
- [ ] Step 2: Build the section structure from Section L
- [ ] Step 3: Map every compliance-matrix requirement to a section
- [ ] Step 4: Annotate each section (factors, themes, proof, graphics)
- [ ] Step 5: Build the page budget
- [ ] Step 6: Write a storyboard for each section
- [ ] Step 7: Write the outline (11-proposal-outline.md) and validate
```

**Step 1: Read and intake.** Read the compliance matrix and win strategy.

**Step 2: Section structure.** Build the outline's heading structure directly
from Section L, using `references/annotated-outline-method.md`. The structure
mirrors Section L's prescribed volumes, order, and headings. Where Section L is
silent on sub-structure, structure to Section M so the evaluator finds each
factor where they expect it.

**Step 3: Map requirements to sections.** Assign every requirement in the
compliance matrix to exactly one home section. Update the matrix's "Volume &
section" column as you go. Two checks: every requirement has a home (no orphans),
and no section is missing requirements it logically owns. An unassigned
mandatory requirement is a planned deficiency.

**Step 4: Annotate.** For each section, record: the requirement IDs it covers,
the Section M factor(s) it is scored under, the win theme it threads, the proof
points it must land, the graphic concept(s), the page allocation, and the
author. This annotation is what makes the outline a plan rather than a table of
contents.

**Step 5: Page budget.** Allocate the volume's page limit across sections.
Weight pages toward the highest-value Section M factors, not evenly. A section
worth little in Section M does not earn many pages. The budget must sum to at or
under the limit.

**Step 6: Storyboards.** Write a storyboard for each substantive section using
`references/storyboarding.md`: the section's theme statement, the customer issue
it answers, the proof points, the graphic concept, the requirements covered, and
the intended evaluator takeaway. The storyboard is the writer's instruction
sheet and the Pink Team's review object.

**Step 7: Write and validate.** Write `11-proposal-outline.md` using
`templates/proposal-outline.md`. Run its validation checklist: the structure
matches Section L, every matrix requirement is mapped to exactly one section,
every section is annotated, the page budget sums within the limit, and every
substantive section has a storyboard.

## Output

One artifact: `11-proposal-outline.md` — the annotated outline plus the
storyboards. Also updates the "Volume & section" column of
`10-compliance-matrix.md`.

Present the user with: the volume/section structure, the page budget, any
requirements that were hard to place, and any sections with weak theme or proof
coverage.

## References

- `references/annotated-outline-method.md`: building the structure from Section L, mapping requirements, annotating sections, and page budgeting.
- `references/storyboarding.md`: the storyboard sheet, writing a theme statement, graphic concepts, and the storyboard review.
- `templates/proposal-outline.md`: the annotated outline and storyboard templates and the validation checklist.

## Guardrails

- **Section L is the structure.** The outline mirrors Section L's prescribed
  organization exactly. An evaluator following Section L must find every section
  where they expect it. Do not impose a "better" structure.
- **No orphan requirements.** Every compliance-matrix requirement maps to exactly
  one section. Zero is a planned miss; two is duplicated effort and risk.
- **Pages follow value.** Budget pages by Section M importance, not evenly.
- **Plan before prose.** This skill produces a plan. If asked to "just write the
  proposal," produce the outline and storyboards first and say why.
