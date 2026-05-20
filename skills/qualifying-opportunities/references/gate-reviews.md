# Adapting the Review to the Gate

The bid/no-bid decision is not made once. It is made repeatedly, at successive
gates, as the opportunity matures and uncertainty falls. The same scoring model
applies at every gate; what changes is the available evidence, the confidence,
and the cost of being wrong. This file tells the skill how to adapt.

## Contents
- The gates
- What changes between gates
- Re-running the review at a later gate
- Conditional bids across gates

## The gates

| Gate | Question | Evidence available |
|---|---|---|
| Pursuit decision | Should we invest capture resources before the RFP? | Market intelligence, customer knowledge, an RFI or sources-sought notice. Little competitive or price data. |
| Preliminary bid decision | Do we intend to bid? | A draft RFP or imminent RFP. Capture plan in progress. Early competitive and price-to-win reads. |
| Bid validation | Given the *actual* released RFP, do we still bid? | The final RFP, Section L and M, amendments. Competitive assessment and price-to-win should exist. |

Smaller or faster acquisitions (task orders under FAR 16.505) may collapse these
into a single decision. Larger pursuits run all three and sometimes more.

## What changes between gates

- **Confidence rises.** At the pursuit gate, most scores carry low confidence
  and many intake answers are unknowns. By bid validation, the RFP has removed
  much of the uncertainty. Report confidence honestly at every gate; an early
  gate dominated by unknowns is normal and not a reason to inflate scores.
- **Knockouts get sharper.** Early, a knockout may be "uncertain" (set-aside not
  yet announced, funding not confirmed). At bid validation, the RFP resolves
  most of them to a firm yes or no.
- **The cost of a wrong yes rises.** Saying "pursue" at the pursuit gate commits
  modest capture cost. Saying "bid" at bid validation commits the full
  bid-and-proposal cost. Later gates demand more evidence for a bid.
- **Section L and M become available.** Only at and after RFP release can the
  review test executability against the real instructions, page limits,
  schedule, and evaluation factors. The schedule-feasibility and
  terms-executability criteria become evidence-based rather than estimated.

## Re-running the review at a later gate

When this skill runs on an opportunity that already has a `01-bid-decision.md`
from an earlier gate:

1. **Do not start from scratch.** Read the prior decision. Note its gate, score,
   pWin, recommendation, and the gaps and conditions it recorded.
2. **Focus intake on what changed.** Has the RFP released? Were prior unknowns
   resolved? Did competitive or price-to-win analysis arrive? Were conditional-bid
   conditions met?
3. **Re-score only what moved**, but re-roll the full result so it is current.
4. **Compare explicitly.** In the new `01-bid-decision.md`, show the prior and
   current score, pWin, and recommendation side by side, and explain the delta.
   A decision that flipped from bid to no-bid (or the reverse) must say why.
5. **Resolve open conditions.** Every condition from the prior gate is now met,
   not met, or still open. State which.

A later-gate review that simply repeats the earlier one has added nothing. Its
value is the comparison.

## Conditional bids across gates

A conditional bid is a deliberate "decide later" with named conditions and
owners. It is appropriate when an opportunity is attractive but hinges on
specific, resolvable uncertainty.

- Each condition must be **specific** (not "improve our position"), **assigned**
  to an owner, and **dated** to a gate or calendar date.
- The next gate review's job includes closing every open condition. A condition
  that is still open at the final bid-validation gate, with no path to
  resolution, converts to a no-bid.
- Do not use "conditional bid" to avoid a hard call. If the evidence supports a
  no-bid, recommend no-bid.
