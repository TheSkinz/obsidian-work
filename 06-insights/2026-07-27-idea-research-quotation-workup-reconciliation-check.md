---
type: review
status: resolved
review_type: idea-research
source_authority: inferred
confidence: medium
created: 2026-07-27
review_after: 2026-08-27
revisit-trigger: "A quotation-vs-workup gap appears that is NOT an exact mob/demob multiple (DSP26026-style scope narrowing) -> rule what distinguishes legitimate narrowing from an error, then the pre-send gate can run unattended (approved-with-edits 2026-07-29) — event: check at bid submission"
related:
  - "[[idea-quotation-workup-reconciliation-check]]"
  - "[[2026-07-25-quotation-workup-reconciliation-scan]]"
  - "[[idea-fallback-regression-battery]]"
  - "[[vault-idea-loop-spec]]"
tags: [review, knowledge-system, idea-research, estimating, data-quality]
---

# Idea Research — Standing Quotation-vs-Workup Reconciliation Check

## Trigger

Scheduled nightly run of the Vault Idea Research Loop. Three `unexplored` idea-seeds existed;
`idea-pig-actuals-maturation` (created 2026-07-25 12:44:58) was processed the previous run
(2026-07-26). Of the remaining two, `git log --diff-filter=A` puts `idea-quotation-workup-reconciliation-check`
first (2026-07-25 18:16:38, vs. `idea-rollup-per-rig-coilset-grain` at 22:34:36) — this seed
was processed. The seed carries a **Gate:** line ("Do not build a scheduled sweep before deciding
the trigger question above"), but that gate restricts *building*, not researching — the "To
explore" section explicitly asks the loop's exact question, "what is the right trigger?" So this
is case (b): no gate blocks research, and the research itself is what the gate is asking for.

## Evidence

**1. The two generator defects the source scan called "NOT applied, Lane 4, awaiting Jesse" are already fixed — same day, before the seed was even filed.** `06-insights`-adjacent note `00-inbox/2026-07-25-quotation-workup-reconciliation-scan.md` flags (a) `extract_workup.py` presenting the workup's internal mob/demob cost as the quotable figure with no confirmation prompt, and (b) the "LINE ITEMS DO NOT RECONCILE" flag firing on healthy contract-capped jobs. Config-repo commit `677d447` ("mob/demob is a contract-capped lump sum, not a derived figure (Jesse 2026-07-25)") applied both fixes at **17:42:21** — 34 minutes *before* the idea-seed's own commit at 18:16:38. Confirmed directly in `~/.claude/skills/usadebusk-estimating/scripts/extract_workup.py`: mob/demob now emit `CONFIRM` flags (lines ~545) alongside prepared-by/valid-until/markup, and a `_is_lump_sum_gap()` check (lines ~468–498) reports an exact-multiple-of-mob/demob gap as expected, not blocking. The seed's "Tentative read" inherited these as open items from the scan note; they are closed and need no further action from this idea.

**2. The seed's exact open question — recurring vs. event-triggered — was already decided once in this vault, for a structurally identical fork.** `idea-fallback-regression-battery` (created 2026-07-19, `status: executed`) asked whether a regression check "should ever become recurring or stay a one-shot," listing the same options this seed lists (fold into an existing loop vs. run only on a triggering event). It was built as `~/.claude/regression/` — six fixtures with frozen reference outputs, replayed **after skill edits or a model switch**, not on a schedule (confirmed by the four separate 2026-07-24/07-25 replay sessions in `change-log.md`, each triggered by a specific skill/model change, never a calendar tick). This is direct internal precedent for the seed's own first candidate ("after any `usadebusk-estimating` script edit"), and it already covers the mechanism question the seed treats as unresolved.

**3. A trigger-based harness for exactly this comparison already exists — this is an extension, not a new build.** `~/.claude/skills/usadebusk-estimating/scripts/backtest_workup.py` already runs `extract_workup.extract()` against known-good workup/quotation pairs on demand (manually invoked after changes, per commit `a4ed96f`'s "CANON and LEGACY roots" split). A standing reconciliation check is a small extension of this existing script — add a step that also parses the *quotation's* totals and diffs against the workup's, reusing the mob/demob exclusion rule already implemented — not a new tool.

**4. The seed's "Rendering docx→PDF via LibreOffice is the slow step; a text-extractable path would be better if one exists" question has a concrete, verified answer: skip the render entirely when the source is a `.docx`.** `render_proposal.py` builds every generated proposal as a native `python-docx` `Document` with real tables (`doc.add_table(...)`, confirmed at 7 call sites), not an image or flattened layout. `python-docx` (and lighter single-purpose tools like `docx2csv`) read table cell text directly from the `.docx` zip/XML with no rendering step and no LibreOffice dependency at all — this is standard, well-documented practice, not a novel technique. The LibreOffice conversion the scan's Method Note flags as slow and flaky (per-file wait required; back-to-back `soffice --convert-to` calls silently drop files) is only necessary for quotations that exist **solely as PDF** with no `.docx` source — true of some older/legacy submissions, not of anything the generator itself produces or of any quotation still held as `.docx`. The fix is conditional: read `.docx` directly via `python-docx` when available; fall back to PDF text extraction (still no LibreOffice needed for a text-layer PDF — only scanned/image PDFs would need OCR) only when no `.docx` exists.

**5. External — no off-the-shelf reconciliation tool fits this narrow use case, as expected; the closest external frame reinforces the same trigger-timing conclusion from outside the vault.** Searched for existing quotation-vs-workup / commercial-document reconciliation tooling — nothing addresses this specific shape (bespoke financial-document diffing against an internal cost workbook). The closest applicable software-engineering pattern is **golden-master / approval testing** (Michael Feathers' technique for characterizing legacy behavior): capture current output as a baseline, diff future runs against it, and the established practice is to re-run the diff **when the thing under test changes**, not on a fixed calendar — the same conclusion reached internally in point 2, from an independent source.

## Interpretation

**Sound, but the seed's central open question is already answered by precedent, and part of its inherited context is stale.** The recurring-vs-triggered fork this seed frames as needing a decision was already made once in this exact vault (point 2) with a result that generalizes cleanly to this case, and it agrees with both the seed's own first candidate and the external golden-master convention (points 2 and 5) — three independent lines pointing the same direction. The two "unresolved" generator defects the seed's tentative read carries forward from the source scan are closed (point 1) — not a research finding so much as a note that the seed's premise needs a light refresh before Jesse acts on it. The one genuinely new, concrete finding is point 4: the slow LibreOffice step the scan flagged as a possible improvement has a direct fix, not just a "maybe something better exists" — and it's a fix that reduces the cost of *either* a recurring or an event-triggered version, so it doesn't itself resolve which cadence to pick, just makes both cheaper.

## Recommended Action

**Bounded one-shot build, not a scheduled sweep** (the seed's own gate is satisfied — build as event-triggered): extend `backtest_workup.py` (or a thin sibling script sharing `extract_workup.extract()`) to run (a) automatically after any edit to `usadebusk-estimating/scripts/*` — mirroring the fallback-regression-battery's already-adopted pattern — and (b) optionally as a manual pre-send gate on a single pair at bid submission, per the seed's second candidate. Implementation notes worth carrying in: read the quotation via `python-docx` directly wherever a `.docx` source exists, reserving PDF/LibreOffice handling for docx-less legacy submissions only; reuse the already-applied mob/demob exclusion and multi-block-per-page summation logic (both already in `extract_workup.py`/the 07-25 scan's method notes) rather than re-deriving them; still needs Jesse's call on the DSP26026-style "legitimate scope narrowing" rule (item 1's open question in the seed remains genuinely open — a large non-mob/demob gap needs a human rule, not just a size threshold, before this can run unattended).

## Decision

- [ ] Approved — build as event-triggered (post-script-edit + optional pre-send gate)
- [x] **Approved with edits** — Jesse, 2026-07-29
- [ ] Park — revisit later (state new trigger)
- [ ] Drop

**The edit: split the build in two and ship only the half that can run unattended.**

**Superseded same day — see the correction below. The regression half needed no build.**

~~Build now — the **post-script-edit regression half**. Extend `backtest_workup.py` (or a thin
sibling sharing `extract_workup.extract()`) to fire after any edit to
`usadebusk-estimating/scripts/*`, mirroring the already-adopted fallback-regression-battery
pattern. Read the quotation's tables via `python-docx` directly wherever a `.docx` source exists;
reserve PDF text extraction for docx-less legacy submissions, and do not reintroduce the
LibreOffice render step. Reuse the mob/demob exclusion and multi-block-per-page summation logic
already in `extract_workup.py` rather than re-deriving them.~~

### Correction — 2026-07-29, before any code was written

**`backtest_workup.py` already *is* the quotation-vs-workup reconciliation.** Its docstring states
the expected values are "the SUBMITTED side, read from the submitted PDFs," and `check()` asserts
the line items, the grand total, the Pricing Summary box, and that the lines sum to the total,
exiting non-zero on divergence — across all three pairs. That is the diff this seed proposed
building. Evidence point 3 above said "an extension, not a new build" and was right, but
understated it: the extension is approximately nothing.

**The frozen-constant design is also the better one here**, so the `python-docx` note does not
apply to this half. Live-parsing the quotation on every run would make the regression depend on a
docx parser that can itself break, and it cannot catch a workup and quotation that are wrong in
the same direction. Golden-master wants frozen expectations. The `python-docx` finding stands for
the **pre-send gate**, where the quotation has no frozen expectation yet — that is its correct
home.

**The one real gap is a hook map entry, not a tool.** `usadebusk-fixture-replay-guard.mjs` maps
`usadebusk-estimating` to fixtures `f1` and `f6`, the estimating-judgment fixtures. Nothing maps a
staged edit to `usadebusk-estimating/scripts/*` onto `backtest_workup.py`, so editing the
extractor does not prompt a replay of the suite that covers it. That is a map entry and a runner
branch.

Hold — the **pre-send gate stays manual**, invoked deliberately on a single pair, until the
DSP26026-style scope-narrowing rule exists. A large non-mob/demob gap needs a human rule, not a
size threshold, before anything gates a bid submission unattended. Carried as this note's
`revisit-trigger`.

Not carried forward: the two `extract_workup.py` defects this note's seed inherited from the
2026-07-25 scan. Config commit `677d447` fixed both on 2026-07-25, 34 minutes before the seed was
filed. They are closed and are not part of this build.

## Apply Log

| Date | Action | By | Notes |
|---|---|---|---|
| 2026-07-29 | Approved with edits — post-edit regression half approved to build; pre-send gate held manual pending the scope-narrowing rule | Jesse (ruling) / Claude (Opus 5) | Walked through in session. Cadence question settled by the `~/.claude/regression/` precedent — event-triggered, not scheduled. **Build not yet written** — filed to `00-inbox/` as a build task. |
| 2026-07-29 | **Regression half withdrawn before implementation — it already exists.** Recon of `backtest_workup.py` on Jesse's "should we build it?" found the reconciliation already implemented against all three pairs. Scope reduced to a hook map entry. | Claude (Opus 5) | No code written. The approval was acted on by checking the target first; the research note had not verified what the existing back-test already covered. |
