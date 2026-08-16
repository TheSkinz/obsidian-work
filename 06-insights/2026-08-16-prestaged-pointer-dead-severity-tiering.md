---
type: review
status: open
review_type: pre-staged
source_authority: inferred
confidence: medium
created: 2026-08-16
related:
  - "[[2026-08-01-pointer-dead-is-mis-tiered]]"
  - "[[2026-08-10-prestaged-quote-note-bid-folder-staleness]]"
tags: [review, knowledge-system, lint, health-dashboard, data-quality]
---

# Review — Should POINTER-DEAD be pulled out of the generic lint-warning backlog?

## Trigger

Pre-staging loop run 2026-08-16, processing `00-inbox/2026-08-01-pointer-dead-is-mis-tiered.md` — the oldest unprocessed candidate carrying the `vault-loop:` marker without a `vault-prestaged:` marker.

## Source Material

| Source | Authority | Notes |
|---|---|---|
| `00-inbox/2026-08-01-pointer-dead-is-mis-tiered.md` (read this run) | Observed | Records the 2026-08-01 DSP26071 folder-move incident: three POINTER-DEAD warnings were open, all real, two dead since 2026-07-23 (nine days unnoticed) — DSP26080's pair recorded `Jobs\` while the folder was still under `Bids\`, H-2501 named a nonexistent parent folder. Argues the failure isn't detection (lint caught all three) but that a caught finding in the generic warning bucket has no path to anyone's attention. Also notes the trigger shape: pointers go stale on OneDrive reorg events (award moves Bids→Jobs, cleanup), which cluster rather than decay — a check timed to a reorg event would catch a batch. Explicitly not proposing a fix. |
| `tools/vault_lint.py:16-26` (rule table, read this run) | Observed | POINTER-DEAD is listed as `warning` severity, grouped in the same tier as REVIEW-OVERDUE, SUPERSEDED, DURATIONS-HEADER, TUBE-GEOM-HEADER, LINK-FACILITY and WORD-DELTA/CHECKBOX-DELTA. Only SECRET, CONF-CONFLICT and YAML-COMMENT are errors (exit 1). Unchanged since the rule shipped in `708c6ba` (2026-07-23) through the current `2bfa95e` self-test rebuild — no commit has touched its tier. |
| `tools/vault_lint.py:868-907` (`check_pointer_dead`, read this run) | Observed | Confirms the mechanism: resolves a backticked absolute path from `02-facilities` notes only, base-gates on the first three path components (skip silently if the machine doesn't have that drive/root), flags if the full path doesn't resolve. Existence-only — matches the source note's description exactly. |
| `50-dashboards/health.md:9-10` (Vault Health metrics table, read this run, 2026-08-16) | Observed | `Lint warnings \| 51 \| (backlog) \| ok` — a single undifferentiated count across every warning-tier rule, always `ok` regardless of composition. Confirms the note's core complaint is still current, fifteen days after the incident: nothing on the dashboard distinguishes "51 warnings, none urgent" from "51 warnings, three are live broken bid-trail pointers." |
| `tools/vault_health.py:563` (Notes section, read this run) | Observed | States plainly: "Lint warnings are the standing to-do list (provenance-frontmatter backfill, stale `related:` links), not failures." That framing is accurate for most of the warning tier (ORPHAN, OP-FRONTMATTER-style backlog) but the note's argument is that POINTER-DEAD doesn't fit it — a dead pointer to a customer's quote/workup folder is not backlog, it's a broken bid trail that happens to have decayed silently. |
| `06-insights/2026-08-10-prestaged-quote-note-bid-folder-staleness.md` (DQ-010, read this run, `status: resolved`) | Observed | Adjacent but distinct: built `bid_folder_signal()` as a **soft-signal column on the Commercial pipeline table**, comparing a quote note's `verified:` date against its bid folder's newest artifact mtime — a content-recency check scoped to `type: quote` notes. It explicitly reuses POINTER-DEAD's base-gating and `POINTER_RE` but does not touch POINTER-DEAD's own severity tier or its treatment in the aggregate "Lint warnings" count. Does not cover heater cards (H-2501, one of the two 2026-08-01 dead pointers, is not a `type: quote` note and never appears on the Commercial pipeline table). Confirms this inbox item is not already covered by DQ-010 — different axis (recency-of-content vs. existence-of-path) and different scope (quote notes only vs. all `02-facilities` pointers). |
| `tools/vault_health.py:87-105, 539-553` (dormant-trigger registry, read this run) | Observed | An existing per-note mechanism (`revisit-trigger:` frontmatter, some machine-checkable via `[machine: …]` tokens) surfaces wake-up conditions on the dashboard. It is note-scoped and manually authored per note, not an aggregate or event-driven check over the whole `02-facilities` tree — doesn't already provide what the source note's "check after a reorg" idea describes. |
| `git log --oneline -i --grep="severity"` and `--grep="pointer-dead"` (checked this run) | Observed | No commit since POINTER-DEAD shipped (`708c6ba`, 2026-07-23) mentions tiering, severity, or escalating it. The only post-ship POINTER-DEAD-adjacent commit is DQ-010's bid-folder signal, already distinguished above. |
| `50-dashboards/decision-queue.md` (checked this run) | Observed | Three open rows (DQ-016 through DQ-018), none address lint-warning severity tiering or POINTER-DEAD specifically. Not already queued. |

## The Question

Should POINTER-DEAD (and any future rule of the same shape — a caught finding that means a live broken reference rather than cosmetic backlog) get a distinct, always-visible surface on `50-dashboards/health.md` instead of folding into the single undifferentiated "Lint warnings" count — or is the existing 0-errors lint gate plus periodic manual review of raw lint output (how the source incident was actually caught) sufficient given three real hits found once in roughly four weeks of the rule's existence?

## Proposed Change

**A. Promote POINTER-DEAD from `warning` to `error` severity in `tools/vault_lint.py`.** Folds it into the existing 0-errors commit gate alongside SECRET/CONF-CONFLICT/YAML-COMMENT, guaranteeing it can never sit unnoticed the way it did for nine days — any commit made after a folder move that breaks a pointer fails immediately.

- [ ] Approved
- [ ] Approved with edits
- [ ] Rejected
- [ ] Needs more research

**B. Keep POINTER-DEAD at warning tier, but give it its own row on `50-dashboards/health.md`'s metrics table (count of live POINTER-DEAD findings, target 0, FAIL if nonzero) instead of folding into the generic "Lint warnings" backlog count.** Mirrors how Dormant triggers and Pending quotes already get their own dedicated rows rather than being absorbed into a generic bucket. Non-blocking (doesn't touch the commit gate), but makes the count impossible to scan past on the one dashboard Jesse actually reads.

- [ ] Approved
- [ ] Approved with edits
- [ ] Rejected
- [ ] Needs more research

**C. No new mechanism — narrower framing of the source note's own event-shape observation: add a one-line reminder to the folder-move / award (Bids→Jobs) procedural step (wherever that's documented) to run `vault_lint.py` and check POINTER-DEAD output before closing out the reorg, since staleness clusters at that exact event rather than decaying gradually.** Cheapest option; treats this as a procedural gap rather than a tooling gap.

- [ ] Approved
- [ ] Approved with edits
- [ ] Rejected
- [ ] Needs more research

## Risks and Counter-Arguments

Option A's risk: escalating to error severity means any future POINTER-DEAD finding blocks every commit touching that note until fixed, including ones unrelated to the pointer — that's a meaningfully bigger lever than the incident justifies (three findings, all real, but all found and fixed the same day once someone looked). It also changes behavior for every machine that doesn't have the OneDrive root mounted differently than intended today: the base-gate already silences it there, but on the machine that *does* have the base path, a stale pointer anywhere in `02-facilities` would now hard-block unrelated work elsewhere in the vault, which is a much larger blast radius than the two facility notes actually affected. Option B's risk is the one DQ-010's Apply Log already names for a structurally identical choice: a soft-signal row that never reads FAIL can be scanned past exactly like the aggregate count it replaces — the mitigation there was "hoist to a count if it turns out to be scanned past anyway," so B is arguably that fix arriving before the miss rather than after it. Option C's risk is that it relies on the moving-folder procedure being followed and documented somewhere discoverable in the first place; the source note doesn't identify one, and a procedural reminder that lives nowhere concrete is not meaningfully different from the current "someone reads raw lint output" status quo that already failed to catch this for nine days. A fourth possibility not raised by the source note — leave it exactly as-is — is defensible on the numbers alone: three findings in roughly four weeks, all caught by the existing rule, all fixed same-day once surfaced; the gap is attention, not detection, and the source note's own framing ("not proposing a fix") suggests it may have been filed as an observation rather than a request for one.

## Decision

*(Pending — Jesse to review.)*

## Apply Log

| Date | Action | By |
|---|---|---|
| 2026-08-16 | Note filed by pre-staging loop from `00-inbox/2026-08-01-pointer-dead-is-mis-tiered.md`. Checked for existing coverage: DQ-010's bid-folder recency signal (resolved 2026-08-15) is adjacent but covers a different axis (content recency vs. path existence) and narrower scope (`type: quote` notes only, not heater cards); the dormant-trigger registry is note-scoped and doesn't provide an aggregate or event-driven check. Grepped `git log` for prior severity/tiering work on POINTER-DEAD — none found since the rule shipped 2026-07-23. `50-dashboards/decision-queue.md` checked — not already queued. No vault or config-repo content modified beyond the source marker. | Claude (pre-staging loop) |
