---
name: checking-submission-compliance
description: Runs the final production and submission-compliance check on a US Federal proposal before submission. Use when the user needs a submission compliance check, a final compliance review, a production check, a page-count or format check, a forms and certifications check, or a pre-submission checklist for a federal bid. Verifies page limits, format rules, file naming, volume separation, required forms and certifications, and submission mechanics, and confirms every mandatory requirement is satisfied.
---

# Checking Submission Compliance

Run the last check before the proposal is submitted. A technically excellent
proposal can still be thrown out for a format technicality — an over-length
volume, a missing certification, price information in the wrong file, a late
upload. The government can and does reject non-conforming proposals without
evaluating them. This skill verifies, methodically, that the proposal will be
accepted and evaluated.

## When to use this skill

Use this skill at the end of the proposal process, after the Gold Team and
before submission. Run it on the final or near-final proposal package.

It is not a content review — `reviewing-color-teams` assesses whether the
proposal is good. This skill assesses whether the proposal is *conforming*: will
it be accepted, opened, and evaluated rather than rejected.

## Inputs

**Required:**
- The final proposal package — every volume and file intended for submission.
- `10-compliance-matrix.md`, including its format and submission register.
- The solicitation Sections L and K, and any submission instructions or portal
  guidance.

**Preferred upstream artifacts:**
- `20-color-review-*.md`: to confirm color team findings were resolved.

Read `../../shared/glossary.md`,
`../../shared/federal-solicitation-primer.md`, and
`../../shared/pursuit-workspace.md` if not already read this session.

## Intake

Ask these as a numbered list. Most answers come from the compliance matrix's
format register and Section L.

1. **The package.** What files make up the submission package, and which volume
   does each represent? Is the package final?
2. **Format rules.** What are the page limits per volume, and the font, point
   size, margin, and spacing rules? What counts toward and is excluded from page
   limits?
3. **File rules.** What file formats, file-naming conventions, and file-size
   limits does Section L impose? What volume-separation rules apply (for example,
   price kept out of the technical volume)?
4. **Forms and certifications.** What forms, representations, and certifications
   does the solicitation require (Section K, the cover form, any
   solicitation-specific certifications)? Is the offeror's SAM.gov registration
   active?
5. **Submission mechanics.** How, where, and by exactly when must the proposal
   be submitted — portal, email, or physical; the due date, time, and time zone;
   any required pre-registration?

## Workflow

```
Submission Compliance Check:
- [ ] Step 1: Load the format and submission register
- [ ] Step 2: Check format compliance per volume
- [ ] Step 3: Check file format, naming, size, and volume separation
- [ ] Step 4: Check required forms, representations, and certifications
- [ ] Step 5: Check submission mechanics and the deadline
- [ ] Step 6: Confirm every mandatory requirement is satisfied
- [ ] Step 7: Write the submission checklist (21-submission-checklist.md)
```

**Step 1: Load the register.** Read the format and submission register from
`10-compliance-matrix.md` and the Section L/K rules. Use
`references/submission-compliance-checklist.md` as the master checklist.

**Step 2: Format per volume.** For each volume, verify the page count is at or
under the limit (counting only what counts), and verify font, point size,
margins, spacing, and any line-per-page rule. An over-length volume is a common
rejection cause; the government may simply not read the pages past the limit, or
reject the volume. For PDF volumes, run `scripts/pdf_page_count.py <file.pdf>`
to get an exact physical page count, then apply the solicitation's rule for what
counts toward the limit.

**Step 3: Files and separation.** Verify file formats, file names (exact naming
conventions matter on portals), and file sizes against the rules. Run
`scripts/check_file_package.py <dir> --max-mb N --pattern REGEX` over the
submission directory to check every file's size and name against the Section L
rules. Verify volume-separation rules — most critically that price and cost
information appear only where permitted and nowhere else; run
`scripts/scan_price_leakage.py <textfile>` over the extracted text of each
non-price volume and review every candidate hit.

**Step 4: Forms and certifications.** Verify every required form, representation,
and certification is present, complete, and signed where required — the cover
form, Section K reps and certs, and any solicitation-specific certifications.
Confirm the offeror's SAM.gov registration is active (an inactive registration
can bar award).

**Step 5: Mechanics and deadline.** Verify the submission method, the portal or
address, any required registration, and the exact due date, time, and time zone.
Late is late: FAR rules on late proposals are strict. Confirm the team's plan
submits with margin, not at the deadline.

**Step 6: Mandatory requirements.** Walk the compliance matrix: confirm every
mandatory requirement has status "Compliant". Any mandatory requirement not
compliant is a go/no-go issue, not a checklist footnote.

**Step 7: Write.** Write `21-submission-checklist.md` using
`templates/submission-checklist.md`, with a clear go/no-go line for each item
and an overall submission-readiness verdict.

## Output

One artifact: `21-submission-checklist.md` — the completed checklist with a
pass/fail on every item and an overall verdict.

Present the user with: the overall go/no-go, every failed or at-risk item with
what must be corrected, and the submission deadline and mechanics restated for
certainty.

## Utility scripts

Deterministic checks are more reliable than reading by eye. This skill bundles
three. They report facts; the skill applies the solicitation's rules to the
results.

- `scripts/pdf_page_count.py <file.pdf>`: exact physical page count and
  metadata of a PDF volume. Requires the `pypdf` package (`pip install pypdf`).
- `scripts/check_file_package.py <dir> [--max-mb N] [--pattern REGEX]`: checks
  every file in the submission directory against a size limit and a naming
  pattern. Standard library only.
- `scripts/scan_price_leakage.py <textfile>`: scans the extracted text of a
  non-price volume for price and cost terms. Every hit is a candidate for human
  review. Standard library only.

Run them where they help; fall back to manual inspection where a script does not
apply (for example, font and margin checks, which the script set does not
cover).

## References

- `references/submission-compliance-checklist.md`: the master checklist of everything to verify, and the common causes of proposal rejection.
- `templates/submission-checklist.md`: the submission checklist artifact template.

## Guardrails

- **Conformance, not quality.** This skill checks whether the proposal will be
  accepted and evaluated, not whether it is persuasive. Do not drift into
  content review.
- **A failed item is go/no-go.** An over-length volume, a missing certification,
  or misplaced price information is not a minor note — it is a reason the
  proposal could be rejected. State it as such.
- **Verify, do not assume.** Check the actual files against the actual rules.
  "It should be fine" is not a check.
- **The deadline is absolute.** Treat the due date and time as immovable and
  build in margin. Do not normalize a plan to submit at the last minute.
- **Section L and K govern.** Where this skill's checklist differs from the
  solicitation, the solicitation wins.
