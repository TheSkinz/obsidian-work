---
type: review
status: open
review_type: pre-staged
source_authority: inferred
confidence: medium
created: 2026-07-28
review_after: 2026-08-27
related:
  - B-101
  - B-151
  - knowledge-system-governance
tags: [review, knowledge-system, data-integrity, git, obsidian]
---

# Review — Should the vault add a guard against silent content-reverting saves?

## Trigger

Pre-staging loop run 2026-07-28, processing the oldest unprocessed inbox item carrying a `vault-loop:` marker: `00-inbox/2026-07-19-stale-editor-buffer-overwrite-vector.md`. That note documented a 2026-07-19 incident where `B-101.md` sat uncommitted carrying an exact content reversal of commit `57ae83e`, disguised by simultaneous Obsidian table auto-formatting. It closed with three open questions and a fourth, explicitly deferred, sibling question — this review covers the three.

## Source Material

| Source | Authority | Notes |
|---|---|---|
| `00-inbox/2026-07-19-stale-editor-buffer-overwrite-vector.md` | Observed | Full incident writeup: B-101.md reverted `Max pig OD` from confirmed (4.026" ID) back to pre-confirmation approximate (~4.03" ID) and deleted the "Resolved (2026-07-07)" Field Notes paragraph. `git diff -w` was what isolated the content change from formatting noise; plain `git diff` did not. |
| `02-facilities/Suncor/Montreal-QC/B-101.md` (current, read this run) | Observed | Confirmed clean against the corrected state: `Max pig OD (in)` row still reads "confirmed ID 4.026\" → max pig OD ≈ 4.276\"", and the "Resolved (2026-07-07)" paragraph is present. `git status`/`git diff -w` on the file show no working-tree divergence. The specific incident is not currently live — the note's own "Disposition at capture time" already recorded it as deliberately left uncommitted pending Jesse's call, and it resolved to the correct state without further action needed here. |
| `02-facilities/Suncor/Montreal-QC/B-151.md` (current, read this run) | Observed | Still carries the approximate value (`ID ~4.03"`, `Max pig OD ≈ 4.28"`) — confirmed as the inbox note's own footnote predicted ("not a regression... its approximate value is its genuine committed state"). The question of whether B-151 deserves the same BOM-based confirmation B-101 got is real but explicitly out of scope for this review (the source note calls it "a separate, unhurried backlog question"). |
| `04-knowledge/knowledge-system-governance.md` (searched this run) | Observed | No existing mention of a content-vs-formatting diff gate, stale-editor-buffer risk, or an Obsidian auto-format policy. The question is genuinely unaddressed, not already covered. |
| Prior-session working memory (this loop's operator context) | Observed | `git diff -w` before committing vault edits was already adopted as standing practice following this incident — i.e. the manual-discipline mitigation is already in force. What remains open is whether that's sufficient or whether a mechanical gate/policy change is also warranted. |

## The Question

The stale-buffer hypothesis itself was never confirmed (the source note calls it "consistent with all the evidence, but not proven"), and confirming it would need editor-session history no longer available — that thread is likely dead. What remains live and decidable: given one observed silent-revert incident, camouflaged by Obsidian's table auto-formatting, should the vault add a mechanical safeguard beyond the manual `git diff -w` habit already adopted — either a diff-gate check or disabling auto-format outright — or is the manual habit sufficient given the incident's low observed frequency (one instance to date)?

## Proposed Change

### A. Build a content-vs-formatting diff gate (session-startup or pre-commit check)

A `git diff -w --stat` based check, run at session start or as a pre-commit hook, that flags any working-tree change to `02-facilities/` or `04-knowledge/` where the whitespace-insensitive diff is non-empty — separating real content regressions from formatting-only churn automatically, rather than relying on a human remembering to run `-w` by eye.

- [ ] Approved
- [ ] Approved with edits
- [ ] Rejected
- [ ] Needs more research

### B. Disable Obsidian's table auto-format for the vault

Removes the camouflage mechanism at the source. The source note observes this format churn has "only real function here was camouflage" and has separately generated recurring noise commits (e.g. `f36de3d`, "Reformat F-802 table alignment").

- [ ] Approved
- [ ] Approved with edits
- [ ] Rejected
- [ ] Needs more research

### C. No new mechanism — the adopted `git diff -w` habit is sufficient

One observed incident in the vault's history to date, already caught by manual discipline, with `HEAD` never actually at risk (nothing was lost in either direction — the note's own disposition left B-101 uncommitted rather than reverted). A build/config investment may not be justified by a single low-frequency incident.

- [ ] Approved
- [ ] Approved with edits
- [ ] Rejected
- [ ] Needs more research

## Risks and Counter-Arguments

Option A adds a mechanical check to a system Jesse has previously pushed back toward "propose-only, low ceremony" (2026-07-03 policing-pattern rejection) — worth weighing whether this is the same shape of over-automation or a narrowly-scoped, justified exception (data-integrity, not content policing). Option B is a broader UX change than the incident strictly requires — it affects every future edit, not just the risk window, and Obsidian's auto-format may have value Jesse hasn't weighed in trade. Option C risks recurrence: the manual habit depends on remembering to run `-w`, which is exactly the step that was originally skipped and let the 2026-07-19 incident go unnoticed until an unrelated close-out review caught it.

The B-151 question (does it deserve the same ID confirmation B-101 got) is real but is a heater-card content decision, not a systems question — it belongs in a separate ask if Jesse wants it queued, not bundled into this one.

## Decision

Open — awaiting Jesse's disposition on A/B/C above.

## Apply Log

| Date | Action | By |
|---|---|---|
| 2026-07-28 | Note filed by pre-staging loop from `00-inbox/2026-07-19-stale-editor-buffer-overwrite-vector.md`; no vault content modified beyond the source marker | Claude (pre-staging loop) |
