# The Federal Capture and Proposal Lifecycle

This package mirrors the gated business-development lifecycle that most federal
contractors run — the model commonly called the *Shipley* process. This file
explains the phases, the gate and color reviews, and how the sixteen skills map
onto them. Skills reference this file so they share one mental model.

## Contents
- The core idea: a gated pipeline
- Phase 1 — Capture (pre-RFP)
- Phase 2 — Proposal development
- Phase 3 — Review and submission
- Phase 4 — Post-submission
- Gate reviews
- Color team reviews
- Skill-to-phase map

## The core idea: a gated pipeline

Federal opportunities move through a pipeline. At each gate, leadership decides
whether to keep spending money (bid-and-proposal cost) on the pursuit. Work is
not thrown away between stages: each phase produces artifacts that the next
phase consumes. Positioning learned during capture becomes the win themes in the
proposal; the competitive assessment becomes the price-to-win target; the
solicitation shred becomes the compliance matrix that governs every section.

A proposal that is merely *compliant* — it answers every requirement — still
loses to a proposal that is compliant *and* responsive to what the customer
actually cares about *and* better than the competition on the factors that
decide the award. The lifecycle exists to produce the second kind.

## Phase 1 — Capture (pre-RFP)

Capture is everything done before the RFP drops to improve the probability of
win. It is where wins are actually decided; the proposal mostly documents a
position already won or lost.

Capture work: identify and qualify the opportunity; understand the customer,
the requirement, and the budget; assess competitors; shape the requirement
through RFI/DRFP responses and customer engagement; decide the win strategy;
form the team. Capture answers: *Should we bid this? Can we win it? How?*

## Phase 2 — Proposal development

When the RFP releases, the proposal phase converts the win strategy into a
compliant, responsive, compelling document. Work: design the solution; stand the
proposal up as a managed project (schedule, assignments, question and amendment
control); shred the solicitation into a compliance matrix; build a Section
L-compliant annotated outline; storyboard each section around themes and proof
points; draft narrative; write the executive summary, past performance, key
personnel, and cost volumes.

The discipline of this phase: nothing is drafted that is not traceable to a
requirement, and nothing that addresses a requirement is left undrafted.

## Phase 3 — Review and submission

Color team reviews (below) catch problems while they are still cheap to fix,
and each review's findings are then worked in disciplined recovery.
The final stage is a production and submission-compliance check: page counts,
format rules, required forms and certifications, file naming, and the mechanics
of the submission portal. Many strong proposals are rejected on a format
technicality; this phase exists to prevent that.

## Phase 4 — Post-submission

After submission: prepare for oral presentations if the solicitation requires
them, then — win or lose — request and analyze the government debrief and
capture lessons learned that feed the next bid/no-bid decision. The pipeline is
a loop, not a line.

## Gate reviews

Gate reviews are leadership decision points. Names and numbering vary by
company; the decisions are consistent. A common set:

| Gate | Decision | Typical timing |
|---|---|---|
| Opportunity identification | Is this real enough to track? | Lead enters pipeline |
| Pursuit decision | Do we invest capture resources? | Well before RFP |
| Preliminary bid decision | Do we intend to bid? Validate pWin and price-to-win. | DRFP / ~RFP release |
| Bid validation | Given the actual RFP, do we still bid? | Just after RFP release |
| Proposal submission | Is the proposal ready to send? | Gold Team / submission |

The `qualifying-opportunities` skill runs the bid/no-bid gate reviews; the
`planning-capture` skill maintains the capture plan that feeds them.

## Color team reviews

Color teams are staged proposal reviews. Each looks at the proposal through a
different lens at a different maturity. The `reviewing-color-teams` skill runs
all of them.

| Review | Maturity reviewed | Lens |
|---|---|---|
| **Blue Team** | Solution / win strategy | Is this going to be the right offer? Reviews the solution and the win themes before heavy drafting. |
| **Pink Team** | ~30–50% draft | Strategy, structure, compliance approach, theme presence. Are the storyboards and early drafts on the right track? |
| **Green Team** | Cost volume | Pricing strategy, basis-of-estimate sufficiency, cost realism, cost-technical consistency, cost-volume compliance. |
| **Red Team** | ~90% draft | The source-selection evaluator's view. Score it against Section M. Find weaknesses and deficiencies before the government does. |
| **Gold Team** | Final | Executive review. Is it compelling, compliant, and ready? Final go/no-go. |
| **White Glove** | Assembled package | Production quality — a page-by-page human pass over the produced submission package. |

The `reviewing-color-teams` skill runs all six. One related review runs in
capture: the **Black Hat** competitive simulation, run by `analyzing-competitors`.

A color team review is only useful if it produces actionable findings and those
findings are worked in *recovery* before the next milestone. The
`running-review-recovery` skill owns that work — it assigns, drives, and verifies
the closure of every finding. A review whose findings are not recovered, and a
review that produces only vague comments, both waste the most expensive people
in the building.

## Skill-to-phase map

```
PHASE 1 — CAPTURE
  qualifying-opportunities ─────► 00-opportunity-profile.md, 01-bid-decision.md
  planning-capture ─────────────► 02-capture-plan.md
  analyzing-competitors ────────► 03-competitive-assessment.md
  estimating-price-to-win ──────► 04-price-to-win.md
  developing-win-strategy ──────► 05-win-strategy.md
  responding-to-rfis ───────────► 06-shaping-response-<type>.md
  developing-teaming-strategy ──► 07-teaming-strategy.md

PHASE 2 — PROPOSAL DEVELOPMENT
  developing-solution-approach ─► 08-solution-design.md
  managing-proposal-operations ─► 09-proposal-management/
  shredding-solicitations ──────► 10-compliance-matrix.md
  outlining-proposals ──────────► 11-proposal-outline.md
  drafting-proposal-sections ───► 12-sections/
  writing-executive-summaries ──► 13-executive-summary.md
  writing-past-performance ─────► 14-past-performance/
  developing-key-personnel ─────► 15-key-personnel/
  narrating-cost-volumes ───────► 16-cost-narrative.md

PHASE 3 — REVIEW AND SUBMISSION
  reviewing-color-teams ────────► 20-color-review-<team>.md
  running-review-recovery ──────► 23-review-recovery.md
  checking-submission-compliance ► 21-submission-checklist.md

PHASE 4 — POST-SUBMISSION
  preparing-orals ──────────────► 22-orals-package.md
  analyzing-debriefs ───────────► 30-debrief-analysis.md
```

Skills are independent and can be invoked alone. When run in sequence they form
the pipeline above, each reading upstream artifacts from the pursuit workspace.
`managing-proposal-operations` and `running-review-recovery` are coordinating
skills — they run alongside the development and review skills rather than as a
single pipeline stage. Solutioning (`developing-solution-approach`) and proposal
kickoff (`managing-proposal-operations`) straddle the capture-to-proposal
boundary; their artifact numbers (08, 09) sit just before the compliance matrix
even though both iterate with it.
