# Color Team Standards

The three color team reviews — their timing, maturity expectations, lenses, and
how findings are recorded and handed to recovery.

## Contents
- Why staged reviews
- Blue Team
- Pink Team
- Green Team
- Red Team
- Gold Team
- White Glove
- The findings format
- Severity levels
- The recovery handoff
- Other reviews

## Why staged reviews

A proposal is reviewed several times at increasing maturity because the cost of
fixing a problem rises sharply the later it is found. A wrong theme caught at the
Pink Team costs an hour of storyboard rework; the same wrong theme caught at the
Red Team costs a recovery cycle across drafted sections. Each review is matched
to the maturity at which its class of problem is cheapest to fix.

## Blue Team

- **Timing / maturity:** early — the solution and win strategy, before or during
  solutioning and before heavy drafting.
- **Lens:** is this going to be the right offer? The Blue Team reviews the
  *thinking* — the solution and the strategy — not the writing.
- **What it checks:**
  - Is the solution sound, and does it deliver the discriminators the win
    strategy claims?
  - Are the win themes real (valuable, true, provable, rare) and substantiated?
  - Does the approach beat the assessed competition?
  - Is the solution affordable against the price-to-win target?
- **Output:** a readiness assessment and findings that correct the solution and
  the strategy before they are committed to storyboards and drafts.

## Pink Team

- **Timing / maturity:** early — storyboards and an early draft, roughly 30–50%
  complete.
- **Lens:** strategy and structure. The Pink Team is not looking for polished
  prose; it is checking that the proposal is being built right.
- **What it checks:**
  - Does the structure follow Section L?
  - Does every section have a clear theme tied to a customer hot button and a
    Section M factor?
  - Is the compliance approach sound — is every requirement assigned a home and
    on track to be answered?
  - Do the storyboards, read together, tell one coherent, winning story?
  - Are proof points identified for the key claims?
- **Output:** a readiness assessment and findings that redirect the drafting
  before heavy writing begins.

## Green Team

- **Timing / maturity:** the cost/price volume, once a cost model and the
  technical and management volumes exist.
- **Lens:** cost and price. The Green Team reviews the pricing the way the
  government's cost evaluators — and the offeror's own management — will.
- **What it checks:**
  - Is the pricing strategy sound and consistent with the price-to-win posture?
  - Is the basis of estimate sufficient and traced to the technical approach?
  - Is the proposed cost realistic — neither padded nor implausibly low?
  - Is the fee or profit posture appropriate?
  - Is the cost volume consistent with the technical and management volumes (the
    cost-technical consistency check)?
  - Is the cost volume compliant with the Section L cost instructions and the
    Section B CLIN structure?
- **Output:** findings on pricing strategy, basis-of-estimate sufficiency,
  realism, and cost-volume compliance, before the cost volume is finalized.

## Red Team

- **Timing / maturity:** near-final — a complete draft, roughly 90% complete.
- **Lens:** the source-selection evaluator. The Red Team reads the proposal as
  the government will and scores it against Section M. See
  `evaluator-perspective.md`.
- **What it checks:**
  - Compliance — is every requirement met, visibly?
  - Scoring — where are the strengths, weaknesses, significant weaknesses, and
    deficiencies under each Section M factor?
  - Persuasion — are themes and discriminators present and convincing? Would
    this proposal win the tradeoff against the assessed competition?
  - Risk — what would an evaluator flag as performance risk?
- **Output:** a scored evaluation (adjectival ratings, past performance
  confidence, an integrated win/lose read) and a prioritized findings matrix for
  recovery.

The Red Team is the most important review and the one most often run too gently.
A Red Team that does not find the proposal's real weaknesses has simply moved
the discovery to the government's evaluation board, where nothing can be fixed.

## Gold Team

- **Timing / maturity:** final — the proposal is essentially complete, days
  before submission.
- **Lens:** executive readiness and the go/no-go decision.
- **What it checks:**
  - Is the proposal compelling and coherent across all volumes — one voice, one
    story, consistent themes?
  - Are the Red Team findings resolved?
  - Is it compliant and submission-ready?
  - Final executive judgment: submit, or not.
- **Output:** a readiness verdict and any last must-fix items.

## White Glove

- **Timing / maturity:** the final, assembled submission package, after the Gold
  Team and before submission.
- **Lens:** production quality. A meticulous, page-by-page human pass over the
  produced package.
- **What it checks:**
  - Is every volume complete and correctly assembled?
  - Is formatting consistent — headings, numbering, graphics, captions, fonts?
  - Are there production defects — broken cross-references, missing pages,
    misplaced graphics, bad page breaks, low-resolution graphics?
  - Are file names, file formats, and the package structure correct?
- **Relationship to `checking-submission-compliance`:** that skill verifies
  *substantive conformance* against the solicitation's rules — page limits,
  required forms, volume separation. The White Glove review is the *human
  quality pass* over the produced artifact. Run both before submission; they
  catch different things.
- **Output:** a production-defect punch list to fix before the package ships.

## The findings format

Every finding, in every review, is recorded with four parts:

1. **Location** — volume, section, and the compliance-matrix requirement ID(s)
   affected.
2. **Finding** — what is wrong, stated specifically.
3. **Severity** — see below.
4. **Recommended fix** — a specific, actionable correction.

A note missing the location or the fix is not a finding. It cannot be worked in
recovery, so it does not belong in the matrix.

## Severity levels

Aligned to how an evaluator would see the issue (see `evaluator-perspective.md`):

- **Deficiency** — a material failure to meet a requirement; makes the proposal
  unawardable as written. Must be fixed.
- **Significant weakness** — appreciably increases performance risk or loses
  significant evaluation credit. Fix before the next milestone.
- **Weakness** — a flaw that costs credit or adds risk. Fix if time allows.
- **Strength opportunity** — a place the proposal could earn a strength it
  currently does not. Amplify if time allows.
- **Administrative** — format, consistency, typo-level. Fix in production.

## The recovery handoff

A review is only useful if its findings are worked. The recovery handoff:

1. The findings matrix is handed to `running-review-recovery`.
2. That skill triages the findings by severity, assigns each to an owner with a
   due date, drives the fixes (through the drafting and volume skills), and
   verifies each fix against the compliance matrix and Section M.
3. The compliance matrix status is updated as findings close.
4. The next review verifies the prior findings were resolved.

A review without disciplined recovery is theater. The review finds the problems;
`running-review-recovery` is what closes them.

## Other reviews

Review names and the exact set vary by company; this skill covers the six most
common. One related review runs elsewhere in this package: the **Black Hat**, a
capture-phase competitive simulation, is `analyzing-competitors`. Whatever a
given shop calls its reviews, the discipline is constant — a defined lens, a
defined maturity, and actionable, prioritized findings handed to recovery.
