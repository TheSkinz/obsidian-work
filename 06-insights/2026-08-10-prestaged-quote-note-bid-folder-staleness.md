---
type: review
status: open
review_type: pre-staged
source_authority: inferred
confidence: medium
created: 2026-08-10
related:
  - "[[2026-07-28-quote-notes-go-stale-against-their-own-bid-folder]]"
  - "[[2026-07-27-idea-research-quotation-workup-reconciliation-check]]"
tags: [review, knowledge-system, data-quality, estimating, quotes]
---

# Review — Should a quote-note-vs-bid-folder staleness check be built, and where does it live?

## Trigger

Pre-staging loop run 2026-08-10, processing `00-inbox/2026-07-28-quote-notes-go-stale-against-their-own-bid-folder.md` — the oldest unprocessed candidate carrying the `vault-loop:` marker without a `vault-prestaged:` marker.

## Source Material

| Source | Authority | Notes |
|---|---|---|
| `00-inbox/2026-07-28-quote-notes-go-stale-against-their-own-bid-folder.md` (read this run) | Observed | Describes the 2026-07-28 incident: [[DSP26095]] read `status: pending`, "Not yet priced — no rates on file" while its own recorded bid folder already held a finished quotation `.docx`/`.pdf` and a priced workup `.xlsx`. Proposes a check that resolves each `type: quote` note's `## Source Files` path and compares folder contents/recency against the note's claimed status and value. Raises three open questions verbatim: where the check lives (lint vs. health), whether it can be a lint rule at all given sync/offline false positives, and whether it overlaps the pending quotation-vs-workup reconciliation work. |
| `02-facilities/Westlake-Chemical/Westlake-LA/DSP26095.md:1-21` (read this run) | Observed | Current state: `status: pending`, `value: 44415.88`, `verified: 2026-07-28 — figures read from the finalized quotation PDF and the workup`. The specific note is now correct — it was fixed directly the same day, not by any new mechanism. Confirms the incident was a point-in-time staleness window, not a standing defect in this one note. |
| `tools/vault_lint.py:702-741` (`check_pointer_dead`, read this run) | Observed | POINTER-DEAD already resolves recorded absolute `## Source Files` paths and checks `p.exists()`, base-gated so it skips silently on a machine where the OneDrive root isn't present (portability pattern). This directly contradicts the inbox note's own open question ("this check has to reach outside the vault into OneDrive, which no current rule does") — a rule already does, for existence. It does not read directory contents, filenames, or mtimes, and does not compare anything against the note's frontmatter (`status`, `value`). Existence-only, not content-comparison. |
| `50-dashboards/health.md:31-40` (Commercial pipeline table, read this run, 2026-08-10) | Observed | Reads `status`, `valid-through`, `date-execution` straight from quote-note frontmatter only. [[DSP26095]] shows `pending / 2026-09-29 / 2026-09 / execution in 22 d` — no field here is cross-checked against the bid folder. Confirms the gap described in the inbox note is still open as of today, thirteen days after the incident. |
| `06-insights/2026-07-27-idea-research-quotation-workup-reconciliation-check.md` (read this run) | Observed | `status: resolved`, approved-with-edits. Its build compares the **quotation against the workup** (`backtest_workup.py`, already does this on all three known pairs) — an internal consistency check between two documents in the bid folder. It does not compare either document against the **vault note's own claimed status**, which is the axis this inbox item is about. Not the same check; adjacent, not overlapping in mechanism. |
| `06-insights/2026-08-01-idea-research-baseline-staleness-detector.md` (read this run) | Observed | Also `status: resolved`, but a different domain entirely — regression-fixture frozen baselines vs. config/vault commit history (`git log <commit>..HEAD`), no relation to quote notes or bid folders. Ruled out as a false-positive match on the word "staleness"; not applicable here. |
| `50-dashboards/decision-queue.md` (checked this run) | Observed | Four open rows (DQ-006 through DQ-009), none address quote-note-vs-bid-folder comparison. Not already queued. |

## The Question

Should a check be built that compares a `type: quote` note's claimed state (`status`, `value`, `verified:`) against the actual contents of the bid folder its own `## Source Files` path points at — and if so, does it live as a `tools/vault_lint.py` rule (extending POINTER-DEAD's existing base-gated OneDrive reach from existence-only to content-comparison) or as a soft signal on the Commercial pipeline table in `50-dashboards/health.md` (which already reads quote frontmatter and is the place quote-state anomalies currently surface)?

## Proposed Change

**A. Extend `vault_lint.py` — add a new rule alongside POINTER-DEAD that, once the base path resolves, lists the bid folder and flags two conditions: (1) a quotation `.docx`/`.pdf` or workup `.xlsx` bearing the note's DSP number exists but the note's `value` is empty or `status` reads as unpriced language; (2) the newest artifact's mtime is later than the note's `verified:` date.** Reuses POINTER-DEAD's exact base-gating (skip silently when the OneDrive root isn't present on this machine) so it inherits the same portability guarantee for free — this is the smallest version of the check, built on a mechanism that already exists rather than a new one.

- [ ] Approved
- [ ] Approved with edits
- [ ] Rejected
- [ ] Needs more research

**B. Build it as a soft signal on the Commercial pipeline table in `50-dashboards/health.md` instead, not as a lint rule.** `vault_health.py` already reads quote frontmatter for this exact table; adding a folder-freshness column there keeps the check in the place quote anomalies already surface, and a health-dashboard row degrading to "unknown" or "check" on a sync/offline false positive reads as a soft prompt rather than a lint error blocking a commit. Matches the inbox note's own lean ("may belong on the health dashboard as a soft signal rather than in lint as a rule").

- [ ] Approved
- [ ] Approved with edits
- [ ] Rejected
- [ ] Needs more research

**C. Do not build either yet — the value comparison against `extract_workup.py`'s reconciled total (the inbox note's third bullet) should wait for the pre-send gate half of the quotation-workup reconciliation build (held manual per that note's Apply Log, pending the scope-narrowing rule), so building the note-vs-folder check now would duplicate work once that gate exists.** Narrower version: build only the existence/recency half now (A or B, minus the value-reconciliation bullet), defer the value-comparison bullet to ride on the pre-send gate when it's built.

- [ ] Approved
- [ ] Approved with edits
- [ ] Rejected
- [ ] Needs more research

## Risks and Counter-Arguments

Option A's risk is the one the source note names: a missing OneDrive path, an unsynced folder, or a laptop offline all look identical to a genuinely stale note under an existence/mtime check, and lint is currently a 0-errors gate — a rule that can false-positive on machine state, not content, is a worse fit for lint's binary pass/fail than for a dashboard row. This is the strongest argument for B over A. Option B's risk is dilution: the Commercial pipeline table already carries one FAIL condition (validity-date expiry) with a clear remediation; adding a second, differently-shaped signal (folder freshness) to the same table raises the chance a real FAIL is scanned past. Option C's risk is that it leaves the exact failure mode that motivated the inbox note — a confident, well-formed, wrong note — open for however long the pre-send gate work stays parked; the source note argues this failure mode is worse than an acknowledged gap because it actively misleads rather than reading as unknown. All three options share one mitigant already available: this is a single quote note class (`type: quote`), currently four open rows on the pipeline table, so even a fully manual check ("does the folder match the note") costs Jesse a few minutes per pending quote if neither A nor B is built.

## Decision

*(Jesse: check one box per lettered option above.)*

## Apply Log

| Date | Action | By |
|---|---|---|
| 2026-08-10 | Note filed by pre-staging loop from `00-inbox/2026-07-28-quote-notes-go-stale-against-their-own-bid-folder.md`. Checked for existing coverage: the quotation-vs-workup reconciliation build (resolved 2026-07-27/29) compares different documents on a different axis and does not cover this; the baseline-staleness-detector (resolved 2026-08-01) is an unrelated domain (regression fixtures) that only matched on the word "staleness." Found and cited one correction to the source note's own framing: POINTER-DEAD already reaches outside the vault into OneDrive (existence-only), so the proposed check is an extension of an existing mechanism, not new ground. `50-dashboards/decision-queue.md` checked — not already queued. No vault or config-repo content modified beyond the source marker. | Claude (pre-staging loop) |
