# Changelog

All notable changes to this package are documented here. Format loosely follows
[Keep a Changelog](https://keepachangelog.com/); versions follow semantic versioning.

## [0.2.1] — unreleased

Sibling-pointer release. Adds a discoverable mention of the wiki-native
sibling package so users see both options when choosing how to adopt
GovCon proposal skills.

### Added
- **README "Sibling package" section** — points at the optional sibling
  `govcon-pursuit-brain`, which handles the same lifecycle as a
  wiki-native knowledge graph and additionally ships a comprehensive
  Obsidian-compatible federal-acquisition domain wiki.
- The sibling is positioned as **completely optional**: teams with their
  own knowledge base / wiki / brain for federal acquisition use that;
  teams without one can adopt the sibling's `knowledge/` directory as a
  starter pack. Both packages stand alone and are launched together so
  users can pick the model that fits their workflow.

## [0.2.0] — unreleased

Connective-tissue release. Addresses a second external review finding that the
package generated artifacts well but under-served the operational work *between*
artifacts. Adds five skills and broadens the review model. The package now has
twenty-one skills.

### Added
- `managing-proposal-operations` — runs the proposal as a managed project:
  proposal management plan, backward-built schedule, volume plan and RACI,
  action item register, question log, amendment impact control, review and
  production logistics. Artifact set: `09-proposal-management/`.
- `responding-to-rfis` — drafts pre-RFP shaping responses: sources-sought
  responses, RFI responses, draft-RFP comment matrices, white papers, capability
  statements. Artifact: `06-shaping-response-<type>.md`.
- `developing-teaming-strategy` — capability and past-performance gap analysis,
  partner scoring, workshare, OCI and set-aside screening, teaming agreements,
  subcontractor data calls. Artifact: `07-teaming-strategy.md`.
- `developing-solution-approach` — designs the proposal-ready solution
  (technical, staffing, management, transition, risk, quality) against
  requirements, win themes, and the price-to-win target. Artifact:
  `08-solution-design.md`.
- `running-review-recovery` — turns color team findings into assigned,
  completed, and verified corrections; produces a recovery burn-down. Artifact:
  `23-review-recovery.md`.
- Evaluation scenarios for the five new skills.

### Changed
- `reviewing-color-teams` broadened from three reviews to six — adds Blue
  (solution and win strategy), Green (cost/price volume), and White Glove
  (production / book check) to Pink, Red, and Gold.
- `planning-capture` capture plan now includes an explicit stakeholder and
  influence map (influence, disposition, access quality) and contact reports
  with a next-legitimate-touch field, replacing the lighter prose treatment.
- Shared `proposal-lifecycle.md` and `pursuit-workspace.md` updated for the new
  skills, artifacts, and review model.

## [0.1.1] — unreleased

Review response. Addresses findings from an external review against the Claude
Code skill/plugin docs and Anthropic skill-authoring best practices.

### Added
- `scripts/package-skill.sh` — builds self-contained standalone skill zips with
  the shared knowledge base bundled in and `../../shared/` paths rewritten, so a
  single skill can be uploaded to claude.ai or the Skills API.
- Pursuit workspace bootstrap in `shared/pursuit-workspace.md` — skills now
  verify the workspace location is not in tracked version control (and add a
  `.gitignore` entry or recommend an untracked location) before writing
  sensitive artifacts.
- Cross-artifact merge protocol in `shared/pursuit-workspace.md` — read current,
  diff intended changes, preserve hand-edited content, record a change note,
  surface conflicts.
- Deterministic validation scripts for `checking-submission-compliance`:
  `pdf_page_count.py`, `check_file_package.py`, `scan_price_leakage.py`.
- Synthetic evaluation fixtures (`evaluations/fixtures/`) and an evaluation
  harness (`evaluations/run-evals.md`) with a result-record template.
- "Regulatory currency" guidance in `shared/federal-solicitation-primer.md` and
  the README limits, directing verification of current FAR/agency rules for
  deadline-sensitive and legally adjacent tasks.

### Changed
- README install section now states the package is designed for plugin /
  whole-repo distribution and documents the standalone packaging path, replacing
  the inaccurate "each skill folder is standalone" claim.
- `.gitignore` excludes `dist/` and `evaluations/results/`.

## [0.1.0] — unreleased

Initial build — the complete sixteen-skill package.

### Added
- Repository scaffold: Claude Code plugin manifest, marketplace manifest, license, contributing guide.
- Shared knowledge base under `shared/`: glossary, proposal lifecycle map, pursuit workspace convention, federal solicitation primer.
- All sixteen lifecycle skills under `skills/`, each with `SKILL.md`, reference
  files, and a template:
  - Phase 1 (Capture): `qualifying-opportunities`, `planning-capture`,
    `analyzing-competitors`, `estimating-price-to-win`, `developing-win-strategy`.
  - Phase 2 (Proposal development): `shredding-solicitations`,
    `outlining-proposals`, `drafting-proposal-sections`,
    `writing-executive-summaries`, `writing-past-performance`,
    `developing-key-personnel`, `narrating-cost-volumes`.
  - Phase 3 (Review and submission): `reviewing-color-teams`,
    `checking-submission-compliance`.
  - Phase 4 (Post-submission): `preparing-orals`, `analyzing-debriefs`.
- Evaluation scenarios (three per skill) under `evaluations/`.

### Not yet done
- The package has not been exercised on real solicitations end to end.
- Synthetic fixtures for the evaluation scenarios are not yet built.
