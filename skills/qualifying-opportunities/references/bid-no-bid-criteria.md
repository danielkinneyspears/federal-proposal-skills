# Bid/No-Bid Criteria

The knockout checks, the weighted scoring model, and pWin estimation guidance
for the `qualifying-opportunities` skill.

## Contents
- How to use this file
- Knockout checks (run first)
- The weighted scoring model
- Category 1 — Customer and relationship
- Category 2 — Opportunity fit and strategic alignment
- Category 3 — Competitive position
- Category 4 — Solution and delivery capability
- Category 5 — Financial and business
- Category 6 — Risk and executability
- Rolling up the score
- pWin estimation
- Reading the result

## How to use this file

1. Run every knockout check. A triggered knockout drives the recommendation
   regardless of score.
2. Score each criterion 1–5 against the anchors below. Every score needs one
   line of evidence. If the evidence is an unknown, score conservatively (toward
   3 or below) and mark confidence low.
3. Average criteria within a category, then apply category weights for the
   overall score.
4. Estimate pWin separately using the guidance at the end.

The 1–5 scale throughout: **1** strongly unfavorable / **2** unfavorable /
**3** neutral or genuinely uncertain / **4** favorable / **5** strongly
favorable.

## Knockout checks (run first)

A knockout is a condition that makes the opportunity unwinnable or non-viable on
its face. For each, the answer is yes/no/uncertain. Any **yes** drives a no-bid.
An **uncertain** on a knockout becomes a condition in a conditional-bid
recommendation — it must be resolved before real money is spent.

- **Set-aside ineligibility.** The acquisition is set aside for a category
  (small business, 8(a), SDVOSB, WOSB, HUBZone) the organization does not
  qualify for and cannot legitimately qualify for as the prime.
- **Size standard.** The organization exceeds the NAICS small-business size
  standard for a small-business acquisition.
- **Missing mandatory qualification.** A required certification, security
  clearance (facility or personnel), facility approval, or accreditation is not
  held and cannot be obtained before performance must begin.
- **No contract vehicle.** The work is a task order under an IDIQ/GWAC the
  organization does not hold and cannot join.
- **Fatal past-performance gap.** Past performance is evaluated pass/fail (or
  effectively gating) and the organization has no recent, relevant past
  performance, and cannot obtain it through a teaming partner.
- **Unresolvable OCI.** An organizational conflict of interest exists that
  cannot be mitigated or waived.
- **Funding is not real.** There is no identified budget or appropriation; the
  "opportunity" is an unfunded wish list or pure market research with no award.
- **No time to comply.** The remaining schedule is too short to produce a
  compliant proposal of the required quality.
- **Categorically unacceptable terms.** The solicitation imposes terms
  leadership has ruled out (e.g., unlimited liability, unacceptable IP terms).
- **Strategic veto.** The work conflicts with the organization's strategy or
  relationships severely enough that leadership will not staff or fund it.

## The weighted scoring model

Six categories, weighted to 100%:

| # | Category | Weight |
|---|---|---|
| 1 | Customer and relationship | 20% |
| 2 | Opportunity fit and strategic alignment | 15% |
| 3 | Competitive position | 20% |
| 4 | Solution and delivery capability | 15% |
| 5 | Financial and business | 20% |
| 6 | Risk and executability | 10% |

Weights are a sensible default. A specific organization may tune them (a
relationship-driven shop may weight Category 1 higher). If the user states
different weights, use theirs and record it.

## Category 1 — Customer and relationship

- **Customer knowledge and access.** Does the team know the customer's mission,
  the program office, the key decision-makers, and have current access?
  *1:* no relationship or access. *3:* known agency, no access to this office.
  *5:* deep, current relationships with the program office and decision-makers.
- **Requirement shaping.** Has the team influenced the requirement, the
  acquisition strategy, or Section M — through RFI responses, draft-RFP comments,
  white papers, or customer engagement?
  *1:* no engagement; first awareness was the solicitation. *3:* responded to an
  RFI with no evidence of influence. *5:* documented influence on scope or
  evaluation criteria.
- **Incumbency and relationship strength.** Is the organization the incumbent,
  and is the customer relationship healthy?
  *1:* a competitor is an entrenched, well-rated incumbent. *3:* new requirement,
  no incumbent. *5:* the organization is the incumbent with strong CPARS and a
  customer that wants continuity.

## Category 2 — Opportunity fit and strategic alignment

- **Strategic fit.** Does this advance the organization's deliberate growth
  strategy — target customer, market, or capability?
  *1:* off-strategy; a distraction. *3:* adjacent. *5:* squarely on a named
  strategic priority.
- **Capability match to scope.** How much of the scope does the organization
  perform today as core work?
  *1:* mostly outside current capability. *3:* significant portions require new
  capability or heavy teaming. *5:* core, demonstrated capability across the scope.
- **Qualification fit.** Do the NAICS code, set-aside type, and vehicle align
  cleanly with the organization's status and holdings? (A hard misfit is a
  knockout; this criterion captures soft friction.)
  *1:* awkward fit requiring workarounds. *3:* workable. *5:* clean alignment.

## Category 3 — Competitive position

- **Competitive landscape.** How crowded and how strong is the likely field?
  *1:* many strong bidders, including the relationship/incumbent favorite.
  *3:* a normal competitive field. *5:* few credible bidders; weak field.
- **Differentiation.** Does the organization have real discriminators — capabilities
  valued by this customer that competitors cannot easily match? (A discriminator
  is only real if it is both valued and rare; see `developing-win-strategy`.)
  *1:* nothing that distinguishes the offer; competing on price alone.
  *3:* some strengths, none clearly unique. *5:* clear, customer-valued discriminators.
- **Incumbent strength (when the incumbent is a competitor).** How strong is the
  incumbent's position?
  *1:* strong incumbent, happy customer, no openings. *3:* incumbent with known
  performance problems or customer fatigue. *5:* no incumbent, or a weak/displaced one.
  Score 3 (neutral) if there is no incumbent.

## Category 4 — Solution and delivery capability

- **Solution maturity.** How ready is the technical solution and approach?
  *1:* would have to invent the approach. *3:* a credible approach exists but is
  unproven for this customer. *5:* a mature, proven solution ready to tailor.
- **Staffing and key personnel.** Can the organization field — recruit, commit,
  and retain — the required staff, especially named key personnel and any
  required clearances?
  *1:* cannot realistically staff it. *3:* staffable with effort and risk.
  *5:* people identified and committable now.
- **Past performance.** Is there recent, relevant, similarly sized past
  performance with strong ratings? (A fatal absence is a knockout; this captures
  degree.)
  *1:* thin or dated past performance. *3:* relevant but smaller-scale or mixed
  ratings. *5:* directly relevant, recent, well-rated work.

## Category 5 — Financial and business

- **Value and margin.** Is the contract value and expected margin attractive
  relative to the effort?
  *1:* low value or thin margin not worth the B&P investment. *3:* acceptable.
  *5:* high value with healthy margin.
- **Funding certainty.** How certain is the funding? (No funding at all is a
  knockout; this captures degree of certainty.)
  *1:* funding uncertain or subject to likely cuts. *3:* expected but not
  confirmed. *5:* confirmed and appropriated.
- **B&P cost vs. expected value.** Is the cost to pursue and propose proportionate
  to the opportunity, given pWin?
  *1:* expensive pursuit, low pWin — poor expected return. *3:* proportionate.
  *5:* modest pursuit cost relative to a strong expected return.
- **Contract type risk.** Does the contract type (FFP, T&M, cost-reimbursement)
  put acceptable risk on the organization given its cost maturity?
  *1:* a contract type that exposes the organization to unacceptable risk.
  *3:* manageable. *5:* well-matched to the organization's risk posture and systems.

## Category 6 — Risk and executability

- **OCI and compliance risk.** Beyond a knockout-level conflict, is there
  residual OCI, compliance, or accounting-system risk?
  *1:* significant residual risk. *3:* minor, mitigable. *5:* none identified.
- **Teaming dependency.** How dependent is the bid on partners the organization
  does not control?
  *1:* the win depends on a partner not yet secured. *3:* teaming needed and
  feasible. *5:* the organization can win as a standalone prime, or partners are locked.
- **Schedule feasibility.** Is there enough time and capacity to produce a
  winning — not merely compliant — proposal?
  *1:* too compressed for quality. *3:* tight but feasible. *5:* comfortable runway.
- **Terms and executability.** Are the solicitation's terms, deliverables, and
  performance constraints executable without heroics?
  *1:* terms create serious execution risk. *3:* normal. *5:* clean and executable.

## Rolling up the score

1. Within each category, average the criterion scores (1–5).
2. Multiply each category average by its weight; sum for the overall score (1–5).
3. Report the overall score, every category average, and the lowest-scoring
   individual criteria — those are the decision drivers and the things to fix.

Score is one input. Knockouts and pWin can override it. A 4.2 overall with a
12% pWin is still likely a no-bid; say so.

## pWin estimation

Estimate probability of win as a percentage. It is a judgment, but a disciplined
one. Build it, do not feel it:

1. **Start from a base rate.** With *N* credible bidders and no other
   information, the naive base rate is 1/*N*. Five credible bidders → start near
   20%.
2. **Adjust for position.** Move up for genuine customer relationship,
   documented requirement shaping, real discriminators, and a price-to-win the
   organization can hit. Move down for a strong incumbent competitor, a
   commodity offer, or a price the organization cannot reach.
3. **Apply anti-optimism discipline:**
   - Being the incumbent helps but does not guarantee a win; incumbents lose
     regularly, especially after performance problems or a price reset.
   - A relationship is not a commitment. Government evaluators are bound to the
     stated evaluation criteria.
   - "We can do the work" is a threshold, not an advantage. Most bidders can do
     the work.
   - If you cannot name a concrete reason this offer beats the field, pWin is
     low — regardless of how capable the organization is.
4. **State the basis.** Write the one or two factors that most drive the number
   up or down.

A pWin below roughly 25–30% on a costly pursuit usually argues for no-bid unless
the strategic value is exceptional and explicitly stated.

## Reading the result

Translate the score, knockouts, and pWin into the recommendation:

- **No-bid** — any knockout triggered; or a low score; or a pWin too low to
  justify the B&P investment.
- **Conditional bid** — the opportunity is attractive but hinges on resolving
  specific uncertainties (an unconfirmed knockout, a teaming gap, unconfirmed
  funding, a price-to-win not yet validated). Name each condition, assign an
  owner, and set a date.
- **Bid** — no knockouts, a solid score, and a pWin that justifies the
  investment.

Always surface the gaps that most constrained confidence. Closing those gaps,
not re-running the math, is what changes a marginal decision.
