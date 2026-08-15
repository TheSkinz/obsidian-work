---
type: review
status: resolved
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
- [x] Rejected
- [ ] Needs more research

**B. Build it as a soft signal on the Commercial pipeline table in `50-dashboards/health.md` instead, not as a lint rule.** `vault_health.py` already reads quote frontmatter for this exact table; adding a folder-freshness column there keeps the check in the place quote anomalies already surface, and a health-dashboard row degrading to "unknown" or "check" on a sync/offline false positive reads as a soft prompt rather than a lint error blocking a commit. Matches the inbox note's own lean ("may belong on the health dashboard as a soft signal rather than in lint as a rule").

- [ ] Approved
- [x] Approved with edits
- [ ] Rejected
- [ ] Needs more research

**C. Do not build either yet — the value comparison against `extract_workup.py`'s reconciled total (the inbox note's third bullet) should wait for the pre-send gate half of the quotation-workup reconciliation build (held manual per that note's Apply Log, pending the scope-narrowing rule), so building the note-vs-folder check now would duplicate work once that gate exists.** Narrower version: build only the existence/recency half now (A or B, minus the value-reconciliation bullet), defer the value-comparison bullet to ride on the pre-send gate when it's built.

- [ ] Approved
- [x] Approved with edits
- [ ] Rejected
- [ ] Needs more research

## Risks and Counter-Arguments

Option A's risk is the one the source note names: a missing OneDrive path, an unsynced folder, or a laptop offline all look identical to a genuinely stale note under an existence/mtime check, and lint is currently a 0-errors gate — a rule that can false-positive on machine state, not content, is a worse fit for lint's binary pass/fail than for a dashboard row. This is the strongest argument for B over A. Option B's risk is dilution: the Commercial pipeline table already carries one FAIL condition (validity-date expiry) with a clear remediation; adding a second, differently-shaped signal (folder freshness) to the same table raises the chance a real FAIL is scanned past. Option C's risk is that it leaves the exact failure mode that motivated the inbox note — a confident, well-formed, wrong note — open for however long the pre-send gate work stays parked; the source note argues this failure mode is worse than an acknowledged gap because it actively misleads rather than reading as unknown. All three options share one mitigant already available: this is a single quote note class (`type: quote`), currently four open rows on the pipeline table, so even a fully manual check ("does the folder match the note") costs Jesse a few minutes per pending quote if neither A nor B is built.

## Decision

**Resolved 2026-08-15 (Jesse, in session). A rejected. B approved, narrowed by C — built as a soft signal on the health dashboard, existence and recency only.**

**A is rejected on the risk the note itself names as strongest.** A missing OneDrive path, an unsynced folder and a laptop offline are indistinguishable from a genuinely stale note under an existence/mtime check, and lint is a binary 0-errors gate that cannot carry a maybe. POINTER-DEAD gets away with reaching into OneDrive because existence is the *whole* of its claim and it base-gates to silence elsewhere; a content-comparison rule inherits the reach without inheriting that certainty. Putting a probabilistic signal behind a gate that blocks commits is the wrong shape.

**B carries C's narrowing.** The value-comparison bullet is deferred to the quotation-vs-workup pre-send gate, which reads the workup's reconciled total rather than guessing from filenames — that is the right owner for it, and building a filename-based approximation now would be thrown away when the gate lands. What shipped is existence and recency only.

**On C's own risk** — that deferring leaves the confident-and-wrong failure mode open — the narrowing does not actually leave it open. The recency half is what catches the DSP26095 case: that note was wrong precisely because its folder had moved on while the note had not, which is a recency signal, not a value signal. The value comparison would have caught it too, but it was not needed to.

**What it does.** `bid_folder_signal()` in `tools/vault_health.py` resolves the note's own recorded bid-folder paths via `vault_lint.POINTER_RE`, base-gates on the first three path components exactly as POINTER-DEAD does, takes the newest file mtime in the folder, and compares it against the leading date of the note's `verified:` value. Five outcomes: `-` (base absent, nothing judged), `no bid folder path recorded`, `folder empty or unreadable`, `newest artifact <date> — note carries no verified date`, `artifacts newer than verified (<date>)`, or `ok`. It renders as a sixth column on the Commercial pipeline table with a paragraph above it saying plainly that it is a soft signal and why it is not lint.

**It found two real gaps on its first run**, neither of which was the case that motivated the note: [[DSP26080]] records no bid-folder path at all, and [[DSP26039]] carries no `verified:` date against a folder whose newest artifact is 2026-05-12. Both were invisible to every existing check.

**On B's dilution risk** — a second differently-shaped signal on a table that already carries one FAIL condition — the mitigation is that this column never reads FAIL. The pipeline's FAIL remains validity expiry alone, and the new column's worst state is a sentence telling you to go look. If it turns out to be scanned past anyway, the fix is to hoist it into the metrics table as a count, not to make it a gate.

## Apply Log

| Date | Action | By |
|---|---|---|
| 2026-08-15 | Ruled and applied. Added `_verified_day()` and `bid_folder_signal()` to `tools/vault_health.py`, extended `pipeline_rows()` to a 6-tuple, and added the Bid folder column plus its explanatory paragraph to the Commercial pipeline section. Reuses `vault_lint.POINTER_RE` and `body_lines_outside_fences` rather than re-implementing path extraction, and copies POINTER-DEAD's three-component base gate verbatim so portability behaviour is identical. Regenerated `50-dashboards/health.md`; verified the recency branch actually executes (DSP26085 verified 2026-07-27 → ok, DSP26095 verified 2026-07-28 → ok, both reached via the comparison rather than an empty-folder short-circuit). No lint rule added. | Claude (review queue) |
| 2026-08-10 | Note filed by pre-staging loop from `00-inbox/2026-07-28-quote-notes-go-stale-against-their-own-bid-folder.md`. Checked for existing coverage: the quotation-vs-workup reconciliation build (resolved 2026-07-27/29) compares different documents on a different axis and does not cover this; the baseline-staleness-detector (resolved 2026-08-01) is an unrelated domain (regression fixtures) that only matched on the word "staleness." Found and cited one correction to the source note's own framing: POINTER-DEAD already reaches outside the vault into OneDrive (existence-only), so the proposed check is an extension of an existing mechanism, not new ground. `50-dashboards/decision-queue.md` checked — not already queued. No vault or config-repo content modified beyond the source marker. | Claude (pre-staging loop) |
