# Evaluations: shredding-solicitations

## Eval 1 — Atomic requirements and cross-walk

**Scenario:** A user provides an RFP with Sections L, M, and a PWS and asks for a compliance matrix.

**Inputs:** A synthetic RFP in `source/`.

**Expected behavior:**
- Splits compound instructions into atomic, separately verifiable requirements.
- Assigns each requirement a stable ID citing its source section/paragraph.
- Populates the L ↔ M ↔ C cross-walk where requirements span the triad.
- Extracts the format and submission register as a separate labeled section.
- Writes `10-compliance-matrix.md`.

**Anti-behavior:**
- Does not leave compound multi-part instructions as single rows.
- Does not invent requirements or soften a "shall" to a "should".

## Eval 2 — L/M conflict is flagged, not resolved

**Scenario:** The RFP's Section M evaluates a "transition approach" but Section L gives no instruction telling offerors where to address transition.

**Inputs:** A synthetic RFP with the L/M gap.

**Expected behavior:**
- Detects the gap during the cross-walk and flags it.
- Suggests it as a question for the contracting officer.
- Does not pick an answer and proceed as if the gap were resolved.

**Anti-behavior:**
- Does not silently guess where transition should go and hide the ambiguity.

## Eval 3 — Incomplete document set

**Scenario:** The user provides Section C and Section L but not Section M, and asks for a full compliance matrix.

**Inputs:** Partial solicitation.

**Expected behavior:**
- Shreds what is available.
- States explicitly that Section M is missing and the matrix is therefore incomplete.
- Does not present the partial shred as complete.

**Anti-behavior:**
- Does not fabricate Section M evaluation factors.
