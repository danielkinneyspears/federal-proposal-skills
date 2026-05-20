---
name: narrating-cost-volumes
description: Drafts the cost or price volume narrative and basis-of-estimate text for a US Federal proposal. Use when the user needs a cost volume narrative, price volume narrative, cost narrative, basis of estimate or BOE, cost-realism narrative, or to check cost-technical consistency for a federal bid. Explains and justifies proposed costs, builds the rationale for each cost element, and verifies the cost volume matches the technical and management volumes.
---

# Narrating Cost Volumes

Draft the cost volume narrative: the words that explain and justify the numbers.
This skill writes the narrative and basis-of-estimate text around a cost model
the user's pricing or finance team has built. It does not build the cost model
and does not produce cost figures. Its job is to make the proposed costs
understandable, credible, realistic, and consistent with the rest of the
proposal.

## When to use this skill

Use this skill once the pricing team has a cost estimate and the technical and
management volumes are drafted, to write the cost volume narrative, the basis of
estimate, and the cost-realism and reasonableness narrative, and to check that
the cost volume agrees with the rest of the proposal.

It is not a pricing tool. It does not set rates, build cost models, or estimate
hours — those are the pricing team's work and the subject of
`estimating-price-to-win` on the strategy side.

## Inputs

**Required:**
- The cost model and figures from the user's pricing team — labor categories,
  hours, rates, indirect rates, fee, ODCs, by CLIN and period.
- The solicitation's cost volume instructions (Section L) and cost evaluation
  criteria (Section M), and the Section B CLIN structure.

**Preferred upstream artifacts:**
- `12-sections/`: the technical and management volumes, for the
  cost-technical consistency check.
- `04-price-to-win.md`: the price posture the bid is taking.
- `10-compliance-matrix.md`: the cost volume requirement rows.

**Without the cost model**, this skill cannot produce a cost volume. Ask the
user for the pricing team's figures; do not generate cost numbers.

Read `../../shared/glossary.md`, `../../shared/federal-solicitation-primer.md`,
and `../../shared/pursuit-workspace.md` if not already read this session.

## Intake

Ask these as a numbered list. Skip what the solicitation answers.

1. **The cost model.** What are the proposed costs, by CLIN and period — labor
   categories, hours, direct rates, indirect rates, fee, escalation, ODCs? Who
   on the pricing team owns them?
2. **Cost volume instructions.** What does Section L require — format, CLIN
   structure, supporting detail, a separate basis of estimate, cost element
   breakdowns, the page or file rules?
3. **Cost evaluation.** How does Section M evaluate cost or price — reasonableness,
   realism (cost-reimbursement), total evaluated price, options? Is this
   best-value or LPTA?
4. **Contract type.** FFP, T&M, cost-reimbursement, or hybrid? (This governs how
   much cost detail and realism narrative is needed.)
5. **Cost-technical link.** Are the technical and management volumes drafted, so
   the cost volume can be checked against the staffing and approach they propose?

## Workflow

```
Cost Volume Narrative:
- [ ] Step 1: Read the cost model, Section L/M cost rules, and the volumes
- [ ] Step 2: Structure the cost volume to Section L and the CLINs
- [ ] Step 3: Draft the basis of estimate for each cost element
- [ ] Step 4: Draft the realism and reasonableness narrative
- [ ] Step 5: Run the cost-technical consistency check
- [ ] Step 6: Write the artifact (16-cost-narrative.md) and update the matrix
```

**Step 1: Read.** Read the cost model, the Section L cost instructions and
Section M cost criteria, and the technical and management volumes.

**Step 2: Structure.** Structure the cost volume to Section L and the Section B
CLIN structure, using `references/cost-narrative-method.md`. The narrative
follows the CLINs and periods the government will evaluate.

**Step 3: Basis of estimate.** For each significant cost element, draft the
basis of estimate — the rationale for *why* the number is what it is: why this
many hours, this labor mix, these ODCs, this escalation rate. The BOE traces the
cost to the work in the technical approach. A number with no rationale invites a
realism or reasonableness challenge.

**Step 4: Realism and reasonableness narrative.** Draft the narrative that
supports the price. For cost-reimbursement work, the realism narrative shows the
proposed cost is realistic for the proposed approach (see the method file and
the solicitation primer on cost-realism analysis). For all types, the
reasonableness narrative supports that the price is fair. Match the depth to the
contract type and Section M.

**Step 5: Cost-technical consistency check.** This is the step that prevents
the most common and most damaging cost-volume failure. Verify the cost volume
agrees with the technical and management volumes, item by item: the labor
categories and staffing levels priced match those the technical volume proposes;
the approach priced is the approach described; the period of performance,
deliverables, travel, and materials are consistent across volumes. Any
mismatch — staffing in the cost volume that differs from staffing in the
technical volume — is a finding the government's evaluators will catch. Flag
every inconsistency for the user and the pricing team to resolve.

**Step 6: Write and update.** Write `16-cost-narrative.md` using
`templates/cost-narrative.md`. Update the cost volume rows of
`10-compliance-matrix.md`.

## Output

One artifact: `16-cost-narrative.md` — the cost volume narrative and basis of
estimate. Cost figures in it are the pricing team's, transcribed, not generated.

Present the user with: the drafted narrative, the cost-technical inconsistencies
found (the most important output), and any cost element whose basis of estimate
the pricing team still needs to supply.

## References

- `references/cost-narrative-method.md`: the cost volume's job, basis-of-estimate construction, the realism and reasonableness narrative, and the cost-technical consistency check.
- `templates/cost-narrative.md`: the cost volume narrative artifact template.

## Guardrails

- **Do not generate cost numbers.** This skill narrates a cost model the pricing
  team provides. It never invents rates, hours, or figures. A missing number is
  requested from the pricing team, never filled in.
- **Cost-technical consistency is the priority.** The most damaging cost-volume
  error is a cost volume that contradicts the technical volume. Check it
  rigorously and flag every mismatch.
- **Realism cuts both ways.** Do not narrate an unrealistically low cost as a
  strength; under cost-realism evaluation the government can adjust it upward.
- **Respect volume separation.** Many solicitations require price to be kept out
  of the technical volume entirely. Honor Section L's separation rules.
- **The BOE must trace to work.** Every basis of estimate ties the cost to the
  proposed approach. "Engineering judgment" with no traceable rationale is weak.
