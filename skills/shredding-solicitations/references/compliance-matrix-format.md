# Compliance Matrix Format

The structure, ID scheme, columns, and status values for the compliance matrix.

## Contents
- What the matrix is for
- The requirement ID scheme
- The columns
- Compliance status values
- The format and submission register
- Keeping the matrix alive

## What the matrix is for

The compliance matrix is the single source of truth for what the proposal must
contain. It serves three audiences: proposal writers (what to write and where),
reviewers (what to check against), and the proposal manager (what is done and
what is not). Every downstream skill reads it.

## The requirement ID scheme

Every requirement gets a stable, unique ID so it can be referenced everywhere —
in the outline, in section drafts, in color team findings. The scheme encodes
the source:

`<SOURCE>-<SECTION>-<NN>`

- `SOURCE` — `L`, `M`, `C` (or `SOW`/`PWS`/`SOO`/`H` as applicable).
- `SECTION` — the section or paragraph number from the solicitation.
- `NN` — a sequence number for atomic requirements split from one paragraph.

Examples: `L-3.2-01` (first requirement extracted from Section L paragraph 3.2),
`M-2-03` (third evaluated element under Section M factor 2), `PWS-4.1-02`.

IDs are permanent. If an amendment changes a requirement, keep the ID and note
the change; do not renumber, or every downstream reference breaks.

## The columns

The matrix is a table with one row per atomic requirement:

| Column | Content |
|---|---|
| Req ID | The stable ID above. |
| Source | Section and paragraph the requirement came from. |
| Requirement | The atomic requirement, in the solicitation's own terms. |
| Type | Instruction (L) / Evaluation (M) / Performance (C/SOW/PWS) / Objective (SOO) / Format / Admin. |
| Mandatory | Yes (shall/must/will) / No (should/may). |
| Volume & section | The proposal volume and section that will address it. |
| Section L ref | The governing instruction (cross-walk). |
| Section M ref | The factor/subfactor that evaluates it (cross-walk). |
| Win theme | The theme to thread here, from `05-win-strategy.md`, if available. |
| Owner | The proposal author responsible. |
| Status | See below. |
| Notes | Conflicts, ambiguities, CO questions, amendment history. |

The Volume & section, Owner, and Status columns are populated as the proposal
develops; `shredding-solicitations` creates the matrix and fills the rest.

## Compliance status values

- **Not started** — no proposal content yet addresses this requirement.
- **In draft** — content is being written.
- **Drafted** — content exists and addresses the requirement.
- **Compliant** — content has been verified to fully satisfy the requirement.
- **At risk** — content exists but does not yet fully satisfy the requirement,
  or a conflict/gap blocks it.
- **N/A** — not applicable, with a recorded reason.

A proposal is ready to submit only when every mandatory requirement is
**Compliant**.

## The format and submission register

Format, page, and submission rules are extracted into a separate labeled section
of the artifact, not mixed with content requirements, because a different
skill — `checking-submission-compliance` — verifies them at the end. The
register records, at minimum:

- Page limit per volume and what counts against it (and what is excluded).
- Font, point size, margin, spacing, and line-count rules.
- File format, file naming, and file-size limits.
- Volume separation rules (e.g., price kept out of the technical volume).
- Due date, due time, and time zone.
- Submission method (portal, email, physical) and any registration required.
- Required forms, certifications, and representations (Section K).

## Keeping the matrix alive

The matrix is a living artifact. As the proposal develops, owners update the
status column. As amendments arrive, requirements are updated in place with IDs
preserved and changes noted. A stale matrix is worse than none — it creates
false confidence. Re-date the artifact on every update.
