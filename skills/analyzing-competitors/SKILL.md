---
name: analyzing-competitors
description: Produces a Black Hat competitive assessment for a US Federal opportunity. Use when the user needs competitive analysis, a Black Hat review or session, competitor profiling, an incumbent assessment, or wants to understand the competitive field for a federal bid. Identifies likely competitors, models each one's probable solution, price posture, and win themes from the competitor's point of view, and derives counters, ghosting opportunities, and the team's own exposures.
---

# Analyzing Competitors

Run a Black Hat competitive assessment: figure out who else will bid, how each
of them will bid, and what to do about it. The core technique is perspective —
stop thinking about the team's own proposal and instead bid the job *as each
competitor would*. A competitive assessment that only lists competitors and
their revenue is a directory. A Black Hat predicts their offers.

## When to use this skill

Use this skill during capture, once an opportunity is being pursued, to assess
the competitive field. It supports the bid/no-bid decision, the price-to-win
analysis, and (most importantly) the win strategy, which needs to know what
it is differentiating *against*.

Re-run it as intelligence improves, especially after a draft RFP clarifies scope
and after customer engagement sharpens the read on the incumbent.

This skill does not set the team's win themes (`developing-win-strategy`) or
estimate the price target (`estimating-price-to-win`) — but both depend on it,
so run this first.

## Inputs

**Preferred upstream artifacts:**
- `00-opportunity-profile.md`: the opportunity facts, including any known
  incumbent and competitors.
- `02-capture-plan.md`: customer intelligence that informs how competitors are
  positioned with this customer.

**Without them**, run the intake below.

Read `../../shared/glossary.md` and `../../shared/pursuit-workspace.md` if not
already read this session. Read `references/competitive-intelligence-ethics.md`
before gathering any competitor information.

## Intake

Ask these as a numbered list. Skip what upstream artifacts answer.

1. **The opportunity.** What is the requirement, customer, contract type,
   estimated value, set-aside, and vehicle? (Set-aside and vehicle bound the
   field — only qualifying firms can bid.)
2. **Known and suspected bidders.** Who does the team already believe will bid?
   Is there an incumbent, and who is it?
3. **What is known about each competitor.** For each likely bidder, what does
   the team know — size, relevant past performance, customer relationship,
   typical technical approach, typical price posture, recent wins and losses?
4. **The incumbent's standing.** If there is an incumbent the team is not, how
   is the customer's relationship with it — strong, strained, fatigued? Any
   known performance problems?
5. **The team's own position.** Briefly — where does the team believe it is
   strong and weak relative to this field? (Used to assess exposure, not to set
   strategy.)
6. **Information sources.** What public or properly obtained sources are
   available — past award data, published past performance, market research,
   prior debriefs? (See the ethics reference for what is in bounds.)

Where the team does not know something about a competitor, that is an
intelligence gap. Record it; do not invent the answer.

## Workflow

```
Black Hat Competitive Assessment:
- [ ] Step 1: Read upstream artifacts; complete intake; review CI ethics
- [ ] Step 2: Confirm the competitive field
- [ ] Step 3: Profile each competitor
- [ ] Step 4: Bid the job as each competitor (the Black Hat)
- [ ] Step 5: Build the comparison and most-probable-winner read
- [ ] Step 6: Derive counters, ghosting opportunities, and our exposures
- [ ] Step 7: Write the assessment (03-competitive-assessment.md) and validate
```

**Step 1: Read, intake, ethics.** Read upstream artifacts and the CI ethics
reference. Use only properly sourced information throughout.

**Step 2: Confirm the field.** List the credible bidders. The set-aside and
vehicle constrain it — only qualifying firms can bid. Distinguish *likely*
bidders from *possible* ones, and treat the incumbent as its own case.

**Step 3: Profile each competitor.** Using
`references/black-hat-method.md`, profile each: size and qualifications,
relevant past performance, customer relationship and incumbency, typical
technical approach, typical price posture, and recent relevant wins and losses.
Mark each item known or assessed.

**Step 4: Bid the job as each competitor.** The Black Hat itself. For each
competitor, switch perspective and answer as them: *How would we bid this? What
solution would we propose? What are our win themes? Where are we strong, and
where are we vulnerable? What price posture would we take?* Be genuinely
adversarial — give each competitor their best plausible bid, not a strawman.

**Step 5: Comparison and most-probable winner.** Build the comparison matrix
from `black-hat-method.md`, scoring each competitor (and the team) across the
factors the customer will evaluate. Then state who is most likely to win today
and why — including, honestly, the cases where it is not the team.

**Step 6: Counters, ghosts, and exposures.** Derive three things:
- Counters: for each competitor's likely strengths and themes, how the
  team's proposal should respond.
- Ghosting opportunities: competitor weaknesses the team's proposal can
  highlight by contrast, without naming the competitor (see the method file for
  how to ghost legitimately).
- Our exposures: the team's own weaknesses that competitors will ghost.
  Each exposure is something the win strategy must address.

**Step 7: Write and validate.** Write `03-competitive-assessment.md` using
`templates/competitive-assessment.md`. Run its validation checklist: every
competitor is bid as themselves (not strawmanned), every claim is sourced or
marked assessed, ghosting opportunities are real and legitimately framed, and
the team's own exposures are listed as honestly as the competitors'.

## Output

One artifact: `03-competitive-assessment.md` in the pursuit workspace.

Present the user with: the likely field, the most-probable winner and why, the
two or three strongest ghosting opportunities, the team's most dangerous
exposures, and the biggest intelligence gaps.

## References

- `references/black-hat-method.md`: competitor profiling dimensions, the "bid as them" technique, the comparison matrix, and how to ghost legitimately.
- `references/competitive-intelligence-ethics.md`: which competitor information may and may not be gathered and used.
- `templates/competitive-assessment.md`: the assessment artifact template and its validation checklist.

## Guardrails

- **Properly sourced information only.** Use public and legitimately obtained
  information. Never use, seek, or speculate from a competitor's proprietary
  information or any source-selection-sensitive material. See the ethics file.
- **No strawmen.** Give each competitor their strongest plausible bid. A Black
  Hat that makes competitors look weak produces dangerous overconfidence.
- **Mark assessed vs. known.** A predicted competitor approach is an assessment.
  Label it. Do not state predictions as fact.
- **Be as honest about us as about them.** The team's exposures must be listed
  with the same candor as competitors' weaknesses.
- **Predictions, not certainties.** This is a structured forecast to inform
  strategy, not intelligence about what competitors will actually do.
