---
type: capture
status: inbox
created: 2026-07-30
related:
  - [[2026-07-28-prestaged-stale-editor-buffer-guard]]
  - [[2026-07-19-stale-editor-buffer-overwrite-vector]]
tags: [capture, obsidian, data-integrity, git, knowledge-system]
---

# Obsidian expanded an ambiguous wikilink to the wrong facility

Found at session close-out 2026-07-30, in changes that had been sitting uncommitted in the working tree since before the session started.

Obsidian rewrote bare `[[_facility]]` wikilinks to full paths across 23 notes. Inside `02-facilities/` every expansion resolved to the note's own facility folder and is correct — with 12 facility folders each holding a `_facility.md`, the bare link is genuinely ambiguous and the expansion is an improvement.

**One resolved to the wrong facility.** `archive/2026-06-26-cnd25004-candidate-canonical-updates.md` is a Syncrude (Fort McMurray, AB) note; both of its `[[_facility]]` links were expanded to `02-facilities/PBF/Toledo-OH/_facility`. Corrected in commit `1d0e522` to `02-facilities/Syncrude/Fort-McMurray-AB/_facility`. The same commit also removed a stray word inserted mid-sentence in `06-insights/2026-07-28-idea-research-rollup-per-rig-coilset-grain.md` ("extracting structured **up** fields").

## Why this matters

This is the same incident class as the 2026-07-19 `B-101.md` silent revert: an editor altering content alongside benign formatting, where the benign pattern supplies cover for the real change. Twenty-three correct expansions made the twenty-fourth look like more of the same.

**It is a distinct failure mode from the one the approved guard targets.** DQ-003 was framed around content *reverts* — a stale buffer overwriting newer text. This was neither a revert nor a loss: the link stayed well-formed, still resolved to a real note, and passed `vault_lint.py` cleanly (DEAD-LINK only catches links that resolve to nothing, not links that resolve to the *wrong* thing). Only reading the changed line against the note's subject caught it.

Worth deciding whether the guard's scope covers **link retargeting**, not just content loss. A cheap check exists: when a wikilink gains a path prefix, the new path's facility segment should match the note's own `facility:` frontmatter or folder. That would have caught this one mechanically and is narrow enough to avoid the false-positive problem that killed the WORD-DELTA diff-shape gate.

## Open

- Does the approved stale-editor-buffer guard (DQ-003) absorb this, or is it a separate check?
- Are there other pre-existing bare `[[_facility]]` links outside `02-facilities/` that Obsidian has not yet expanded, and would expand wrongly for the same reason? `archive/` and `06-insights/` are the likely places.
