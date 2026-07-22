---
type: build-spec
status: active
created: 2026-07-21
source-idea: [[idea-job-report-generator]]
back-test: [USA26038, USA25025]
tags: [spec, fieldpm, automation, cross-cutting, job-report]
---

# Job-Report Generator — Build Spec

Specification produced from `00-inbox/idea-job-report-generator.md`, forks resolved with Jesse
2026-07-21.

> [!done] Built and validated 2026-07-21. The generator lives in
> `~/.claude/skills/usadebusk-fieldpm/scripts/` (`extract_ticket_breakdown.py` +
> `render_job_report.py`), wired behind `/report`. It reproduces the shipped USA26038 report
> exactly (per-heater pig/smart, operating 207, stand-by 74, pigs 298 + full matrix, 6-page
> layout). **Rig is pooled at project level** (Jesse's decision — rigging is fungible). Open:
> the USA25025 input-structural stress test is **blocked** — its workbook isn't on the system
> (McPherson not in OneDrive; likely retired GDrive). The multi-heater-per-pumper boundary stays
> untested until a second workbook is available.

## Why

The USA26038 report shipped, but building it took four tools and three hand-offs: a one-off
docx-js script → Word edits → Claude-in-Word mangled the flow tables → python-docx repair. The
*numbers* were the easy part (per-heater hours, pig counts, stand-by, KPIs all extracted cleanly
from the ticket breakdown and self-reconciled). The friction was owning the format and moving
data into it. A generator that owns the settled format and pulls data from where it already
lives removes the rebuild-from-scratch and the fragile Word round-trip from every future report.

This is cross-cutting work — it applies to every job report, not one facility.

## Architecture — a transfer step in the document-lineage chain

Jesse's governing model:

```
heater drawings → heater card → quote → job sheet → job report
```

Each document inherits the prior and adds a layer. **The job report ≈ the job sheet + actuals +
narrative + flow tests.** The generator is therefore not a standalone report-builder; it is the
`job sheet + actuals → job report` transfer step.

It inherits the **job sheet** (already vault-native markdown, e.g.
`02-facilities/HF-Sinclair/Artesia-NM/USA26038-job-sheet.md`) as the static skeleton — crew,
project details, heater coil data, as-quoted plan — and overlays three layers:

| Layer | Source |
|---|---|
| Actuals — hours by task per heater, pig counts, stand-by, dates, KPIs | ticket-breakdown xlsx |
| Narrative — deposit localization, decoking analysis, project summary/close | PM-supplied prose |
| Flow tests — before/after RPM/PSI at constant GPM | field flow sheets (PDF/image), transcribed |

Inheriting the job sheet *reduces* the generator's job versus the seed's "pull heater data from
cards" framing: most static content is already in the job sheet, which already inherited the
card and quote. The heater card is consulted only for physical facts the job sheet doesn't carry.

### Convergence with the workup-to-proposal generator

Not one monolith, not two unrelated tools. **Shared "structured-source → branded-docx" render
core + shared brand/layout library, two separate mapping front-ends:**

- proposal generator = `quote / heater-card → proposal` transfer step
- job-report generator = `job sheet + actuals → job report` transfer step

Same inheritance pattern, separate mapping specs. Prove each transfer step alone against its own
back-test before merging the render cores. See [[idea-workup-to-proposal-generator]].

## Feasibility (forks resolved 2026-07-21)

- **Ticket-breakdown xlsx is the same template every job** (INPUT + per-shift DAY/NIGHT tabs +
  SUMMARY). One mapping-spec covers all jobs — the high-feasibility branch. This is the green light.
- **Extraction + aggregation already exist and are proven.** The `usadebusk-fieldpm` `/extract`
  command, `references/extraction-format.md`, and the aggregation rules (per-heater hour splits
  read from each shift's pumper→heater ticket-note line; pig aggregation by size/type across all
  shifts) worked and self-reconciled on USA26038. The generator reuses this logic — it is not new.
- **Flow tests: accept current inputs.** Crews handwrite on blank DeBusk templates on site; Jesse
  holds the result as a PDF/image and can pre-extract before hand-off. No field-process change is
  forced. Phase-2 option below.

## Load-bearing design rules

1. **The generator owns all tables and layout. The PM only ever hand-edits prose paragraphs.**
   Table changes happen by editing inputs and re-running — never by hand-editing a table in Word.
   This single rule would have prevented the USA26038 flow-table breakage.
2. **Never fabricate flow data.** Render what exists; mark a missing post-decoke (AFTER) column as
   a gap, do not curve-fit it to look realistic. On USA26038 missing AFTER columns were fabricated
   "to a realistic curve" — that is a data-integrity defect the generator must not reproduce.
   (Consistent with the fieldpm "never guess illegible fields" rule.)
3. **Output/editing model: generate final + polish prose only.** Recommended over regenerate-on-
   every-change. The generator emits a complete .docx; the PM edits only prose paragraphs in place.
   This is what keeps the fragile Word round-trip from returning.

## Settled format — the refined layout (target)

Verified section-for-section against the shipped `USA26038_Job Report…2026-07.pdf`. This is the
golden-master format; the stale `report-structure.md` (cover-page-first, with a Timeline table)
is superseded and reconciled to this as part of this work.

**Running header (every page):** UD logo left; right block `JR-DCK-<FAC><JOB> | REV <n>` over
`<service> | <N> Heaters | <client>`. **Footer (every page):** `USADebusk | Deer Park, TX |
usadebusk.com` … `Page <n>`. No cover page.

| # | Section | Contents |
|---|---|---|
| 1 | Title block | Amber eyebrow (condition-driven, e.g. EMERGENCY MECHANICAL DECOKE); title (facility — heater tags — scope); subtitle line. **Two-row job table** (4 cols): JOB NO / FACILITY / EXECUTION / PROJECT MANAGER — then PO NO / SCOPE / HEATERS / DURATION. **KPI band** (4 stats): Heaters Cleaned · Operating Hours · Pigs Run · Smart-Pig Inspection(s). |
| 1 | Job Summary | Customer Details table (FACILITY / ADDRESS / JOB & PO # / CONTACT); Project Details table (SCOPE / EXECUTION / HEATERS / EQUIPMENT); Crew Details table (PROJECT MANAGER / SHIFT LEAD day·night / DAYSHIFT / NIGHTSHIFT). |
| 2 | Project Duration | Table SCOPE / UNIT / PIG / SMART PIG / SUBTOTAL, one row per heater; **rig pooled** to a single "Rigging (project)" line; then a TOTAL row. Superscript footnotes for delays / as-built reconfig. |
| 2 | Stand-By Summary | Intro sentence; table CAUSE / DATES / HOURS + TOTAL row; combined-total line (operating + stand-by). Stand-by is broken out from operating hours — it is **not** in the KPI operating-hours figure. |
| 2 | Pigs Used | Intro line (size range + legend); **two-column** table SIZE / TC / HR / FOAM / SWAB/HC / TOTAL, aggregated across all shifts and both heaters. |
| 3 | Heater Data and Results | Per heater: amber sub-header; data table (Number of Passes / Total Footage / Convection Tube ID / Radiant Tube ID / Metallurgy / Return Bends / Inlet-Outlet / Smart Pigging); **Result:** paragraph; amber callout box for the critical note. |
| 4 | Flow Tests | Per pass-pair: amber sub-header; table GPM \| BEFORE (RPM/PSI) \| AFTER (RPM/PSI) \| Δ PSI. GPM held constant in the left column; before/after side-by-side; Δ PSI last. |
| 5 | Images | Pig-progression photos; pass-visualization diagram. PM attaches. |
| 6 | Project Summary / Close | Summary prose (what was done, stand-by, field adaptations); Project Close prose; closing block (PM name / USADebusk / Project Manager / Cell / email). |

Render path: python-docx or the `docx` skill. Fonts, colors, table-header/alt-row fills, and
section-header borders come from `usadebusk-core` Brand Standards — do not restate values.

## Mapping — every report line to its source

Sources: **JS** = job sheet · **TB** = ticket-breakdown xlsx · **HC** = heater card ·
**PM** = PM-supplied prose · **FT** = flow-test field sheets · **⚙** = derived/computed by generator.

| Report line | Source |
|---|---|
| Doc-id `JR-DCK-<FAC><JOB>` | ⚙ (prefix + facility code + job no.) |
| REV | PM (default 0) |
| Header subtitle `<service> \| <N> Heaters \| <client>` | ⚙ from JS |
| Eyebrow (EMERGENCY / PLANNED …) | JS project type / condition |
| Title, subtitle | JS (facility, heater tags, scope, location) |
| Job table: JOB NO, PO NO, FACILITY, SCOPE, PROJECT MANAGER | JS |
| Job table: EXECUTION dates | TB (rig-in → demob), cross-check JS |
| Job table: HEATERS (count), DURATION (days) | ⚙ from JS heater list + execution dates |
| KPI: Heaters Cleaned | ⚙ count (JS) |
| KPI: Operating Hours | TB SUMMARY (rig + pig + smart; **excludes stand-by**) |
| KPI: Pigs Run | TB pig total |
| KPI: Smart-Pig Inspection(s) | ⚙ count of heaters with smart pig |
| Customer Details (FACILITY/ADDRESS/JOB&PO/CONTACT) | JS + setup customer contact |
| Project Details (SCOPE/EXECUTION/HEATERS/EQUIPMENT) | JS |
| Crew Details (PM/SHIFT LEAD/DAY/NIGHT rosters) | JS crew assignment; actual mobilized crew from TB |
| Project Duration: SCOPE rows | JS heater list |
| Project Duration: UNIT (which Trimax) | config `pumper_heater` (job sheet) |
| Project Duration: PIG / SMART per heater | TB, attributed by pumper→heater (pumper that pigged that heater) |
| Project Duration: Rigging (project) line | TB, rig-in + rig-out + rig-over summed across all units (pooled — fungible) |
| Project Duration: TOTAL cells + TOTAL row | ⚙ sums |
| Project Duration: footnotes | PM |
| Stand-By Summary: HOURS + DATES | TB stand-by lines |
| Stand-By Summary: CAUSE | PM / shift-summary attribution (TB gives hours, not cause) |
| Stand-By Summary: TOTAL + combined-total line | ⚙ |
| Pigs Used: matrix by size × type | TB pig aggregation (all shifts, both heaters) |
| Pigs Used: intro range + legend | ⚙ (min/max size) + fixed legend |
| Heater Data tables | HC + JS coil data; **as-built passes confirmed by PM** where they differ from quoted |
| Heater Result paragraph + amber callout | PM |
| Flow Tests tables (RPM/PSI before/after) | FT |
| Flow Tests Δ PSI | ⚙ (BEFORE PSI − AFTER PSI at matched GPM) — **only where AFTER data exists; never fabricated** |
| Images | PM attaches |
| Project Summary / Close prose | PM |
| Closing block (PM name/title/cell/email) | JS / setup PM data |

**PM writes:** eyebrow/condition call, footnote text, stand-by cause attribution, as-built pass
confirmation, all Result paragraphs, all callouts, Images, Summary/Close prose, REV.
**Generator produces:** everything else.

## Back-test plan

- **USA26038 — golden-master.** Reproduce the shipped refined report from its ticket-breakdown
  xlsx + `USA26038-job-sheet.md` + the narrative already written, and diff against
  `02-facilities/HF-Sinclair/Artesia-NM/USA26038_Job Report…2026-07.pdf`. Must match
  section-for-section before the generator touches a live job. The numbers are known-good
  (207 operating h, 74 stand-by, 298 pigs, per-heater 89/118 splits) — this validates that the
  generator reproduces the *format and the mapping*, not just the arithmetic.
- **USA25025 — input-structural stress only.** `02-facilities/CHS/McPherson-KS/USA25025-job-record.md`
  is an internal job-record: 9 heaters, routine TA, **flow-test data lost**, carries pricing. It
  cannot be an output golden-master. Use it to prove the mapping/aggregation survives the hard
  shape — 9 heaters, multi-unit (TriMax 1/2) splits, 190 h stand-by across three causes, 396 pigs
  in 26 sizes — and validate the output *structurally* (no golden doc, no flow tests).

## Phase plan

- **Phase 1 — accept current flow inputs.** Generator takes flow data as Jesse hands it over
  (transcribed from field-sheet PDF/image). Ships the whole value of removing the rebuild + Word
  round-trip.
- **Phase 2 (optional) — structured flow-test capture.** A reusable blank structured flow-test
  form for crews (tablet/spreadsheet) so flow data arrives structured, deleting the transcription
  step and the fabrication temptation at its source. This **also closes an already-outstanding
  vault item** — USA25025 open-items call for a reusable blank flow-test sign-off form (2025 data
  was lost). Double duty; bigger, field-process lift; not required for Phase 1.

## Where the build lands

- Generator + mapping spec belong to `usadebusk-fieldpm` (the `/report` command's engine). This
  spec is the reference `/report` implements against.
- `usadebusk-fieldpm/references/report-structure.md` is reconciled to the refined format above as
  part of picking up this idea (it was cover-page-first with a Timeline table — both superseded).
- Render via python-docx or the `docx` skill; brand values from `usadebusk-core`.

## Open decision for the build session

- Authoring vs operating: Fable-authored mapping spec once, then Sonnet/Codex-operated per job?
  Leaning yes — the mapping is now fixed by this document; per-job operation is mechanical.
