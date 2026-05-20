---
name: estimating-price-to-win
description: Produces a price-to-win analysis for a US Federal opportunity. Use when the user needs price-to-win, PTW, a competitive pricing analysis, a price target or price range, or wants to understand pricing strategy, cost drivers, and pricing levers for a federal bid. Estimates the competitive price range and a target price the bid must reach to win, independent of a bottom-up cost estimate, and reconciles that target against the team's likely cost.
---

# Estimating Price-to-Win

Estimate the price the bid has to reach to win — built from the customer's
budget and competitors' likely pricing, not from the team's own cost. Price-to-win
(PTW) and a bottom-up cost estimate answer different questions. The cost estimate
says what the work *costs the team*. PTW says what the customer is *willing and
likely to pay the winner*. When those two numbers differ, PTW analysis finds the
levers that close the gap — or proves the bid cannot be won profitably.

## When to use this skill

Use this skill during capture, after a competitive assessment exists, to
establish the price target that shapes the win strategy and, later, the cost
volume. Re-run it when the competitive picture or budget signals change, and
again when the RFP clarifies the contract type, evaluation weighting, and CLIN
structure.

This skill estimates the *target*. It does not build the bottom-up cost estimate
or write the cost volume narrative — that is `narrating-cost-volumes`. It hands
the target to that skill and to `developing-win-strategy`.

## Inputs

**Preferred upstream artifacts:**
- `00-opportunity-profile.md`: contract type, estimated value, period of performance, scope.
- `02-capture-plan.md`: customer budget signals and acquisition history.
- `03-competitive-assessment.md`: the competitors and their assessed price postures and cost structures. PTW depends heavily on this; run `analyzing-competitors` first if it is missing.

**Without the competitive assessment**, the skill can still produce a budget-based
estimate, but it must flag that the competitor-price leg of the analysis is
missing and confidence is reduced.

Read `../../shared/glossary.md`, `../../shared/federal-solicitation-primer.md`,
and `../../shared/pursuit-workspace.md` if not already read this session.

## Intake

Ask these as a numbered list. Skip what upstream artifacts answer.

1. **The buy.** Contract type (FFP, T&M, cost-reimbursement, hybrid), scope,
   period of performance including option years, and CLIN structure if known.
2. **The evaluation.** Is the approach best-value tradeoff or LPTA? How is price
   weighted against non-price factors? For cost-reimbursement work, will the
   government perform a cost-realism analysis? (If the RFP is out, Section M
   answers this.)
3. **Budget signals.** What is known or assessed about the customer's budget —
   the funding line, an independent government cost estimate if signaled, the
   prior contract's value, or the value of comparable awards?
4. **The team's cost picture.** What is the team's rough bottom-up cost view, if
   any — labor mix, wrap rates, subcontractor content, escalation assumptions?
   (Used to size the gap, not to set the target.)
5. **Pricing flexibility.** Where does the team have real room to move — labor
   mix, indirect rates, fee, escalation, subcontractor selection, solution scope
   choices, the make/buy split?
6. **Strategic posture.** Is this a must-win where the team will price thin, a
   margin-priority bid, or somewhere between?

## Workflow

```
Price-to-Win Analysis:
- [ ] Step 1: Read upstream artifacts; complete intake
- [ ] Step 2: Establish the evaluation context (pricing posture)
- [ ] Step 3: Estimate the customer budget / ceiling
- [ ] Step 4: Estimate competitors' likely prices
- [ ] Step 5: Set the price-to-win range and target
- [ ] Step 6: Reconcile target against the team's cost; identify levers
- [ ] Step 7: Write the analysis (04-price-to-win.md) and validate
```

**Step 1: Read and intake.** Read upstream artifacts; run intake for the rest.

**Step 2: Evaluation context.** Using `references/pricing-by-evaluation-type.md`,
establish what kind of pricing problem this is. LPTA, best-value tradeoff, and
cost-reimbursement with realism analysis each demand a different posture. Get
this right first — it governs everything after.

**Step 3: Customer budget.** Estimate the customer's likely budget or ceiling
from the signals available: funding lines, a signaled IGCE, the prior contract's
value adjusted for scope and escalation, comparable awards. Give a range, not a
false point, and state the basis.

**Step 4: Competitor prices.** For each competitor in the competitive
assessment, estimate a likely price using the method in `references/ptw-method.md`:
their assessed cost structure, their assessed posture (aggressive / market /
premium), and their likely solution scope. Produce a range per competitor.

**Step 5: PTW range and target.** Combine the budget ceiling and the competitor
price estimates into a price-to-win range, then set a target price within it,
consistent with the evaluation posture from Step 2. For LPTA, the target is at
or below the lowest credible competitor price while staying realistic. For
best-value, the target is the highest price the team's non-price advantage can
justify against the field.

**Step 6: Reconcile and find levers.** Compare the PTW target against the
team's bottom-up cost view. If cost is at or below target, confirm the margin.
If cost exceeds target, identify the specific levers (from `ptw-method.md`) that
could close the gap and quantify each. If no realistic combination of levers
closes the gap without making the bid unrealistic or unprofitable, **say so
plainly** — that finding feeds straight back to the bid/no-bid decision.

**Step 7: Write and validate.** Write `04-price-to-win.md` using
`templates/price-to-win.md`. Run its validation checklist: the evaluation
posture is identified, every estimate is a sourced range not a false precision
point, the target is consistent with the posture, and the cost-to-target gap is
either closed with named levers or honestly declared unbridgeable.

## Output

One artifact: `04-price-to-win.md` in the pursuit workspace.

Present the user with: the recommended target price (as a range with a point
recommendation), the PTW range and how it was bounded, the gap to the team's
cost and the levers to close it, and the pricing risks.

## References

- `references/ptw-method.md`: estimating budgets and competitor prices, the cost drivers, and the pricing levers.
- `references/pricing-by-evaluation-type.md`: how PTW posture differs for LPTA, best-value tradeoff, and cost-reimbursement with realism analysis.
- `templates/price-to-win.md`: the analysis artifact template and its validation checklist.

## Guardrails

- **PTW is not the cost estimate.** Never substitute the team's bottom-up cost
  for the price-to-win target. They answer different questions.
- **Ranges, not false precision.** Budget and competitor-price estimates are
  ranges with a stated basis. A single confident number is a lie about the
  uncertainty.
- **Realism cuts both ways.** A price below what the work can credibly be done
  for is a risk, not a win — especially under cost-realism evaluation, where the
  government can adjust an unrealistically low cost upward for scoring.
- **An unbridgeable gap is a finding.** If the work cannot be priced to win
  profitably, report that clearly; it belongs back in the bid/no-bid decision.
- **Decision support only.** The target informs the human pricing decision; it
  does not set the price.
