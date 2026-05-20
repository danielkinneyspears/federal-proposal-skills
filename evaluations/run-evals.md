# Evaluation Harness

There is no automated runner for skill evaluations — checking a skill's behavior
requires judgment. This harness makes the process repeatable and the results
recordable, so that after a change to a skill you can tell whether behavior
improved, held, or regressed.

## How to run an evaluation

1. **Start a fresh session** with the skill available (a clean Claude Code
   session with the plugin installed, or the skill uploaded).
2. **Set up inputs.** If the scenario references a fixture, copy it where the
   scenario expects (for example, into a pursuit workspace `source/` directory).
3. **Give the scenario prompt** exactly as written in the skill's evaluation
   file, as if you were the user.
4. **Observe the run** against the scenario's `Expected behavior` and
   `Anti-behavior` lists. Each bullet is one pass/fail check.
5. **Record the result** using the record template below.
6. **Compare to the prior baseline** for that eval. A change is an improvement
   only if it turns a fail into a pass without turning any pass into a fail.

## Fixtures

Synthetic fixtures live in `fixtures/`. They are fictional and contain no real
solicitation, competitor, or proprietary data.

| Fixture | Used by |
|---|---|
| `fixtures/synthetic-rfp.md` | `shredding-solicitations`, `outlining-proposals`, and any eval needing a solicitation with Sections L, M, and a PWS |
| `fixtures/synthetic-proposal-section.md` | `reviewing-color-teams`, `drafting-proposal-sections`, `checking-submission-compliance` — a drafted section with seeded defects |

Many evaluation scenarios describe inputs the tester supplies directly (a
described opportunity, a competitor list). Those need no fixture file. Build
additional synthetic fixtures as new evaluations require them; never use real
procurement data.

## Result record template

Record each run as a Markdown file in `evaluations/results/` (git-ignored),
named `<skill-name>-<eval-number>-<date>.md`:

```markdown
# Eval result: <skill-name> — Eval <n>

- Date: <date>
- Skill version / commit: <git short SHA or version>
- Model: <model used>

## Checks

| Check (from Expected / Anti-behavior) | Pass/Fail | Note |
|---|---|---|
| <bullet 1> | | |
| <bullet 2> | | |

## Verdict

<PASS — all checks passed | FAIL — list the failed checks>

## Observations

<Anything noteworthy about how the skill behaved — for feeding back into skill
refinement per CONTRIBUTING.md.>
```

## Using results to refine skills

When an evaluation fails, follow the refinement loop in `CONTRIBUTING.md`:
diagnose the cause (description mis-trigger, missing workflow step, reference
file too deep, vague instruction), fix the smallest thing, and re-run the
evaluation. Keep the result records so the before/after is visible.
