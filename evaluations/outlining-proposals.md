# Evaluations: outlining-proposals

## Eval 1 — Structure follows Section L

**Scenario:** A user has a compliance matrix and asks for a proposal outline. Section L prescribes a specific volume and heading structure.

**Inputs:** `10-compliance-matrix.md` and the solicitation Section L.

**Expected behavior:**
- Builds the outline structure to mirror Section L's prescribed volumes, order, and headings.
- Maps every compliance-matrix requirement to exactly one section.
- Annotates each section with factors, theme, proof points, graphic concept, pages, and author.
- Builds a page budget weighted toward high-value Section M factors.
- Writes `11-proposal-outline.md` and updates the matrix "Volume & section" column.

**Anti-behavior:**
- Does not impose a custom structure that departs from Section L.
- Does not leave requirements unmapped (orphans).

## Eval 2 — Storyboards before drafting

**Scenario:** A user says "skip the planning and just write the technical volume."

**Inputs:** A compliance matrix exists.

**Expected behavior:**
- Produces the annotated outline and storyboards first.
- Explains that storyboarding before drafting is the point — it makes each section's strategy explicit while it is cheap to change.

**Anti-behavior:**
- Does not skip straight to drafting narrative.

## Eval 3 — Page budget overflow surfaced

**Scenario:** The requirements assigned to the technical volume cannot plausibly fit in the Section L page limit.

**Inputs:** A compliance matrix with a heavy technical volume and a tight page limit.

**Expected behavior:**
- Builds the page budget and detects the overflow.
- Flags it as a structural problem to solve during planning, and cuts from the lowest-value sections rather than proportionally.

**Anti-behavior:**
- Does not produce a budget that silently exceeds the page limit.
