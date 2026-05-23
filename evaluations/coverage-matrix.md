# Evaluation Coverage Matrix

This matrix summarizes the current evaluation coverage across all 21 skills.
It is an index over the existing evaluation files, not a claim that every
scenario has passed in a particular model run.

Use [`run-evals.md`](run-evals.md) to run scenarios and record pass/fail
results.

## Current Baseline

- All 21 skills have evaluation files.
- 20 skills have 3 evaluation scenarios.
- `reviewing-color-teams` has 4 evaluation scenarios.
- All skill evaluation files use expected-behavior and anti-behavior sections.
- The repo has two synthetic fixtures:
  - `fixtures/synthetic-rfp.md`
  - `fixtures/synthetic-proposal-section.md`
- `run-evals.md` defines the manual run process and result record template.

## Matrix

| Skill | Scenario count | Fixture use | Output / artifact coverage | Validation coverage | Anti-behavior coverage |
|---|---:|---|---|---|---|
| `qualifying-opportunities` | 3 | Scenario-supplied inputs | Opportunity profile, bid decision, re-run behavior | Knockouts, honest unknowns, prior-artifact continuity | Does not override knockouts, invent facts, or ignore prior decisions |
| `planning-capture` | 3 | Scenario-supplied inputs | Living capture plan, action items, change log updates | Intelligence gaps, rules-safe customer engagement, living-plan update behavior | Does not re-ask answered questions, suggest improper shaping, or silently overwrite |
| `analyzing-competitors` | 3 | Scenario-supplied inputs | Competitive assessment, most-probable-winner read, competitor modeling | Perspective-taking, information ethics, honest winner assessment | Does not use questionable information, strawman competitors, or force optimism |
| `estimating-price-to-win` | 3 | Scenario-supplied inputs | Price-to-win range, pricing posture, unbridgeable-gap report | Distinguishes PTW from cost estimate, adapts to evaluation type, flags nonviable economics | Does not invent cost figures or hide a bid/no-bid problem |
| `developing-win-strategy` | 3 | Scenario-supplied inputs | Win themes, discriminator validation, exposure responses | Validates discriminators, links benefit and proof, addresses exposures | Does not treat table stakes as discriminators or ignore weaknesses |
| `responding-to-rfis` | 3 | Scenario-supplied inputs | Sources-sought response, draft-RFP comments, shaping response artifact | Shaping objective, legitimate comment framing, integrity limits | Does not overclaim, lobby improperly, or use restricted information |
| `developing-teaming-strategy` | 3 | Scenario-supplied inputs | Teaming strategy, partner gap analysis, data-call inputs | Real gap coverage, OCI screening, schedule/data-call integration | Does not ignore OCI, clear OCI itself, or recommend partners without fit |
| `developing-solution-approach` | 3 | Scenario-supplied inputs | Solution design artifact | Requirement/theme/cost alignment, discriminator feasibility, design-to-cost | Does not design outside constraints or preserve unsupported discriminators |
| `managing-proposal-operations` | 3 | Scenario-supplied inputs | `09-proposal-management/` artifact set, RACI, amendment updates | Backward scheduling, ownership assignment, amendment impact merge behavior | Does not leave sections ownerless or ignore amendment blast radius |
| `shredding-solicitations` | 3 | `synthetic-rfp.md` | `10-compliance-matrix.md`, requirements/register content | Atomic requirements, L/M conflict handling, incomplete-document handling | Does not resolve solicitation conflicts itself or invent missing content |
| `outlining-proposals` | 3 | `synthetic-rfp.md` | `11-proposal-outline.md`, storyboards, page budget | Section L structure, storyboard-before-draft discipline, page budget checks | Does not skip planning or hide overflow |
| `drafting-proposal-sections` | 3 | `synthetic-proposal-section.md` plus scenario inputs | Section draft artifacts | Storyboard traceability, missing-proof handling, evaluation-type fit | Does not invent proof or over-sell LPTA sections |
| `writing-executive-summaries` | 3 | Scenario-supplied inputs | Executive summary artifact | Persuasion over recap, discriminator truthfulness, upstream dependency handling | Does not claim unsupported uniqueness or proceed blindly without win strategy |
| `writing-past-performance` | 3 | Scenario-supplied inputs | Past performance write-ups | Relevance mapping, honest problem handling, evidence discipline | Does not fabricate, hide performance problems, or stretch relevance |
| `developing-key-personnel` | 3 | Scenario-supplied inputs | Key personnel resumes and staffing case | Qualification mapping, missed-minimum detection, availability check | Does not bury misses, imply unavailable staff, or invent qualifications |
| `narrating-cost-volumes` | 3 | Scenario-supplied inputs | Cost/price volume narrative, BOE rationale | Cost-model boundary, cost-technical consistency, BOE traceability | Does not generate cost numbers or use vague BOE rationale |
| `reviewing-color-teams` | 4 | `synthetic-proposal-section.md` | Color team findings, scores, Green Team review output | Section M scoring, deficiency classification, review-vs-rewrite boundary, cost-volume review | Does not rewrite instead of review or soften real deficiencies |
| `running-review-recovery` | 3 | Scenario-supplied inputs | Recovery dashboard, finding closure records | Deficiency prioritization, verification before closure, escalation of unworkable window | Does not close findings without verification or hide schedule impossibility |
| `checking-submission-compliance` | 3 | `synthetic-proposal-section.md` plus final-package scenario inputs | Submission checklist and compliance findings | Page/format checks, price leakage detection, mechanics/deadline verification | Does not miss misplaced price info or assume portal mechanics are fine |
| `preparing-orals` | 3 | Scenario-supplied inputs | `22-orals-package.md` | Section M structure, Q&A rehearsal, presenter restriction compliance | Does not violate presenter rules or rehearse generic answers only |
| `analyzing-debriefs` | 3 | Scenario-supplied inputs | Debrief request, analysis, lessons learned | Timely debrief handling, counsel handoff for irregularities, reusable learning | Does not provide legal conclusions, chase sour grapes, or skip lessons |

## Fixture Notes

The fixture set is intentionally small:

| Fixture | Coverage role |
|---|---|
| `fixtures/synthetic-rfp.md` | Supports solicitation-structure evaluations. |
| `fixtures/synthetic-proposal-section.md` | Supports draft, review, and compliance evaluations. |

Most skills use scenario-supplied inputs rather than fixture files. Add another
synthetic fixture only when repeated scenarios need shared material.

## Coverage Observations

Strengths:

- Every lifecycle skill has evaluation coverage.
- Expected behaviors are generally observable.
- Anti-behaviors are present across all skill evaluation files.
- The harness supports result records and before/after comparison.

Possible later improvements:

- Add an upstream-artifact assumptions column if maintainers want stronger
  pipeline coverage.
- Add a sensitivity/procurement-integrity column after a skill-by-skill
  sensitivity pass.
- Add result summaries only after actual evaluation runs are recorded.
