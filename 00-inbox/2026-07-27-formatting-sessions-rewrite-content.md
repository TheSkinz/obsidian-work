---
type: insight
status: unexplored
created: 2026-07-27
tags: [vault-hygiene, verification, agent-behavior]
---

# A "fix the formatting" session rewrote content, and a line diff could not show it

**What happened.** A terminal session asked to fix Obsidian formatting issues left
`02-facilities/ExxonMobil/Baytown-TX/F-501.md` with **zero formatting changes and three
content changes**. It flipped the SOP entry to say Phase II runs *sequentially* (the
opposite of the awarded scope, and contradicted by the card's own Notes two screens
below), deleted `Mode = 3` and the concurrency statement outright with nothing in their
place, and reversed a closed ruling — "this is not an open action / no reissue required"
became "superseded, REV 2 required," turning a decision Jesse had already made that same
day back into a phantom action item on the August TA. Restored in `c63f0ac`.

**Why it hid.** Rewrapping prose changes every line in a paragraph, so a reflow and a
reflow-plus-reword look identical in a line diff. `git diff -w` does not help — it
ignores whitespace *within* a line, but a reworded sentence moves words *across* lines
and reads as genuine content change either way. This is the same family as the reverted
tube-ID confirmation caught on 2026-07-19 (see `00-inbox/2026-07-19-stale-editor-buffer-overwrite-vector.md`),
one level harder: `-w` caught that one, and cannot catch this one.

**The check that works — word-multiset comparison.** Extract all words from the before
and after blobs, compare as counted multisets, ignore line structure entirely. A pure
reformat nets to zero words lost and zero gained. Anything else is real. Script used:
`audit_commit.py` (session scratchpad; ~40 lines, `collections.Counter` + a word regex).

Run against `b689150` — the committed half of the same session — this cleared it:
11 of 14 files pure reformat, and the three that flagged were all benign (H-102A/B were
the documented Max-pig-OD-to-Field-Notes migration with every value intact — 2.900
governing ID, 3.150 computed, 3.125 practical ceiling; H-101 only gained YAML quote
characters). So the technique discriminates, it does not just alarm.

**Worth deciding.** Three options, none taken yet:

1. Fold the word-multiset check into `tools/vault_lint.py` as a staged-diff mode, so it
   runs before any commit that touches prose.
2. Keep it as a manual audit script under `tools/`, invoked when a session's stated scope
   was formatting/cleanup.
3. Make it a rule instead of a tool: any session whose scope is formatting commits with
   `--stat` reviewed and states explicitly that no content changed.

Option 1 is the only one that catches this without someone remembering to look, which is
the actual failure mode — Jesse does not track triggers.

**Open question the incident raises but does not answer:** how many *earlier* "cleanup"
or "formatting" commits in vault history carry the same silent rewrites? The audit is
cheap enough to sweep the whole log. Nobody has run it beyond `b689150`.
