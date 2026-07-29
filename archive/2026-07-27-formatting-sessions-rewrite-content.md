<!-- vault-loop: operational — vault_lint.py WORD-DELTA rule and the usadebusk-word-delta-guard.mjs hook, a tooling/governance decision record (tools/, 04-knowledge scope). Defers to the on-demand Agent-Review loop; capture loop cannot write this content. -->
---
type: insight
status: resolved
created: 2026-07-27
resolved: 2026-07-28
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

## Resolved 2026-07-28

**The sweep.** 42 commits audited, selected from all 252 by stated scope — formatting,
reflow, render-drift, lint, schema normalization, layout migration, thinning,
decommission-cleanup, and rename/restructure. Ordinary content and ingest commits were
skipped; they legitimately change words.

**One real finding.** `62cc044` (2026-06-28, "Reconcile heater cards to canonical Task
Durations schema") replaced the `## Pig History` table in `F-301` and `F-371A` with an empty
`## Task Durations` table, dropping its only row with nothing in its place — the same shape as
the F-501 incident, a concurrency fact deleted during a schema pass. The concurrency half had
self-healed by HEAD. Still missing were the pig sequence Foam → Smart Pig and the DSP26039
duration estimate; both were recovered from `archive/F-301_2026-06-22_pre-canonical-schema.md`
into each card's Notes. Reading [[DSP26039]] while restoring them caught a second-order error
the archive row would have propagated: the 24 pig + 8 smart pig figure is the *paired* line
item covering both heaters on one Trimax, not per heater. Both cards now say so explicitly.

**Everything else triaged benign** — metallurgy moved from frontmatter to the geometry table
with every value intact (`b5fda91`), confidence tiers dropped from cards later re-derived and
Jesse-verified (`d7c086c`), F-802's Total 134 → 85 being Stand-By moving out of Total exactly
as that commit said (`72bbaa5`). The pure reformats netted zero words, so the technique
discriminates rather than just alarming.

**Decision: option 1, with a gate.** `tools/vault_lint.py --staged` now carries the check as
rule `WORD-DELTA`, and a third PreToolUse hook — `~/.claude/hooks/usadebusk-word-delta-guard.mjs`
— runs it unprompted before an agent commit. It warns via `additionalContext` and never blocks.

**What the build changed about the design.** The plan called for a gate keyed on the *shape*
of the diff: lost words plus high line churn, the fingerprint of a reflow that also reworded.
Measurement killed it. Across the last 120 commits, firing on any word loss would have hit
**70%**, and firing only on lost numbers or ruling words still hit **50%** — this vault
legitimately rewrites numbers constantly, so no diff-shaped signature separates the dangerous
case. Worse, the churn half was backwards: the F-501 edit had *zero* formatting changes, so a
churn gate would have missed the very case it existed for.

What actually made that session wrong was not the diff, it was that it believed it was only
reformatting. That intent lives in the commit message. Gating on a presentation-only
vocabulary — format, reflow, whitespace, typo, house style, render-drift, and deliberately
*not* schema/migrate/rename/audit/cleanup, which describe content work — drops the fire rate
to **7%** (9 of 120) while still catching `b689150`, the render-drift commit from this very
incident. The lesson generalizes: **an intent-vs-effect check needs the stated intent as
input; it cannot be recovered from the artifact alone.**

Options 2 and 3 were rejected for the same reason as before — both fire only when someone
remembers the session's scope was formatting, and the F-501 session would have passed both,
because it *said* its scope was formatting and believed it.
