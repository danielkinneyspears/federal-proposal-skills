# The Pursuit Workspace

Every skill in this package reads and writes a shared, on-disk workspace for one
opportunity. This is what lets a pursuit survive across many sessions and weeks:
the workspace *is* the persistent memory. A skill never assumes context is still
in the conversation — it reads what it needs from the workspace and writes its
result back.

## Location and naming

One directory per opportunity, under a top-level `pursuits/` directory:

```
pursuits/<solicitation-id>/
```

`<solicitation-id>` is the government's solicitation or notice number when one
exists (e.g., `47QFCA24R0001`), lowercased with non-alphanumeric characters
replaced by hyphens. Before the RFP releases, use a short slug for the
opportunity (e.g., `dhs-cloud-recompete`).

Pursuit workspaces routinely hold competitor analysis, pricing, and customer
intelligence. Treat the workspace as sensitive. Never place classified, CUI, or
source-selection-sensitive material in it unless your organization's policy and
the applicable safeguarding rules allow it.

### Workspace bootstrap — do this before creating any artifact

A pursuit workspace must not end up tracked in version control. This repository
git-ignores `pursuits/`, but when the skills are installed as a plugin and run
inside *another* project, that protection does not travel with them. Before a
skill creates the first artifact in a pursuit workspace, it performs this
bootstrap:

1. **Determine where the workspace will live.** Default to a `pursuits/`
   directory; confirm the location with the user if it is ambiguous.
2. **Check whether that location is inside a git repository.** (For example,
   look for a `.git` directory at or above the workspace path.)
3. **If it is inside a git repository**, either:
   - add `pursuits/` (or the specific workspace path) to that repository's
     `.gitignore` and tell the user it was added; or
   - recommend the user place the workspace outside version control entirely.
   Do not create sensitive artifacts in a tracked location without surfacing
   this to the user first.
4. **If it is not inside a git repository**, proceed, and note to the user that
   the workspace holds sensitive material and should be handled accordingly.

This bootstrap runs once per pursuit, at first workspace creation. A skill that
finds an existing workspace can assume it was done, but should still avoid
writing sensitive material to an obviously tracked location.

## Artifact files

Skills produce numbered Markdown artifacts. The number prefix encodes lifecycle
order, so the directory listing reads as the pipeline state.

| File | Produced by | Phase |
|---|---|---|
| `00-opportunity-profile.md` | qualifying-opportunities | Capture |
| `01-bid-decision.md` | qualifying-opportunities | Capture |
| `02-capture-plan.md` | planning-capture | Capture |
| `03-competitive-assessment.md` | analyzing-competitors | Capture |
| `04-price-to-win.md` | estimating-price-to-win | Capture |
| `05-win-strategy.md` | developing-win-strategy | Capture |
| `06-shaping-response-<type>.md` | responding-to-rfis | Capture |
| `07-teaming-strategy.md` | developing-teaming-strategy | Capture |
| `08-solution-design.md` | developing-solution-approach | Proposal |
| `09-proposal-management/` | managing-proposal-operations | Proposal |
| `10-compliance-matrix.md` | shredding-solicitations | Proposal |
| `11-proposal-outline.md` | outlining-proposals | Proposal |
| `12-sections/` | drafting-proposal-sections | Proposal |
| `13-executive-summary.md` | writing-executive-summaries | Proposal |
| `14-past-performance/` | writing-past-performance | Proposal |
| `15-key-personnel/` | developing-key-personnel | Proposal |
| `16-cost-narrative.md` | narrating-cost-volumes | Proposal |
| `20-color-review-<team>.md` | reviewing-color-teams | Review |
| `23-review-recovery.md` | running-review-recovery | Review |
| `21-submission-checklist.md` | checking-submission-compliance | Submission |
| `22-orals-package.md` | preparing-orals | Post |
| `30-debrief-analysis.md` | analyzing-debriefs | Post |

Source inputs the user provides (the solicitation PDF, past performance library,
resumes, prior proposals) go in a `source/` subdirectory:

```
pursuits/<solicitation-id>/source/
```

## How skills use the workspace

1. **On invocation**, a skill checks whether the pursuit workspace exists and
   reads the upstream artifacts it depends on. If they exist, it uses them
   instead of re-asking the user for that information.
2. **If an upstream artifact is missing**, the skill notes what is missing,
   proceeds with what the user can provide, and records the assumption.
3. **On completion**, the skill writes its artifact with the standard header
   (below) and tells the user which file it wrote.

Skills do not silently overwrite. When re-running a skill, it updates its
artifact following the merge protocol below.

## Updating an existing artifact

Artifacts are long-lived and are often edited by hand between skill runs — a
proposal manager adds a column, fills in an owner, corrects a fact. A skill
re-running over an existing artifact must not destroy that work. When a skill
would write an artifact that already exists, it follows this protocol:

1. **Read the current artifact in full** before changing anything.
2. **Diff the intended changes against it.** Identify what is genuinely new or
   updated versus what is unchanged.
3. **Preserve content the skill does not own.** Keep hand-added columns, notes,
   status values, owners, and any rows or sections the skill did not generate.
   When unsure whether a field was hand-edited, preserve it.
4. **Apply only the intended changes**, leaving everything else intact.
5. **Record a change note.** Update the artifact's `Updated` date and add a
   short line stating what changed in this run (artifacts that carry a change
   log, such as the capture plan, use that log).
6. **Surface conflicts.** If an intended change would overwrite something that
   appears to be deliberate hand-edited content, do not silently override it —
   tell the user and let them decide.

The compliance matrix is the most-shared artifact: `shredding-solicitations`
creates it, and `outlining-proposals`, the drafting skills, and the volume
skills all update specific columns (`Volume & section`, `Owner`, `Status`).
Each of those updates touches only its own columns and preserves the rest.

## Artifact header

Every artifact starts with this header so its provenance and freshness are
visible:

```markdown
# <Artifact title> — <Opportunity name>

- Solicitation: <number or "pre-RFP">
- Customer: <agency / office>
- Skill: <skill-name>
- Updated: <date>
- Upstream inputs: <list of artifact files this was built from>
- Status: <draft | reviewed | final>
```

## Dependency notes

Skills degrade gracefully. `drafting-proposal-sections` is far stronger when
`05-win-strategy.md` and `10-compliance-matrix.md` exist, but it will still run
from the solicitation alone — it just flags that themes are un-validated. Each
skill's `SKILL.md` lists its preferred upstream inputs and what it does without
them.
