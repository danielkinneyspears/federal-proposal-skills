---
name: qualifying-opportunities
description: Runs a structured bid/no-bid gate review for a US Federal opportunity. Use when deciding whether to pursue or bid a federal solicitation, RFP, RFQ, RFI, sources-sought notice, draft RFP, or IDIQ task order — triggered by requests for a bid/no-bid decision, pursuit decision, gate review, opportunity qualification, capture gate, go/no-go, or pWin assessment. Produces an opportunity profile and a weighted scorecard with a defensible recommendation.
---

# Qualifying Opportunities

Run a disciplined bid/no-bid gate review on a US Federal opportunity and produce
a defensible recommendation. The expensive mistake in federal BD is not losing a
bid — it is spending bid-and-proposal money on bids that were never winnable.
This skill exists to make that decision deliberately, on evidence, against a
consistent standard.

## When to use this skill

Use this skill when a user needs to decide whether to pursue or bid a federal
opportunity, at any gate:

- A new lead or sources-sought notice has appeared and the question is whether to invest capture resources.
- A draft RFP or RFP has released and the question is whether to bid.
- An opportunity already in the pipeline is reaching a gate review.

Do not use this skill to *build the win plan* — that is `planning-capture` and
`developing-win-strategy`. This skill decides whether there should be a win plan
at all. If the decision is already made and the user wants positioning work,
route to those skills instead.

## Inputs

**Preferred upstream artifacts** (from the pursuit workspace, if present):
- `03-competitive-assessment.md`: sharpens the competitive-position scoring.
- `04-price-to-win.md`: sharpens the financial and competitiveness scoring.

**Without them**, the skill still runs: it scores competitive position from what
the user knows and records the lower confidence. A bid/no-bid decision is often
made *before* deep competitive and price analysis exists; that is expected.

Read `../../shared/glossary.md`, `../../shared/proposal-lifecycle.md`, and
`../../shared/pursuit-workspace.md` if you have not already this session.

## Intake

Before scoring anything, establish the facts. Ask the user these questions as a
numbered list. Skip any already answered by a solicitation document or an
existing `00-opportunity-profile.md` in the workspace. Do not guess answers —
unknown is a valid and important answer that lowers confidence and often the
score.

1. **The opportunity.** What is it — agency/office, scope of work, contract type, estimated value, period of performance, set-aside status, and solicitation/notice number? Is there a document (RFI, sources-sought, draft RFP, RFP) available to read?
2. **The gate.** Which decision is this — an early pursuit decision (invest capture resources?) or a bid decision/bid validation (commit to proposing?)? How long until the proposal would be due?
3. **Customer relationship.** What is the prior relationship with this customer and office? Has the team shaped this requirement, engaged the customer, or responded to an RFI/draft RFP? Is there an incumbent, and is it the user's organization?
4. **Capability and past performance.** Can the organization actually perform this work? Is there recent, relevant, similarly sized past performance? Are required clearances, certifications, facility approvals, or NAICS size standards met?
5. **Competition and price.** Who is likely to bid, and what is the realistic read on competitiveness? Is funding confirmed? Is there a known or estimated budget?
6. **Strategic fit and constraints.** Does this fit the organization's strategy and growth direction? Are there blockers — OCI, a teaming dependency, a missing vehicle, capacity limits, or unacceptable contract terms?

If the user cannot answer a question, record it as a gap. A bid/no-bid built on
guesses is worse than one built on honest unknowns.

## Workflow

Copy this checklist and track progress:

```
Bid/No-Bid Gate Review:
- [ ] Step 1: Complete intake; resolve or record gaps
- [ ] Step 2: Write the opportunity profile (00-opportunity-profile.md)
- [ ] Step 3: Run knockout checks
- [ ] Step 4: Score the weighted criteria
- [ ] Step 5: Estimate pWin honestly
- [ ] Step 6: Form the recommendation
- [ ] Step 7: Write the bid decision (01-bid-decision.md) and validate
```

**Step 1: Intake.** Work the intake questions above. Carry every unknown
forward as an explicit gap; do not paper over it.

**Step 2: Opportunity profile.** Write `00-opportunity-profile.md` capturing
the facts from intake: customer, requirement, contract type and value, period of
performance, set-aside, key dates, incumbent, and known competitors. This is the
shared fact base every later capture skill reads. Use the artifact header from
`pursuit-workspace.md`.

**Step 3: Knockout checks.** Before scoring, run the knockout checks in
`references/bid-no-bid-criteria.md`. A knockout is a condition that makes the bid
unwinnable or non-viable regardless of how attractive it looks — for example, a
set-aside the organization does not qualify for, a mandatory certification it
lacks, an unresolvable OCI, or no relevant past performance where past
performance is a pass/fail gate. **If any knockout is triggered, the
recommendation is no-bid** (or "bid only if this specific condition is
resolved"). Do not let an attractive opportunity override a true knockout.

**Step 4: Score the weighted criteria.** Score each criterion in the six
categories defined in `references/bid-no-bid-criteria.md`, using the 1–5 anchors
given there. For every score, write one line of evidence justifying it. Where
the evidence is an unknown from intake, score conservatively and mark the
confidence as low. Roll the weighted scores into a category and overall result.

**Step 5: Estimate pWin.** Estimate probability of win as a percentage, guided
by `references/bid-no-bid-criteria.md`. Apply the anti-optimism discipline there:
incumbents lose, relationships are not commitments, and "we can do the work" is
not "we will win." State the basis for the number.

**Step 6: Recommendation.** Form one of three recommendations:
- Bid: pursue and propose.
- No-bid: decline; record why so the lesson is reusable.
- Conditional bid: pursue only if specific, named conditions are met by a
  specific date (e.g., "secure a teaming partner with HUBZone status by the
  draft RFP", "confirm funding"). List the conditions and who owns each.

The recommendation must follow from the knockouts, the score, and the pWin — not
from enthusiasm. If they conflict (high score, low pWin), say so and explain.

**Step 7: Write and validate.** Write `01-bid-decision.md` using the template
in `templates/bid-no-bid-scorecard.md`. Then run the validation checklist in
that template: every score has evidence, every unknown is listed as a gap, the
recommendation is consistent with the knockouts and score, and the conditions
(if any) are specific and assigned. Revise until it passes.

## Output

Two artifacts in the pursuit workspace:
- `00-opportunity-profile.md`: the opportunity fact base.
- `01-bid-decision.md`: the scorecard, pWin, recommendation, and rationale.

Present the user with: the recommendation, the overall score and pWin, the top
two or three drivers of the decision, and the most important gaps that, if
closed, would change confidence. Be direct. A bid/no-bid skill that hedges
everything is useless.

## References

- `references/bid-no-bid-criteria.md`: weighted scoring criteria, 1–5 anchors, knockout factors, and pWin estimation guidance.
- `references/gate-reviews.md`: how to adapt the review to each gate, and how a re-run at a later gate should differ.
- `templates/bid-no-bid-scorecard.md`: the scorecard and decision artifact template, with its validation checklist.

## Guardrails

- **Honest unknowns beat confident guesses.** Never invent a customer
  relationship, a competitor read, or funding certainty to fill a blank.
- **Knockouts are not negotiable.** A real disqualifier produces a no-bid (or a
  conditional bid contingent on resolving it), regardless of the score.
- **Resist happy ears.** Capture and BD culture is optimistic by default. This
  skill's job is to be the sober voice. Score to the evidence.
- **This is decision support.** The recommendation informs a human gate
  decision; it does not replace it. Leadership owns the call.
