---
name: drafting-proposal-sections
description: Drafts narrative sections of a US Federal proposal from approved storyboards. Use when the user needs to draft, write, or develop proposal sections, technical volume or management volume narrative, a solution approach, or section content for a federal bid. Writes customer-focused, benefit-led narrative that threads the section's win theme, lands its proof points, stays traceable to the compliance matrix, and is organized so a Section M evaluator can score it easily.
---

# Drafting Proposal Sections

Draft proposal section narrative from approved storyboards — narrative that is
compliant, responsive, and built to be scored. Federal proposal writing has a
specific job: not to describe the offeror, but to make it easy for a tired
evaluator to find the requirement, see it answered, recognize the strength, and
write down a good rating. This skill drafts to that job.

## When to use this skill

Use this skill after `outlining-proposals` has produced the annotated outline
and storyboards, to draft the substantive narrative sections of the technical,
management, and similar volumes.

It does not draft the executive summary (`writing-executive-summaries`), past
performance (`writing-past-performance`), key personnel
(`developing-key-personnel`), or the cost narrative (`narrating-cost-volumes`) —
those have their own conventions and skills. Use this skill for the solution and
approach narrative.

## Inputs

**Required:**
- `11-proposal-outline.md`: the annotated outline and the storyboard for the
  section being drafted.
- `10-compliance-matrix.md`: the requirements the section must satisfy.

**Preferred:**
- `05-win-strategy.md`: the win themes and proof points.
- The solicitation Sections L, M, and C/SOW/PWS — the source of truth.
- Source material in `source/` — past performance, technical facts, resumes.

**Without a storyboard**, do not free-draft. Run `outlining-proposals` for the
section first, or build at least a minimal storyboard with the user. Drafting
without a plan is the failure mode this package exists to prevent.

Read `../../shared/glossary.md` and `../../shared/pursuit-workspace.md` if not
already read this session.

## Intake

Ask these as a numbered list, then confirm before drafting.

1. **Which section(s).** Which outline section(s) is this drafting pass for?
2. **Storyboard status.** Has the storyboard been reviewed and approved? If not,
   draft the storyboard or get it approved first.
3. **Source material.** What factual source material is available for the proof
   points — past performance data, technical details, named personnel, metrics?
   What proof points have no source yet?
4. **Evaluation approach.** Is this a best-value tradeoff or LPTA evaluation?
   (Tradeoff sections sell value; LPTA sections demonstrate clean acceptability
   without gold-plating.)
5. **Page allocation.** What is the section's page budget?

## Workflow

```
Section Drafting:
- [ ] Step 1: Read the storyboard, matrix rows, and source material
- [ ] Step 2: Confirm proof points have real sources
- [ ] Step 3: Draft the section against the storyboard
- [ ] Step 4: Run the compliance self-check
- [ ] Step 5: Run the persuasion self-check
- [ ] Step 6: Write the section file and update the matrix
```

**Step 1: Read.** Read the section's storyboard, every compliance-matrix row
the section owns, the relevant solicitation language, and the source material.

**Step 2: Confirm proof.** Check that every proof point in the storyboard has a
real source. Where a proof point has no source, do not invent one. Flag it: mark
the claim `[PROOF NEEDED: <what is required>]` in the draft and list it for the
user. An unsubstantiated claim is a Red Team finding and a credibility risk.

**Step 3: Draft.** Draft the section following `references/federal-proposal-writing.md`
and the section-type guidance in `references/section-types.md`. The essentials:
- **Lead with the theme.** The section opens with its theme statement, not with
  a restatement of the requirement.
- **Answer the requirement visibly.** Use headings that match Section L/M
  language so the evaluator finds each requirement answered where they expect.
- **Convert features to benefits.** Every capability is carried through to what
  the customer gets.
- **Weave in proof.** Substantiate claims inline with specific evidence.
- **Write for the evaluator.** Short paragraphs, informative headings, action
  captions on graphics, no unsupported superlatives.
- **Stay in the page budget.**

**Step 4: Compliance self-check.** For every compliance-matrix requirement the
section owns, confirm the draft addresses it, in language traceable to the
requirement. Tag each addressed requirement inline (e.g.,
`<!-- covers: PWS-4.1-02 -->`) so reviewers and the matrix can trace it. Any
requirement not yet addressed is named explicitly.

**Step 5: Persuasion self-check.** Apply the checklist in
`federal-proposal-writing.md`: theme present and threaded, benefits not just
features, proof for every claim, customer as the subject, graphics carry an
action caption, nothing gold-plated under LPTA.

**Step 6: Write and update.** Save the section as a file in the workspace's
`12-sections/` directory, named for the outline section. Update the
corresponding rows of `10-compliance-matrix.md` to status "Drafted".

## Output

One file per section in `12-sections/`, plus updated status in the compliance
matrix.

Present the user with: the drafted section, the requirements it covers, any
`[PROOF NEEDED]` flags, and any requirement it could not fully address and why.

## References

- `references/federal-proposal-writing.md`: federal proposal writing conventions: customer focus, theme-first structure, features-to-benefits, substantiation, writing for evaluators, and the persuasion self-check.
- `references/section-types.md`: drafting guidance for common section types: technical/solution, management, transition, staffing, quality control, and risk.
- `templates/section-draft.md`: the section draft file template.

## Guardrails

- **Never invent proof.** A claim with no source is flagged `[PROOF NEEDED]`,
  never fabricated. Invented past performance, metrics, or credentials are a
  catastrophic integrity failure.
- **Draft from a storyboard.** No storyboard, no drafting. The plan comes first.
- **Compliance is the floor.** Every owned requirement is addressed and
  traceable. Persuasion is built on top of compliance, never instead of it.
- **The customer is the subject.** Sections are about what the customer gets,
  not about how good the offeror is.
- **Do not gold-plate under LPTA.** Where the evaluation is LPTA, demonstrate
  clean acceptability; exceeding the requirement adds cost and earns nothing.
