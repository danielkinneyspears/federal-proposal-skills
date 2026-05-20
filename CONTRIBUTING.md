# Contributing

This package improves through real proposal work. Two kinds of contributions are valuable:

1. **Domain corrections** — federal BD practitioners who spot something wrong, dated, or agency-specific.
2. **Skill refinement** — improvements to how a skill behaves when Claude actually runs it.

## Domain corrections

The skills encode federal acquisition practice (FAR structure, source selection, color team conventions, Shipley-style lifecycle). Practice varies by agency and contract vehicle. If a skill states something as universal that is actually agency-specific, open an issue or PR that:

- names the specific skill and file,
- states the correction,
- cites the authority (FAR/DFARS section, agency supplement, or a clearly described common practice), and
- if it is agency- or vehicle-specific, says so rather than overwriting the general guidance.

Do not commit real solicitation text, proprietary data, or source-selection-sensitive material as examples. Use synthetic examples only.

## Refining a skill

Skills are refined by observing how Claude uses them, following Anthropic's recommended loop:

1. **Use the skill on a real task** with a fresh Claude instance.
2. **Observe** where it skips a step, misreads a reference file, picks the wrong skill, or produces weak output.
3. **Diagnose** — usually one of: the `description` mis-triggers, the workflow checklist is missing a step, a reference file is too deep to be read fully, or an instruction is too vague.
4. **Fix the smallest thing** that addresses the observation. Strengthen wording (`MUST` vs `should`), promote a buried rule, or split an overlong reference file.
5. **Re-test** with a fresh instance.

Record the observation and fix in the PR description so the reasoning is preserved.

## Authoring conventions

All skills in this package follow these rules. New skills must match.

- **Naming.** Skill directory and `name` field use gerund form, lowercase with hyphens: `qualifying-opportunities`, `reviewing-color-teams`.
- **Description.** Third person. State what the skill does *and* the triggers/contexts for when to use it. Include federal-specific key terms (the solicitation section names, "compliance matrix", "color team", etc.) so it triggers reliably. Max 1024 characters.
- **SKILL.md body.** Under 500 lines. If it grows past that, move detail into `references/`.
- **Structure.** Every skill folder contains:
  - `SKILL.md` — overview, intake questions, workflow, output spec.
  - `references/` — domain depth loaded on demand. Each reference file over 100 lines starts with a table of contents.
  - `templates/` — output templates the skill fills in (optional).
  - `scripts/` — deterministic utilities the skill runs (optional).
- **References one level deep.** Every reference file links directly from `SKILL.md`. Do not chain reference files.
- **Workflows are checklists.** Multi-step skills give Claude a checklist to copy and track.
- **Intake first.** Each skill opens by asking a short, numbered set of intake questions before producing output, unless the needed inputs are already present in the pursuit workspace.
- **Persist artifacts.** Skills read and write the numbered artifacts defined in [shared/pursuit-workspace.md](shared/pursuit-workspace.md).
- **No time-sensitive claims.** Do not write "as of 2026". If acquisition practice changes, use a dated "superseded practice" note.
- **Terminology.** Use the terms defined in [shared/glossary.md](shared/glossary.md) consistently. Do not mix synonyms.

## Evaluations

Each skill should ship with at least three evaluation scenarios in `evaluations/<skill-name>/`. An evaluation states a representative task, the inputs, and the expected behavior. They are the source of truth for whether a change helps or hurts. See `evaluations/README.md`.

## License

Contributions are accepted under the Apache 2.0 License (see [LICENSE](LICENSE)).
