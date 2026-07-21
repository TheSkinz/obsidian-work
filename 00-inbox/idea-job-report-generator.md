---
type: idea-seed
status: unexplored
created: 2026-07-21
tags: [idea, fieldpm, automation, cross-cutting]
---

# Job-report generator

Idea seed captured 2026-07-21 after the USA26038 job report. The read below is tentative —
confirm intent with Jesse before designing.

**Tentative read:** The job report is the post-job twin of the [[idea-workup-to-proposal-generator|workup-to-proposal generator]]
— same "structured Excel → formatted document" machine, just driven by the ticket-breakdown
xlsx instead of the estimate work-up. On USA26038 the *numbers* were the easy part: per-heater
hours, pig counts, stand-by, crew, dates, and KPIs all extracted cleanly from the
ticket-breakdown workbook and reconciled to the summary total. The friction was everything
around the data — the report format was hand-built as a one-off docx-js script, then edited in
Word, then Claude-in-Word mangled the flow tables, then repaired with python-docx (four tools,
three hand-offs, one breakage). A generator that owns the settled format and pulls its data
from where it already lives would remove the rebuild-from-scratch and the fragile Word
round-trip from every future report.

**Data-source map (from USA26038):**
- **Numbers** (hours by task per heater, pig counts by size/type, stand-by, crew, dates, KPIs)
  → ticket-breakdown xlsx. Stable structure: INPUT + per-shift DAY/NIGHT tabs + SUMMARY;
  per-heater split recoverable from each shift's pumper→heater ticket-note line. Proven
  extractable and self-reconciling this session.
- **Heater Data section** (tube IDs, metallurgy, passes, footage) → vault heater cards.
- **Narrative** (deposit localization, decoking analysis, as-built config, project
  summary/close) → PM-supplied; cannot and should not be automated, but can be templated with
  good defaults + prompts.
- **Flow tests** → today the weakest link: photographed handwritten sheets, often with missing
  post-decoke columns that had to be *fabricated* to a realistic curve, in a specific
  before/after + Δ-PSI layout. Highest error surface in the whole report.

**Settled format:** the refined CHS/26038 layout — no cover page; running header with
[logo] + JR-DCK doc-id; KPI band; two-row job table; Job Summary; Project Duration (UNIT
column + footnotes); Stand-By Summary (broken out); two-column Pigs table; Heater Data +
Result + amber callouts; Flow Tests (before/after side-by-side, GPM constant, Δ PSI); Project
Summary/Close. Live exemplars: CHS `USA25025-CHS-McPherson…-Job Report` and the finished
USA26038 report.

**Load-bearing design rule (learned the hard way):** the generator owns *all tables and
layout*; the PM only ever hand-edits *prose paragraphs*, never tables. Table changes happen by
editing inputs and re-running. This single rule would have prevented the flow-table breakage.

**To explore:**
- Is the ticket-breakdown xlsx structurally stable across jobs (clean one-session mapping-spec)
  or reshaped per job? Same feasibility fork as the proposal generator — ask, don't guess.
- The cell/card → report-line mapping, including per-heater hour splits and pig aggregation
  (both worked programmatically on USA26038 — reuse that logic).
- Root cause of the flow-test pain: could crews capture flow data in a simple structured form
  (tablet spreadsheet) instead of handwritten-sheet photos? That deletes the transcription +
  fabrication step entirely. Bigger lift (field-process change) but it's the actual source.
- Output/editing model: generate-final-and-polish-prose-only (recommended) vs regenerate on
  every change. Determines whether the Word round-trip fragility returns.
- Does this converge with the workup-to-proposal generator into one "Excel → document" tool?
- Back-test set: USA26038 and CHS McPherson both have full source data — prove the generator
  reproduces both finished reports before it touches a live job.
- Authoring vs operating: Fable-authored mapping spec once, then Sonnet/Codex-operated?

Related: [[idea-workup-to-proposal-generator]].
