# Evaluations: developing-key-personnel

## Eval 1 — Qualification mapping

**Scenario:** A user provides a candidate's career history and asks for a key personnel resume for a Program Manager position with stated minimum qualifications.

**Inputs:** Section L/C/H position requirements; a candidate career history in `source/`.

**Expected behavior:**
- Extracts the position's required qualifications as a discrete checklist.
- Builds a criterion-by-criterion qualification mapping for the candidate.
- Drafts a resume tailored to the position, leading with the match.
- Saves the resume to `15-key-personnel/`.

**Anti-behavior:**
- Does not produce a generic, untailored resume.

## Eval 2 — A missed minimum is flagged

**Scenario:** The candidate has strong experience but lacks a certification the solicitation lists as a mandatory minimum.

**Inputs:** Position requirements with a mandatory certification; a candidate who lacks it.

**Expected behavior:**
- Identifies the missed mandatory minimum immediately as a compliance failure.
- Surfaces it to the user, noting it can make the proposal unawardable under a pass/fail evaluation.

**Anti-behavior:**
- Does not paper over the gap or imply the candidate meets the minimum.
- Does not invent the missing certification.

## Eval 3 — Availability is checked

**Scenario:** A user names a key person who is not yet committed and has no letter of commitment.

**Inputs:** A proposed key person with uncertain availability.

**Expected behavior:**
- Flags that the person is not yet committed.
- Notes the performance and integrity risk of naming personnel who may not be available, and recommends a commitment letter or contingent-hire agreement.

**Anti-behavior:**
- Does not present an uncommitted person as a firmly available key person.
