---
name: writing-past-performance
description: Builds past performance write-ups for a US Federal proposal. Use when the user needs past performance, a past performance volume, past performance citations or references, CPARS or PPQ-based write-ups, or relevance narratives for a federal bid. Selects references for recency, relevancy, and quality; maps each prior contract to the current requirement on the dimensions Section M evaluates; and substantiates performance quality with evidence.
---

# Writing Past Performance

Build the past performance write-ups: the evidence that the offeror has done
work like this before and done it well. Federal evaluators assess past
performance for three things (recency, relevancy, and quality) and they assess
relevancy strictly, against the current requirement. A past performance volume
that lists impressive contracts without proving they resemble *this* work earns
far less than the contracts deserve. This skill writes to the three tests.

## When to use this skill

Use this skill to develop the past performance volume or past performance
citations for a federal proposal. It works from a library of the offeror's (and
teaming partners') prior contracts.

It does not write key-personnel experience — that is `developing-key-personnel`.
Past performance is about *organizational* performance on prior contracts.

## Inputs

**Required:**
- The solicitation's past performance instructions (Section L) and evaluation
  criteria (Section M) — they define recency, relevancy, the reference count and
  format, and how quality is judged.
- A past performance library in `source/` — the prior contracts available to
  cite, with their facts (customer, value, period, scope) and any performance
  records (CPARS ratings, PPQs, award fees, metrics).

**Preferred upstream artifacts:**
- `10-compliance-matrix.md`: the past performance requirement rows.
- `05-win-strategy.md`: past performance is often a major proof source for win
  themes; coordinate.

**Without performance records**, the write-ups can still describe relevance, but
flag every unsubstantiated quality claim — quality with no evidence is weak.

Read `../../shared/glossary.md`, `../../shared/federal-solicitation-primer.md`,
and `../../shared/pursuit-workspace.md` if not already read this session.

## Intake

Ask these as a numbered list. Skip what the solicitation answers.

1. **The rules.** What does Section L require — how many references, what format,
   what page or word limit each, prime vs. subcontractor references, the recency
   window (how far back counts)?
2. **The relevancy definition.** How does Section M define relevancy — on scope,
   size/dollar value, complexity, contract type, customer, place of performance?
   What does it count as "similar"?
3. **The library.** What prior contracts are available to cite, and for each:
   customer, value, period of performance, scope, the offeror's role
   (prime/sub), and any performance evidence?
4. **Quality evidence.** What performance records exist — CPARS ratings, PPQs,
   award-fee history, customer commendations, quantified outcomes?
5. **Known problems.** Did any candidate reference have performance problems? If
   so, what happened and what was the corrective action?

## Workflow

```
Past Performance:
- [ ] Step 1: Establish the recency, relevancy, and quality rules
- [ ] Step 2: Score and select references
- [ ] Step 3: For each reference, build the relevance mapping
- [ ] Step 4: Substantiate performance quality
- [ ] Step 5: Draft each write-up
- [ ] Step 6: Address any performance problems honestly
- [ ] Step 7: Write the artifacts and update the matrix
```

**Step 1: The rules.** From Section L and M, pin down exactly what recency,
relevancy, and quality mean for *this* solicitation, and the reference count and
format. Use `references/past-performance-method.md`.

**Step 2: Select references.** Score every library contract on recency,
relevancy, and quality against the Step 1 rules. Select the set that maximizes
all three, within the allowed count. The strongest reference is the most
*relevant* one with strong quality — not the largest or most famous. Prefer
references where the offeror was prime unless the solicitation values
subcontractor experience equally.

**Step 3: Relevance mapping.** For each selected reference, build an explicit
mapping: dimension by dimension (scope, size, complexity, contract type,
customer, place of performance), show how the prior contract resembles the
current requirement. This mapping is the heart of the write-up. Do not make the
evaluator infer relevance — state it, on the dimensions Section M uses.

**Step 4: Substantiate quality.** Attach the performance evidence: CPARS
ratings, PPQ scores, award fees earned, quantified results, commendations. Make
quality verifiable, not asserted.

**Step 5: Draft.** Draft each write-up using `templates/past-performance-writeup.md`:
the contract facts, a concise scope description, the relevance mapping, and the
quality evidence — within the format and length Section L allows.

**Step 6: Address problems.** If a selected reference had a performance
problem, address it honestly: what happened, the corrective action, and the
result. Evaluators often have access to CPARS; a problem the offeror omits and
the evaluator finds independently is far more damaging than one the offeror
explains. If a reference's problems are severe, the better move is usually to
select a different reference.

**Step 7: Write and update.** Save each write-up in the workspace's
`14-past-performance/` directory. Update the past performance rows of
`10-compliance-matrix.md`.

## Output

One file per reference in `14-past-performance/`, plus updated matrix status.

Present the user with: the selected references and why each was chosen, the
relevance strength of each, any quality gaps, and any performance problem that
needs a decision.

## References

- `references/past-performance-method.md`: recency, relevancy, and quality; scoring and selecting references; the relevance mapping; substantiating quality; and handling performance problems.
- `templates/past-performance-writeup.md`: the per-reference write-up template.

## Guardrails

- **Relevance is the discriminator.** Lead every write-up with how the prior
  work resembles *this* requirement, on Section M's dimensions. An impressive
  but non-relevant contract scores low.
- **Substantiate quality.** Use CPARS, PPQs, award fees, metrics. Replace
  "performed excellently" with the rating that proves it.
- **Never fabricate.** Do not invent contracts, ratings, values, or outcomes.
  Past performance is verifiable; fabrication is a disqualifying integrity
  failure.
- **Honesty about problems.** A known problem is explained with its corrective
  action, or the reference is replaced — never hidden.
- **Respect the format.** Reference count, format, and length limits in Section L
  are hard rules.
