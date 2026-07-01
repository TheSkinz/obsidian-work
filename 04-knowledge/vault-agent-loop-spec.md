---
type: governance
status: active
source_authority: primary
confidence: high
created: 2026-06-26
last_reviewed: 2026-06-27
review_after: 2026-07-26
related:
  - [[knowledge-system-governance]]
  - [[vault-source-of-truth]]
  - [[knowledge-review-dashboard]]
  - [[vault-idea-loop-spec]]
tags: [knowledge-system, agent-loop, vault-review, governance]
---

# Vault Agent Loop Spec

This note defines the scheduled command loop for maintaining the USADeBusk Obsidian vault. It turns the proven CND25004 pilot workflow into a repeatable agent loop with strict approval boundaries.

## Loop Name

Vault Review Loop

## Trigger

On-demand only. Run manually after a batch of operational work, or whenever you want the operational core reviewed:

```text
Run the Vault Review Loop on obsidian-work. Pick one safest item and create a review note only.
```

This loop is deliberately **not** scheduled. It governs high-stakes operational content (pricing, SOPs, heater cards) that changes infrequently and should only be reviewed when you are present. The low-ceremony content layer is handled on a schedule by the Vault Capture Loop ([[vault-capture-loop-spec]]); this loop does not perform session harvest and does not run unattended. It runs locally against the working tree — no cloud routine, no separate clone.

## Scope

Canonical vault only:

```text
C:\Users\Jwuts\obsidian-work
```

Before any write, verify the target path starts with the canonical vault path in [[vault-source-of-truth]].

## Governance Scope

This loop governs the **operational core** of the vault:

- `02-facilities/` (heater cards, facility overviews)
- `04-knowledge/` (canonical rules, governance, equipment, SOPs)
- Pricing, SOP, safety, field-execution, and customer-facing content wherever it appears
- `change-log.md`

It does **not** govern `00-inbox/` content routing or the `07-llms/`, `08-systems/`, `09-interests/` content layers. Those are owned by the Vault Capture Loop ([[vault-capture-loop-spec]]). When a harvested item is operational, it routes here under this loop's approval boundaries regardless of which session produced it.

`change-log.md` is a **shared append-only history**. Both loops append their own dated entries; neither edits or removes the other's. This loop logs approved operational changes; the capture loop logs its scheduled run summaries. Single-writer-per-entry, never a shared edit.

## Goal

Improve vault trust, retrieval, and maintenance by finding one small reviewable item per run. The loop should create evidence-backed review artifacts, not silently reorganize the vault.

## Loop Steps

1. Observe current state.
2. Retrieve only the minimum relevant notes.
3. Identify candidate issues.
4. Pick one safest useful item.
5. Create a review, contradiction, or question note.
6. Stop before mutating source/canonical notes unless Jesse has explicitly approved the specific change.
7. Log approved changes after they are applied.

## Observation Targets

Check these areas in order:

| Order | Area | Purpose |
|---:|---|---|
| 1 | `00-inbox/` | Unprocessed source notes and routing candidates. |
| 2 | `06-insights/` | Open reviews, contradictions, and prior loop notes. |
| 3 | `04-knowledge/` | Governance, canonical rules, evaluation questions, stale/due notes. |
| 4 | `02-facilities/` | Only when a specific facility/heater is needed for the selected item. |
| 5 | `change-log.md` | Confirm history before writing or closing a loop. |

Never scan the whole vault deeply unless the selected item requires it.

## Candidate Issue Types

| Type | Create |
|---|---|
| Unprocessed source | Review note. |
| Conflicting claims | Contradiction note. |
| Poor retrieval or missing source | Question note. |
| Stale note or due review | Review note. |
| Candidate facility/heater/job update | Review note first; draft scaffold only after approval or when explicitly low-risk and marked draft/source-derived. |
| Duplicate vault/source-of-truth concern | Review note; no file moves or deletion. |

## Allowed Without Additional Approval

| Action | Limits |
|---|---|
| Read vault notes | Stay within canonical vault unless source evidence requires a referenced local source path. |
| Create review notes in `06-insights/` | Must include trigger, evidence, proposed change, risks, decision checklist, and apply log. |
| Create contradiction notes in `06-insights/` | Must quote or precisely paraphrase the conflicting claims and link sources. |
| Create question notes in `06-insights/` or `04-knowledge/` | Must include expected sources and retrieval failure type. |
| Create draft/source-derived scaffolds | Only when explicitly approved or clearly requested; must be marked `status: draft`, `source_authority: secondary`, and `confidence: medium` or lower. |
| Append to `change-log.md` | Only after a real approved change is applied. |

## Blocked Without Specific Approval

| Action | Reason |
|---|---|
| Delete files or folders | Data loss risk. |
| Archive or move source notes | Routing/source-of-truth impact. |
| Mark draft heater cards as reviewed | Canonical fact promotion. |
| Edit pricing, SOP, safety, field execution, customer-facing, or heater-card facts | Operational risk. |
| Merge conflicting claims | Must preserve contradiction trail. |
| Bulk edit metadata across many notes | Sync and regression risk. |
| Convert this loop to an automated/unattended schedule | Operational core must stay manually triggered and reviewed while present. |

## Selection Rule

Pick one item per run. Prefer the smallest item that improves trust or retrieval. Do not batch unrelated cleanup.

Recommended priority:

1. High-risk contradiction with clear source trail.
2. Inbox item with obvious routing but no canonical edits needed.
3. Open review waiting for evidence gathering.
4. Stale/due governance or canonical note.
5. Retrieval evaluation failure.

## Output Artifact Requirements

Every loop-created review artifact must include:

| Section | Required Content |
|---|---|
| Trigger | Why the item was selected. |
| Evidence | Source notes, paths, dates, and authority. |
| Proposed Action | What should happen next. |
| Approval Boundary | What cannot happen without Jesse approval. |
| Risks / Open Questions | Uncertainty and operational impact. |
| Decision | Checkboxes for approve/reject/needs more source material. |
| Apply Log | Date/action/by after any approved change. |

## Staleness Check Categories

Mined from the claude-obsidian wiki-lint audit, filtered to operational content. Observe-only; flag in the review note, never auto-fix.

| Category | What to flag |
|---|---|
| Dead links | Broken `[[wikilinks]]` or relative paths in `02-facilities/` / `04-knowledge/` notes pointing to renamed or deleted files. |
| Frontmatter gaps | Operational notes missing required fields per `_canonical-heater-card.md` or governance frontmatter (type, status, source_authority, confidence). |
| Stale reviews | `06-insights/` review notes past `review_after`, or with an unresolved Decision checklist older than 14 days. |
| Stale claims | An operational claim contradicted by a newer source note. Create a contradiction note; do not merge. |
| Orphan pages (informational only) | Operational notes with no inbound links. Report count only; do not propose deletion. |

Dropped as non-transferable: semantic tiling (requires ollama + wiki structure), DragonScale address validity, Dataview/canvas dashboard generation.

The scan may surface several issues at once; the loop still creates one review note for the single highest-priority item per the Selection Rule. Un-actioned flags are simply re-detected on the next on-demand run — there is no backlog artifact, and that is acceptable because this loop is manual and infrequent.

## Stop Conditions

Stop and report instead of continuing when:

- The selected item touches safety, pricing, SOP execution, customer-facing content, or heater-card facts and approval has not been given.
- Source authority is unclear.
- The path is outside the canonical vault.
- The same class of failure happens twice.
- Git working-tree or file-existence state is ambiguous (uncommitted conflicts, missing expected files).

## Success Criteria

A successful loop run leaves the vault better by one small increment:

- one review note created,
- one contradiction documented,
- one question/evaluation item captured,
- one approved source routed,
- or one approved draft scaffold created.

The loop is successful even if it stops with a well-documented blocker. It is not successful if it makes broad silent changes.
