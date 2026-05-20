---
name: analyzing-debriefs
description: Prepares for and analyzes a US Federal procurement debrief. Use when the user needs to request a debrief, prepare debrief questions, analyze a government debrief, conduct win/loss analysis, or capture lessons learned from a federal bid. Structures the debrief request, interprets what the government said about the evaluation, and turns it into lessons that feed future bid/no-bid and capture decisions.
---

# Analyzing Debriefs

Close the loop on a pursuit. After award (win or lose) the government's
debrief is the single best source of truth about how the proposal was actually
evaluated. Most teams underuse it: they request it late, ask weak questions, or
read a loss debrief through sour grapes. This skill helps request the debrief
properly, interpret what the government said, and convert it into lessons that
make the next bid better.

## When to use this skill

Use this skill after a federal award decision, in two modes:

- Before the debrief: to request it on time and prepare strong questions.
- After the debrief: to analyze what the government said and capture
  win/loss lessons learned.

Use it for wins as well as losses. A win debrief reveals what worked and where
the proposal was weaker than its score suggested — both valuable.

## Inputs

**Before the debrief:**
- The award notification and the solicitation (for the debrief rules).
- The pursuit workspace artifacts — `01-bid-decision.md`, `05-win-strategy.md`,
  `20-color-review-*.md` — so questions target what the team most needs to learn.

**After the debrief:**
- The government's debrief content (the written debrief, slides, or notes from
  an oral debrief).
- The same pursuit workspace artifacts, to compare what the team believed
  against what the government found.

Read `../../shared/glossary.md`,
`../../shared/federal-solicitation-primer.md`, and
`../../shared/pursuit-workspace.md` if not already read this session.

## Intake

Ask these as a numbered list.

1. **Mode.** Is this preparing to request a debrief, or analyzing a debrief
   already received?
2. **Outcome.** Won or lost? If lost, is the awardee known?
3. **Timing.** When was the award notification received? (Debrief request
   windows are short and strict — see the method file.)
4. **Debrief type.** Is the debrief written, oral, or a combination? What did
   the government provide or schedule?
5. **What the team wants to learn.** What are the open questions — why the
   proposal scored as it did, how it compared, what the deciding factors were?

## Workflow: requesting a debrief

```
Debrief Request:
- [ ] Step 1: Confirm the debrief rules and the request deadline
- [ ] Step 2: Draft a timely debrief request
- [ ] Step 3: Prepare focused debrief questions
```

**Step 1: Rules and deadline.** From the solicitation and the award notice,
confirm the debrief rules and (critically) the deadline to request a debrief.
The window is short. Use `references/debrief-method.md`. A debrief requested
late may be denied, and a timely debrief can affect other downstream timelines.

**Step 2: Request.** Help draft a prompt, professional written request within
the deadline.

**Step 3: Questions.** Prepare focused questions: how the proposal was
evaluated against each Section M factor, the strengths and weaknesses
identified, and (within what the government may disclose) how it compared and
the basis for the award decision. Good questions are specific and tied to the
evaluation factors; vague questions get vague answers.

## Workflow: analyzing a debrief

```
Debrief Analysis:
- [ ] Step 1: Capture what the government said, factor by factor
- [ ] Step 2: Compare government findings to the team's own view
- [ ] Step 3: Separate observations from possible protest issues
- [ ] Step 4: Extract win/loss lessons learned
- [ ] Step 5: Write the analysis (30-debrief-analysis.md)
```

**Step 1: Capture.** Record what the government said, organized by Section M
factor: the strengths, weaknesses, significant weaknesses, and deficiencies it
identified, its ratings, and (to the extent disclosed) the comparison and the
award rationale. Capture it factually, in the government's words, before
interpreting.

**Step 2: Compare.** Set the government's findings against the team's own view
— the win strategy, the Red Team's findings (`20-color-review-*.md`), the
bid/no-bid rationale. Where did the government agree with the Red Team? Where did
it find something the reviews missed? Where did a believed discriminator fail to
score? The gaps between what the team thought and what the government found are
the richest lessons.

**Step 3: The protest boundary.** A debrief sometimes surfaces something that
looks like a procurement irregularity. This skill **does not provide legal
advice and does not assess protest merit.** If the debrief suggests the
evaluation may not have followed the stated criteria or the solicitation, the
skill flags it plainly as a matter for contracts counsel and notes that protest
deadlines are short — it does not advise whether or how to protest. That
decision belongs to counsel.

**Step 4: Lessons learned.** Extract concrete, reusable lessons. For each, name
what to do differently and which future activity it changes — a bid/no-bid
criterion, a capture action, a proposal practice, a pricing posture. Avoid sour
grapes: a loss attributed entirely to bad luck or an unfair government teaches
nothing. Be as honest about a win's weak spots as about a loss's.

**Step 5: Write.** Write `30-debrief-analysis.md` using
`templates/debrief-analysis.md`.

## Output

One artifact: `30-debrief-analysis.md` in the pursuit workspace — the captured
debrief, the comparison, any flagged counsel item, and the lessons learned.

Present the user with: the headline reasons for the outcome, the most important
gaps between the team's view and the government's, any item flagged for counsel,
and the top lessons for the next pursuit.

## References

- `references/debrief-method.md`: debrief rights and timing, preparing questions, reading a debrief, win/loss lessons, and the protest boundary.
- `templates/debrief-analysis.md`: the debrief analysis artifact template.

## Guardrails

- **Mind the deadline.** Debrief request windows are short and strict. When
  helping request a debrief, lead with the deadline.
- **No legal advice.** This skill does not assess protest merit or advise
  whether to protest. It flags possible irregularities for contracts counsel and
  notes that protest timelines are short. Counsel decides.
- **Capture before interpreting.** Record the government's actual words first;
  analyze second. Do not reshape what the government said into what the team
  wishes it had said.
- **No sour grapes.** A loss explained away as bad luck produces no lesson. Find
  the controllable factors.
- **Lessons must be actionable.** Every lesson names what changes and where —
  otherwise it is a feeling, not a lesson.
