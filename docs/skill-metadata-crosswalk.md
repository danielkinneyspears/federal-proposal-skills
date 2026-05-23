# Skill Metadata Crosswalk

This crosswalk maps the package's 21 skills to a compact discovery vocabulary:

- `phase`
- `canonical_job`
- `common_names`
- primary inputs
- primary outputs

The current skill frontmatter remains intentionally simple. This document gives
maintainers and contributors a single place to review the vocabulary before any
future frontmatter expansion.

## Phase Vocabulary

The crosswalk uses three broad phases:

| Phase | Meaning |
|---|---|
| `plan` | Decide whether and how to pursue, and shape the win. |
| `create` | Turn the pursuit position into a compliant, compelling response. |
| `iterate` | Test, fix, approve, submit, and learn. |

These phases align with the sibling `govcon-pursuit-brain` lifecycle taxonomy.
The README still presents the package in four familiar proposal lifecycle
groups: Capture, Proposal development, Review and submission, and
Post-submission.

## Crosswalk

| Skill | Phase | Canonical job | Common names | Primary inputs | Primary outputs |
|---|---|---|---|---|---|
| `qualifying-opportunities` | `plan` | `opportunity-qualification` | bid/no-bid, gate review, go/no-go, pursuit decision, opportunity qualification, sizing | opportunity notice, solicitation summary, customer/competitor/capability facts | `00-opportunity-profile.md`, `01-bid-decision.md` |
| `planning-capture` | `plan` | `capture-planning` | capture plan, pursuit plan, capture strategy, customer engagement plan, shaping plan | opportunity profile, bid decision, customer intelligence, action gaps | `02-capture-plan.md` |
| `analyzing-competitors` | `plan` | `competitive-intelligence` | Black Hat, competitor analysis, market intel, incumbent assessment, competitive assessment, recompete analysis | opportunity profile, known competitors, public competitor data, customer context | `03-competitive-assessment.md` |
| `estimating-price-to-win` | `plan` | `price-to-win` | PTW, business case, pricing strategy, target price, competitive pricing analysis | opportunity profile, competitive assessment, budget/IGCE signals, evaluation model | `04-price-to-win.md` |
| `developing-win-strategy` | `plan` | `win-strategy` | win themes, discriminators, value proposition, ghosting strategy, ghosting language | customer hot buttons, discriminators, competitive assessment, price-to-win | `05-win-strategy.md` |
| `responding-to-rfis` | `plan` | `solution-shaping` | RFI response, sources-sought response, draft-RFP comments, white paper, capability statement, requirement shaping | notice or draft RFP, company capabilities, customer priorities, shaping goals | `06-shaping-response-<type>.md` |
| `developing-teaming-strategy` | `plan` | `teaming-and-partner-strategy` | teaming, partner selection, JV strategy, mentor-protege strategy, subcontractor strategy, OCI screening | capability gaps, small-business requirements, partner options, workshare constraints | `07-teaming-strategy.md` |
| `developing-solution-approach` | `plan` | `solution-shaping` | solution approach, solution architecture, technical approach shaping, solutioning, staffing model, management model | requirements, win strategy, price constraints, capture plan, compliance drivers | `08-solution-design.md` |
| `managing-proposal-operations` | `create` | `submission-package-assembly` | proposal management plan, schedule, kickoff, RACI, action register, question log, production planning | solicitation, proposal calendar, team roster, compliance matrix, milestones | `09-proposal-management/` |
| `shredding-solicitations` | `create` | `compliance-tracing` | solicitation shred, RFP shred, requirements matrix, compliance matrix, L/M/C trace, requirements traceability | solicitation, amendments, Section L, Section M, SOW/PWS/SOO | `10-compliance-matrix.md` |
| `outlining-proposals` | `create` | `annotated-outline` | outline, proposal outline, annotated outline, storyboards, proposal structure, page budget | compliance matrix, Section L/M, win strategy, solution design | `11-proposal-outline.md` |
| `drafting-proposal-sections` | `create` | `technical-volume-drafting` | section drafting, technical approach drafting, technical narrative, solution writing, proposal narrative | approved storyboards, compliance matrix, solution design, win themes, proof points | section draft artifacts |
| `writing-executive-summaries` | `create` | `claims-and-proof-points` | executive summary, proposal summary, opening volume, value proposition, proof point development | win strategy, customer hot buttons, discriminators, solution approach | executive summary artifact |
| `writing-past-performance` | `create` | `past-performance-volume` | PP write-ups, past performance references, citations volume, relevance narratives | past performance references, Section L/M criteria, CPARS/quality evidence | past performance write-ups |
| `developing-key-personnel` | `create` | `management-volume-drafting` | key personnel, tailored resumes, staffing qualifications, staffing approach, letters of commitment | resumes, labor category requirements, Section L/M criteria, availability evidence | key personnel resumes and staffing case |
| `narrating-cost-volumes` | `create` | `cost-and-pricing-volume` | cost volume, price volume, pricing buildup, BOE, cost narrative, cost-realism narrative | pricing model, BOE inputs, technical solution, staffing plan, solicitation cost instructions | cost/price volume narrative |
| `reviewing-color-teams` | `iterate` | `evaluator-perspective-review` | Blue Team, Pink Team, Green Team, Red Team, Gold Team, White Glove, mock evaluation, color team review | draft proposal, compliance matrix, Section M, review criteria | color team findings and scores |
| `running-review-recovery` | `iterate` | `review-recovery` | comment adjudication, recovery, finding closure, correction tracking, recovery dashboard | color team findings, proposal drafts, compliance matrix, assignments | recovery dashboard and closure records |
| `checking-submission-compliance` | `iterate` | `submission-compliance-check` | final compliance check, final compliance review, production check, page-count check, pre-submission checklist | final volumes, Section L, forms, portal rules, file package | submission checklist and compliance findings |
| `preparing-orals` | `iterate` | `executive-readiness-review` | orals prep, oral presentation, proposal briefing, pitch, evaluator Q&A rehearsal, executive readiness | written proposal, win strategy, technical approach, Section M, presenter roster | orals package |
| `analyzing-debriefs` | `iterate` | `debrief-analysis` | debrief, debrief request, debrief questions, win/loss analysis, post-mortem, lessons learned | award notice, debrief materials, proposal record, evaluation feedback | debrief analysis and lessons learned |

## Notes On Approximate Mappings

Some skills in this artifact pipeline are broader or more specific than one
canonical job in the sibling wiki-native taxonomy:

- `responding-to-rfis` maps to `solution-shaping`, though pre-RFP shaping
  responses may eventually deserve their own canonical job.
- `managing-proposal-operations` maps to `submission-package-assembly`, but it
  spans broader proposal operations.
- `writing-executive-summaries` maps to `claims-and-proof-points`, but executive
  summary writing may deserve a first-class canonical job later.
- `developing-key-personnel` maps to `management-volume-drafting`, because
  there is not currently a standalone key-personnel job.
- `reviewing-color-teams` maps to `evaluator-perspective-review`, although the
  skill covers multiple review types.
- `preparing-orals` maps to `executive-readiness-review`, but orals preparation
  may eventually deserve a standalone canonical job.

## Future Frontmatter Option

If this vocabulary proves useful, a later change could add selected metadata
fields to each `SKILL.md` frontmatter block. That should be reviewed separately
because it would touch all 21 skill files.
