# Evaluations: preparing-orals

## Eval 1 — Structured to Section M within the rules

**Scenario:** A task order requires a 30-minute oral presentation followed by 15 minutes of Q&A, with a 12-slide limit submitted in advance.

**Inputs:** The orals instructions, Section M, `05-win-strategy.md`, `12-sections/`.

**Expected behavior:**
- Captures the format, time split, and slide limit.
- Structures the presentation to the Section M factors and allocates time by factor importance, reserving the Q&A block.
- Builds theme-driven content within the 12-slide limit.
- Assigns presenters and writes `22-orals-package.md`.

**Anti-behavior:**
- Does not exceed the slide limit or design a presentation that crowds out Q&A.

## Eval 2 — Q&A is rehearsed

**Scenario:** A user asks the skill to prepare orals and considers Q&A "we'll handle it live."

**Inputs:** A win strategy and competitive assessment.

**Expected behavior:**
- Builds an anticipated-question list drawn from weaknesses, risks, and competitive exposures.
- Prepares a concise, honest answer for each and assigns a responder.
- Plans a Q&A rehearsal drill with a mock panel.

**Anti-behavior:**
- Does not skip Q&A preparation.

## Eval 3 — Presenter restrictions honored

**Scenario:** The orals instructions require all presenters to be proposed key personnel. The user wants a polished business-development executive to present.

**Inputs:** Orals instructions with the presenter restriction.

**Expected behavior:**
- Flags that the BD executive is not eligible to present under the rules.
- Assigns segments to proposed key personnel and prepares them.

**Anti-behavior:**
- Does not assign an ineligible presenter.
