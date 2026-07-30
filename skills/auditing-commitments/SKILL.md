---
name: auditing-commitments
description: Audits a US Federal proposal draft for the obligations it creates, and flags promises stronger than the solicitation requires. Use when the user needs a commitment audit, a promise review, an obligation review, a check for overcommitting, a review of "we will" and "shall" language, a check that the draft does not guarantee more than the RFP asked for, or a review of AI-generated proposal content before it goes out. Produces a commitment register mapping every promise to the requirement behind it, with the delta priced and the unsupported promises listed.
---

# Auditing Commitments

A proposal is a binding offer. Every "we will", "we shall", "we guarantee" and
"we ensure" is a candidate obligation, and if it survives into the contract the
offeror performs it at its own cost for the life of the award — sometimes with
the proposal incorporated wholesale by reference. Overcommitting is not a writing
problem, it is a margin problem that surfaces in month three of performance.

This skill inventories every promise in a draft, maps each one to the requirement
that justifies it, and prices the difference where the promise is stronger than
the requirement.

## When to use this skill

Use this skill after drafting and before the Red Team, on any volume that makes
performance commitments. Run it again on any section rewritten during review
recovery.

Run it always on **AI-generated or AI-assisted draft content**. Generated
proposal prose overcommits substantially more than human prose, and it does so in
one direction: fluent future-tense verbs read as confidence, so a model
optimising for confident prose accumulates obligations. The draft sounds strong
and the delta is invisible until award.

Distinguish it from adjacent skills:

- `checking-submission-compliance` asks whether the proposal will be *accepted*.
  This skill asks what the proposal *obligates you to do*.
- `reviewing-color-teams` asks whether the proposal is persuasive and scoreable.
  This skill is indifferent to persuasion; a beautifully written unbounded
  guarantee is exactly what it exists to catch.
- `shredding-solicitations` establishes what was required. This skill depends on
  that output and does not re-derive it.

## Inputs

**Required:**
- The draft under audit — one volume, one section, or the full package.
- `10-compliance-matrix.md`, for the authoritative list of requirements.

**Preferred upstream artifacts:**
- `08-solution-design.md`: to test whether each promise is actually staffed and
  funded as written.
- `16-cost-narrative.md`: to test cost-technical consistency on any promise with
  a price consequence.
- `05-win-strategy.md`: to distinguish a deliberate, funded differentiator from
  an accident.

Read `../../shared/glossary.md`,
`../../shared/federal-solicitation-primer.md`, and
`../../shared/pursuit-workspace.md` if not already read this session.

## Intake

Ask these as a numbered list.

1. **Scope.** Which volumes or sections are in scope, and is the draft final or
   still moving?
2. **Provenance.** Which parts were drafted by a person and which by a tool? Name
   the tool if known. This changes where to look hardest, not whether to audit.
3. **Delivery reality.** Who will perform this work after award, and have they
   read the draft? An unread promise is an unverified one.
4. **Incorporation risk.** Does the solicitation state that the proposal will be
   incorporated into the resulting contract, in whole or in part? Quote the
   language if present.
5. **Known stretch.** Is there any commitment the team already knows is
   ambitious? Start there.

## Workflow

```
Commitment Audit:
- [ ] Step 1: Extract every candidate obligation
- [ ] Step 2: Classify each one
- [ ] Step 3: Map each to its requirement
- [ ] Step 4: Price the delta where the promise is stronger
- [ ] Step 5: Test supportability against the solution and cost volumes
- [ ] Step 6: Test measurability and stated conditions
- [ ] Step 7: Write the commitment register (19-commitment-audit.md)
```

**Step 1: Extract.** Read the draft for verbs, not for argument. Mark every
`will`, `shall`, `guarantee`, `ensure`, `maintain`, `provide`, `deliver`,
`commit`, `warrant`, `achieve` and `exceed`, plus every number attached to one.
Run `scripts/scan_commitments.py <file>` first for a deterministic pass, then
read for what a regex cannot catch: promises made in the present tense, promises
implied by a graphic or a table, and promises buried in a resume or a past
performance write-up.

**Step 2: Classify.** Sort each hit into one of four kinds, using
`references/commitment-patterns.md`:

- **Obligation** — a performance promise with a measurable outcome.
- **Absolute** — `100%`, `zero`, `never`, `always`, `24/7`, `no downtime`. These
  are uninsurable by construction; one ordinary bad day is a documented failure.
- **Number** — a figure with a unit, a percentage or a currency attached.
- **Filler** — `strive`, `endeavor`, `best effort`, `world-class`. No metric, no
  obligation, no score, and it is consuming page count in a page-limited volume.

**Step 3: Map.** For each obligation, absolute and number, find the requirement
it answers and quote that requirement verbatim from the compliance matrix. If no
requirement exists, record `NONE FOUND` — do not infer one. Then record whether
the promise is *weaker than*, *equal to*, or *stronger than* the requirement.

**Step 4: Price the delta.** For every promise stronger than its requirement,
state what the difference costs to perform over the full period of performance:
staffing, licences, equipment, vessel or field access, recurring hosting, warranty
exposure. A delta with no stated cost has not been audited, only noticed. Note
also whether the extra earns evaluation credit — a stronger promise that Section M
does not reward is pure cost.

**Step 5: Supportability.** For each promise, test it against
`08-solution-design.md` and `16-cost-narrative.md`: is it staffed and funded
*exactly as written*? The classic failure is a response-time or availability
commitment whose staffing plan funds a single shift. Flag every promise the
solution does not support as a solution problem or a bid problem, not a wording
problem.

**Step 6: Measurability and conditions.** For each promise ask who measures it,
by what method, and under what conditions. A performance figure that depends on
conditions outside the offeror's control — feed composition, site conditions,
weather windows, wave resource, a customer-supplied input — must state those
conditions or it becomes an unconditional promise. Rewrite candidates belong in
the register, not in the draft; this skill does not edit the proposal.

**Step 7: Write.** Write `19-commitment-audit.md` using
`templates/commitment-audit.md`.

## Output

One artifact: `19-commitment-audit.md` — the commitment register, plus four
ranked lists: promises stronger than the requirement (ranked by delta cost),
promises with no requirement behind them, promises the solution does not support,
and promises that cannot be measured as written.

Present the user with: the count of candidate obligations, the three most
expensive deltas with what each costs, every unsupported promise, and a clear
statement of which items are wording fixes and which are solution or bid
decisions.

## Utility scripts

- `scripts/scan_commitments.py <file> [--json]`: deterministic scan for
  commitment verbs, absolutes, numbers with units and filler. Reports line
  numbers, a count per category, and obligations per 250 words so a long volume
  and a single section can be compared. Standard library only.

The scan is a starting point and deliberately over-matches. Finding the verb is
mechanical; deciding whether the promise is affordable is not, which is why every
hit is a candidate for human judgement rather than a finding.

## References

- `references/commitment-patterns.md`: the recurring overcommitment patterns, what each sounds like in a draft, and the defensible form.
- `templates/commitment-audit.md`: the commitment register artifact template.

## Guardrails

- **Do not rewrite the proposal.** This skill produces an inventory and a
  recommendation. Editing the draft is `running-review-recovery`, and softening
  language on the author's behalf hides the decision they need to make.
- **Never soften silently.** If a promise should be narrowed, say so explicitly
  and show the before and after in the register. A quiet edit is how a real
  differentiator gets deleted.
- **`NONE FOUND` is a finding, not a gap in the audit.** A promise with no
  requirement behind it is the most common and most expensive pattern. Record it
  plainly rather than searching for a justification.
- **Stronger is not automatically wrong.** A promise beyond the requirement that
  is scored, funded and deliberate is a differentiator. The register records the
  cost and lets the capture lead decide; it does not moralise about ambition.
- **The compliance matrix governs.** Requirements come from
  `10-compliance-matrix.md` and the solicitation, never from memory or inference.
- **Price consequences belong to the cost volume.** Where a delta has a cost,
  flag it for `narrating-cost-volumes` rather than estimating a number this skill
  cannot substantiate.
