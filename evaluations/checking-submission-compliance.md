# Evaluations: checking-submission-compliance

## Eval 1 — Over-length volume is caught

**Scenario:** A user asks for a final submission check. The technical volume is 62 pages against a 50-page Section L limit.

**Inputs:** The final proposal package and `10-compliance-matrix.md`.

**Expected behavior:**
- Checks each volume's page count against its limit.
- Identifies the over-length technical volume as a failed, go/no-go item.
- Produces an overall NO-GO verdict until corrected.
- Writes `21-submission-checklist.md`.

**Anti-behavior:**
- Does not treat the over-length volume as a minor note.

## Eval 2 — Misplaced price information

**Scenario:** The solicitation requires price information only in the cost volume. A pricing table appears in the management volume.

**Inputs:** The proposal package with the volume-separation violation.

**Expected behavior:**
- Detects the price information in the management volume.
- Flags it as a serious volume-separation failure and a go/no-go item.

**Anti-behavior:**
- Does not pass the package as conforming.

## Eval 3 — Mechanics and deadline

**Scenario:** A user asks for the submission check the afternoon before a noon-Eastern deadline and has not registered for the submission portal.

**Inputs:** The proposal package and Section L submission instructions.

**Expected behavior:**
- Verifies the submission method, destination, and the exact due date/time/time zone.
- Flags the missing portal registration as a blocking item.
- Confirms a submission plan with margin and a backup path.

**Anti-behavior:**
- Does not normalize submitting at the deadline with no margin.
