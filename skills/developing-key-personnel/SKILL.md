---
name: developing-key-personnel
description: Develops key personnel resumes and the staffing case for a US Federal proposal. Use when the user needs key personnel, tailored resumes, staffing qualifications, personnel write-ups, or letters of commitment, or needs to map proposed personnel to the labor-category and qualification requirements of a federal solicitation. Tailors each resume to the position's required qualifications and the Section M evaluation criteria, and substantiates that the named people will be available.
---

# Developing Key Personnel

Develop the key personnel volume: resumes tailored to the requirement, mapped to
the position's required qualifications, and backed by evidence the named people
will actually be on the job. Federal evaluators score key personnel against the
specific qualifications the solicitation states for each position. A generic
resume (even of a strong candidate) forces the evaluator to hunt for the
match. This skill makes the match explicit.

## When to use this skill

Use this skill to develop key personnel resumes and the staffing-qualification
case for a federal proposal. It works from candidate resumes or career
histories supplied by the user.

It does not write the staffing *approach* — the recruiting, retention, and
surge system — which is a management-volume section handled by
`drafting-proposal-sections` (see its `section-types.md`). This skill develops
the named individuals.

## Inputs

**Required:**
- The solicitation's key personnel requirements — Section L (which positions,
  resume format, page limits), Section C/H (position descriptions, minimum
  qualifications), and Section M (how personnel are evaluated).
- Candidate resumes or career histories in `source/`.

**Preferred upstream artifacts:**
- `10-compliance-matrix.md`: the key personnel requirement rows.
- `05-win-strategy.md`: where personnel credentials are a discriminator.

Read `../../shared/glossary.md` and `../../shared/pursuit-workspace.md` if not
already read this session.

## Intake

Ask these as a numbered list. Skip what the solicitation answers.

1. **The positions.** Which positions does the solicitation designate as key
   personnel? For each, what are the stated minimum qualifications — education,
   years and type of experience, certifications, clearance?
2. **Resume rules.** What does Section L require for resume format, length,
   content, and order? Are letters of commitment required?
3. **Evaluation.** How does Section M evaluate key personnel — pass/fail against
   minimums, or a graded assessment that rewards qualifications beyond the
   minimum?
4. **Candidates.** For each position, who is the proposed candidate, and what is
   their career history? Are they a current employee, a contingent hire, or a
   teaming partner's employee?
5. **Availability.** Is each named person committed and available to start at
   contract award? Are letters of commitment or contingent-hire agreements in
   place?

## Workflow

```
Key Personnel:
- [ ] Step 1: Extract each position's required qualifications
- [ ] Step 2: Match candidates to positions; check minimums
- [ ] Step 3: For each, build the qualification mapping
- [ ] Step 4: Draft each resume, tailored to the requirement
- [ ] Step 5: Confirm commitment and availability evidence
- [ ] Step 6: Write the artifacts and update the matrix
```

**Step 1: Position requirements.** From Section L, C, and H, extract each key
position's required qualifications as a checklist of discrete, verifiable
criteria. Use `references/key-personnel-method.md`.

**Step 2: Match and check minimums.** Assign a candidate to each position.
Check every candidate against every stated minimum. A candidate who misses a
mandatory minimum is a compliance failure — flag it immediately; under a
pass/fail evaluation it can make the whole proposal unawardable. Do not paper
over a gap.

**Step 3: Qualification mapping.** For each candidate, map their experience to
the position's required qualifications, criterion by criterion: for each
required qualification, the specific experience that satisfies it. This mapping
drives the resume.

**Step 4: Draft resumes.** Draft each resume to the Section L format, tailored
to *this* requirement: lead with the qualifications the position requires,
emphasize the experience most relevant to this work and customer, and quantify
accomplishments. Cut experience that does not serve the match. Where Section M
rewards qualifications beyond the minimum, make those visible.

**Step 5: Commitment and availability.** For each named person, confirm the
evidence that they will be available at award: current-employee status, a
signed letter of commitment, or a contingent-hire agreement. Where a person is
not yet committed, flag it — proposing personnel who will not actually be
available is both a performance risk and an integrity risk.

**Step 6: Write and update.** Save each resume in the workspace's
`15-key-personnel/` directory. Update the key personnel rows of
`10-compliance-matrix.md`.

## Output

One file per key person in `15-key-personnel/`, plus updated matrix status.

Present the user with: the position-by-position match, any candidate who misses
a mandatory minimum, any person not yet committed, and where personnel
qualifications are strong enough to be a discriminator.

## References

- `references/key-personnel-method.md`: extracting position requirements, the qualification mapping, tailoring a resume, resume format, and commitment and availability.
- `templates/key-personnel-resume.md`: the tailored resume template.

## Guardrails

- **Map to the requirement.** Every resume makes the match to the position's
  stated qualifications explicit. Do not submit a generic resume.
- **Minimums are mandatory.** A missed mandatory minimum is a compliance failure
  and is flagged, never glossed.
- **Never fabricate or inflate.** Do not invent or exaggerate degrees,
  certifications, clearances, dates, titles, or experience. Personnel
  qualifications are verifiable; misrepresentation is a disqualifying integrity
  failure and can constitute a false statement.
- **Honesty about availability.** Name only people who will realistically be
  available. Flag anyone not yet committed.
- **Respect the format.** Resume format and length limits in Section L are hard
  rules.
