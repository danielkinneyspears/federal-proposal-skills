---
name: reviewing-color-teams
description: Runs proposal color team reviews for a US Federal bid — Blue, Pink, Green, Red, Gold, and White Glove. Use when the user needs a color team review; a Blue, Pink, Green, Red, Gold, or White Glove (book check) review; a proposal or cost-volume review; an evaluator-perspective assessment; a mock evaluation; or a proposal scored before submission. The Red Team scores the proposal as a source-selection evaluator would, against Section M, identifying strengths, weaknesses, significant weaknesses, and deficiencies; every review produces prioritized, actionable findings for recovery.
---

# Reviewing Color Teams

Run a proposal review the way a federal source-selection evaluator would. Color
team reviews catch problems while they are still cheap to fix. Their value
depends entirely on one thing: producing findings that are scored, prioritized,
and specific enough to act on. A review that returns vague impressions wastes
the most expensive afternoon in the proposal schedule. This skill runs the
review against an explicit standard and produces a findings matrix the team can
work in recovery.

## When to use this skill

Use this skill to run any of the proposal color team reviews:

- Blue Team: early, on the solution and win strategy, before or during solutioning.
- Pink Team: on storyboards and an early draft (~30–50%).
- Green Team: on the cost/price volume and the pricing strategy.
- Red Team: near-final (~90%), scoring as the government evaluator would.
- Gold Team: final, executive go/no-go before submission.
- White Glove: final production / book check of the assembled package.

Determine which review fits the work and its maturity (the skill's intake does
this). This skill reviews; it does not fix. The fixes are recovery work, run by
`running-review-recovery` with the drafting skills.

## Inputs

**Required:**
- The proposal content to review — storyboards (`11-proposal-outline.md`) for a
  Pink Team; drafted sections (`12-sections/` and the volume artifacts) for Red
  and Gold.
- `10-compliance-matrix.md`: the requirements the proposal is checked against.
- The solicitation Sections L and M — the evaluation standard.

**Preferred upstream artifacts:**
- `05-win-strategy.md`: to assess whether themes and discriminators landed.

**Without Section M**, a Red Team cannot score properly — Section M *is* the
scoresheet. Obtain it before running a Red Team.

Read `../../shared/glossary.md`, `../../shared/proposal-lifecycle.md`, and
`../../shared/pursuit-workspace.md` if not already read this session.

## Intake

Ask these as a numbered list.

1. **Which review.** Which color team — Blue, Pink, Green, Red, Gold, or White
   Glove? If unsure, describe what is being reviewed and its maturity:
   solution/win strategy → Blue; storyboards and early draft → Pink; the cost
   volume → Green; a near-final full draft → Red; the final proposal → Gold; the
   assembled submission package → White Glove.
2. **Scope.** The whole proposal or specific volumes/sections? Which artifacts
   are available to review?
3. **The standard.** Are Section L, Section M, and the compliance matrix
   available? For a Red Team, what are the Section M factors, subfactors, their
   relative importance, and the evaluation approach (tradeoff or LPTA)?
4. **Win strategy.** Is `05-win-strategy.md` available, so the review can check
   whether the themes and discriminators are present and persuasive?
5. **Recovery time.** How much time remains before the next milestone or
   submission? (This shapes how findings are prioritized.)

## Workflow

```
Color Team Review:
- [ ] Step 1: Confirm the review type and load the standard
- [ ] Step 2: Run the review for that team's lens
- [ ] Step 3: Record each finding with location, severity, and a fix
- [ ] Step 4: Score (Red Team: rate against Section M)
- [ ] Step 5: Prioritize findings for recovery
- [ ] Step 6: Write the review (20-color-review-<team>.md)
```

**Step 1: Review type and standard.** Confirm which review this is. Load the
applicable standard from `references/color-team-standards.md` (the lens and
maturity expectation for that team) and, for a Red Team,
`references/evaluator-perspective.md` (how to score as a source-selection
evaluator).

**Step 2: Run the review.** Review every in-scope piece of the work through
that team's lens:
- Blue Team: solution and win strategy. Is the solution sound and does it
  deliver the discriminators? Are the win themes real and substantiated? This
  review happens before heavy drafting, while the approach can still change.
- Pink Team: strategy and structure. Do the storyboards and early draft
  follow Section L? Is each section's theme present and tied to a hot button and
  a Section M factor? Is the compliance approach sound? Is the proposal on the
  right track *before* heavy drafting?
- Green Team: cost and price. Is the pricing strategy sound? Is the basis
  of estimate sufficient? Is the cost realistic and consistent with the
  technical and management volumes? Is the cost volume compliant with Section L?
- Red Team: the evaluator's view. Read each section as the government
  evaluator who scores it. Is every requirement compliant? Where are the
  strengths, weaknesses, significant weaknesses, and deficiencies? Would this
  win the tradeoff?
- Gold Team: executive readiness. Is it compelling, coherent across volumes,
  compliant, and ready to submit? Go or no-go?
- White Glove: production / book check. Is the assembled package complete,
  consistently formatted, correctly produced, and free of production defects?
  (Substantive conformance is `checking-submission-compliance`'s job; the White
  Glove review is the human quality pass over the produced package.)

**Step 3: Record findings.** Every finding is recorded with: its exact location
(volume, section, requirement ID); what is wrong; its severity; and a specific
recommended fix. A finding without a location and a fix is an opinion, not a
finding — do not record it that way.

**Step 4: Score.** For a Red Team, assign ratings as an evaluator would, using
`evaluator-perspective.md`: rate each Section M factor (adjectival rating and
the strengths/weaknesses behind it), assess past performance confidence, and
give an integrated read of whether the proposal wins. Reviews other than the Red
Team give a readiness assessment rather than a formal score, but still state
plainly whether the work is on track.

**Step 5: Prioritize.** Sort findings for recovery: deficiencies and
significant weaknesses first (a deficiency makes the proposal unawardable until
fixed), then weaknesses, then strengths to amplify, then minor issues. Given the
recovery time available, mark which findings *must* be fixed before the next
milestone.

**Step 6: Write.** Write `20-color-review-<team>.md` (e.g.,
`20-color-review-red.md`) using `templates/color-review.md`.

## Output

One artifact per review: `20-color-review-<team>.md` in the pursuit workspace.

Present the user with: the overall assessment (for a Red Team, the scored
verdict), the deficiencies and significant weaknesses that must be fixed, the
prioritized recovery list, and (honestly) whether the proposal is on track.

## References

- `references/color-team-standards.md`: the six reviews, their maturity expectations and lenses, the findings format, and the recovery handoff.
- `references/evaluator-perspective.md`: scoring as a source-selection evaluator: the definitions of strength, weakness, significant weakness, and deficiency; adjectival ratings; past performance confidence; and scoring against Section M.
- `templates/color-review.md`: the color review artifact template and findings matrix.

## Guardrails

- **Findings must be actionable.** Every finding has a location, a severity, and
  a specific fix. Vague comments ("strengthen this section") are not findings.
- **Score against Section M, not taste.** A Red Team rates the proposal against
  the solicitation's stated evaluation criteria — not against what the reviewer
  personally would prefer.
- **Be the adversary.** A Red Team that is gentle is worthless. Find the
  weaknesses and deficiencies now, while the team can still fix them, because
  the government's evaluator will not be gentle.
- **Do not rewrite.** This skill reviews and prescribes fixes. The fixes are
  recovery work for the drafting skills. A reviewer who rewrites stops reviewing.
- **Honest verdict.** If the proposal is not on track, say so plainly. A review
  that softens a bad verdict denies the team the chance to recover.
