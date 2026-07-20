<!-- vault-loop: operational — unresolved Lane 4 data-integrity question on B-101.md (02-facilities) plus a proposed change to knowledge-system-governance.md (04-knowledge). Defers to the on-demand Agent-Review loop / Jesse's call; capture loop cannot write this content. -->
---
type: capture
status: inbox
created: 2026-07-19
related:
  - [[B-101]]
  - [[knowledge-system-governance]]
tags: [capture, vault-system, data-loss, git, obsidian]
---

# A stale editor buffer can silently revert committed vault work

Caught during the 2026-07-19 harness close-out. `02-facilities/Suncor/Montreal-QC/B-101.md` sat uncommitted in the working tree carrying an exact reversal of commit `57ae83e` (2026-07-07, "Confirm tube IDs across Suncor Montreal heater cards"):

- `Max pig OD (in)` reverted from `confirmed ID 4.026" → max pig OD ≈ 4.276"` back to the pre-confirmation `ID ~4.03" → max pig OD ≈ 4.28"`.
- The `**Resolved (2026-07-07):**` Field Notes block — the paragraph explaining *why* the IDs were confirmed rather than approximate (every BOM row states "Sch 40", which is sufficient to read exact wall/ID off the standard pipe table) — was deleted entirely.

The same save also applied current Obsidian table auto-formatting to the file, which is what disguised it: `git diff` showed a wall of whitespace realignment, and the content reversal was invisible until `git diff -w` isolated it.

## Why this matters

Max pig OD is a pig-sizing input. The numeric delta is trivial (4.276 vs 4.28) but the provenance delta is not — "confirmed" versus "~approx" decides whether someone trusts the figure well enough to order pigs against it. This is a Lane 4 fact quietly demoting itself with no commit, no author, and no signal.

## Suspected mechanism (unconfirmed)

A stale Obsidian buffer. If B-101.md was open in an editor pane *before* `57ae83e` landed (that commit was made from a different session), and Obsidian later flushed its in-memory copy to disk, the write would reproduce exactly this: pre-07-07 content, plus present-day auto-formatting. Consistent with all the evidence, but not proven — worth confirming before designing a guard.

## Why the existing safety net missed it

Nothing in the vault's automation watches for this. `vault_lint.py` checks schema and links, not whether a fact regressed against its own git history. The loops only inspect files they touch. A dirty working tree carrying a silent revert is invisible until someone reads a `git diff` by eye — and the auto-format noise actively discourages that.

## To explore

- Confirm or kill the stale-buffer hypothesis (was B-101 open in a pane across the 07-07 remote session?).
- Whether a pre-commit or session-startup check should flag working-tree diffs that *remove* content from `02-facilities/` or `04-knowledge/` — a `git diff -w --stat` gate that surfaces content-bearing changes separately from formatting churn would have caught this in one line.
- Whether Obsidian's table auto-format should be disabled for the vault outright. It generates recurring commit noise (`f36de3d`, `[auto] Reformat F-802 table alignment`) whose only real function here was camouflage.
**Checked at capture time — blast radius is one file.** `57ae83e` touched B-101, B-102, B-103, and `_walkdown-summary.md`; all except B-101 are clean against HEAD. B-151 also reads `ID ~4.03`, but that is not a regression — it was never part of the confirmation pass, so its approximate value is its genuine committed state. Whether B-151 deserves the same BOM-based ID confirmation B-101 got is a separate, unhurried backlog question.

## Disposition at capture time

B-101.md deliberately left **uncommitted**. `HEAD` still holds the correct 07-07 version, so nothing is lost in either direction; restoring is `git checkout -- 02-facilities/Suncor/Montreal-QC/B-101.md`. Flagged to Jesse rather than reverted unilaterally — it is domain truth, and the change was not authored by this session.
