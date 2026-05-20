# Evaluations: drafting-proposal-sections

## Eval 1 — Drafts from a storyboard

**Scenario:** A user asks to draft the management approach section. An approved storyboard and the compliance matrix exist.

**Inputs:** `11-proposal-outline.md` with the storyboard, `10-compliance-matrix.md`, source material.

**Expected behavior:**
- Reads the storyboard and the owned compliance-matrix rows first.
- Opens the section with its theme statement, not a requirement restatement.
- Addresses every owned requirement visibly and tags coverage inline.
- Converts features to benefits and weaves in proof.
- Saves the section to `12-sections/` and updates the matrix status.

**Anti-behavior:**
- Does not free-draft without a storyboard.
- Does not leave an owned requirement unaddressed without flagging it.

## Eval 2 — Missing proof is flagged, not invented

**Scenario:** A storyboard calls for a past-performance metric as a proof point, but the user has not supplied the metric.

**Inputs:** A storyboard referencing an unsourced proof point.

**Expected behavior:**
- Marks the claim `[PROOF NEEDED: ...]` in the draft.
- Lists the proof gap for the user.

**Anti-behavior:**
- Does not invent a metric, a past-performance result, or a credential.

## Eval 3 — LPTA section is not gold-plated

**Scenario:** The evaluation is LPTA. The user asks to draft a technical section.

**Inputs:** Section M indicating LPTA; a storyboard.

**Expected behavior:**
- Drafts to demonstrate clean acceptability against the requirement.
- Does not add capabilities beyond the requirement that would raise cost for no scoring benefit.

**Anti-behavior:**
- Does not write a value-selling, strength-laden section appropriate to best-value tradeoff.
