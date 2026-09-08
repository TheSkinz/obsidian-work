---
type: note
status: resolved
created: 2026-09-02
tags: [CAD26001, syncrude, job-report, handoff, resolved]
resolved: 2026-09-02
---

# Handoff — build the CAD26001 job report

> [!success] Closed 2026-09-02 — report delivered. Two load-bearing claims below were wrong.
> The report was built and delivered the same day. This note did its job: read cold, it carried the
> looping election, the omit-never-annotate rule, the dormant-skill state and the workbook cell
> geometry, none of which the reader would have re-derived. **But two of its central claims did not
> survive contact, and both are recorded here rather than quietly archived, because the failure mode is
> reusable.**
>
> **1. "No ticket-breakdown workbook exists for this job."** It existed. `CAD26001 Syncrude Fort Mac
> 7-1F-1 Bitumen  2 TriMax Ticket Breakdown.xlsx`, in the OneDrive job folder, populated and extracting
> clean. **The search that produced the claim was scoped to the vault**, and the note says so in
> parentheses — but the conclusion was written as if it were about the world. Phase 1 of this handoff,
> a whole `usadebusk-ops` receipt-to-workbook rebuild, did not need doing. **The vault is the index,
> OneDrive is the store: a "does not exist" finding from a vault-only search is a finding about the
> index.**
>
> **2. "The renderer asserts your grouping reconciles to the workbook total, so a wrong guess fails
> loudly rather than silently."** It does not. `build_standby` sums the config's rows into its own
> TOTAL and separately prints the workbook's figure in the grey line beneath; a mismatch renders two
> disagreeing numbers on the same page and exits 0. The only `assert` is in `build_duration`. The
> stand-by grouping had to be reconciled by hand.
>
> Also superseded: the loop location. This note inherited "temporary 180s at the radiant outlet flanges"
> from five vault files. **They went in at the convection inlets.** Corrected everywhere 2026-09-02.
>
> Outcome, all committed: report at `.../Jobs/CAD26001 Syncrude Fort McMurray/CAD26001 Syncrude 7-1F-1
> Job Report.docx`; actuals, `## Coilset Durations`, Field Notes and pig rows on [[7-1-F-1]];
> DSP #CAN24120 recorded on [[CAD26001-job-sheet]].

Written 2026-09-02 to be read cold. Nothing here depends on the session that produced it. The job is finished; the receipts are on Jesse's desktop; the report has not been started.

## Read these first

- [[CAD26001-job-sheet]] — static skeleton: customer/project details, connection points, the looping election, crew roster, PO 1300060001
- [[7-1-F-1]] — tube geometry, metallurgy, prior campaigns (CAD24002 April 2024, CAD25004 September 2025)
- [[CAD26001-flow-tests]] — three measured circuits, plus the post-decoke coil condition Jesse gave on 2026-09-02
- [[active-jobs]] — the CAD26001 row, now under Recently Completed

## It is two phases, and phase 1 is a different skill

There is **no receipts-direct path into the report generator.** The renderer's signature is:

```
python render_job_report.py <job_config.py> <ticket_breakdown.xlsx> <out.docx>
```

The workbook is a required argument and **no ticket-breakdown workbook exists for this job** (confirmed 2026-09-02 — nothing matching `*ticket*breakdown*` anywhere in the vault).

**Phase 1 — receipts → ticket-breakdown workbook.** This is `usadebusk-ops` scope (its Receipt Extraction Process, Steps 1–4, ends at an import-ready table for Ticket Breakdown Excel entry), *not* `usadebusk-fieldpm`. The fieldpm skill says so itself: post-job receipt work is ops's scope.

**Phase 2 — the report.** `usadebusk-fieldpm`, `/report`.

### The workbook geometry is fixed and read by cell address

`extract_ticket_breakdown.py` does not search for headers — it reads known cells. Build the workbook to match or the extractor returns nothing:

- Pumper blocks at **rows 26–35 and 36–45**; labels in **col B**, hours in **col I**
- Stand-by cause in **col L**
- Pigs in **`Q6:R28`**, shift total in **`R29`**
- Shift date in **`C3`**
- Tab names matching `^\s*(day|night)\s*\(\s*\d+\s*\)`

## Reactivating the skill

`usadebusk-fieldpm` is `status: dormant` with `disable-model-invocation: true` — **it will not auto-load and must be invoked by name.** Its frontmatter is stale: it still names USA26038 (demobbed 2026-07-17) as last active, having never been flipped for this job. `SKILL.md:10` instructs verifying the command flow against the current vault workflow on reactivation — do that, and re-set `status: dormant` at the end.

Subagents cannot load it through the Skill tool (`disable-model-invocation` removes it entirely); tell any subagent to read `SKILL.md` from disk instead.

## The retroactive path works — but three things must be rebuilt by hand

No live `/extract` was run during this job. **That breaks nothing.** `/extract` is a payroll-and-email loop feeding `/email`, not a report-feeding loop; the report is fed by the workbook, the job sheet, the heater cards and the flow sheets. The "read back through this conversation thread" line in the `/report` inputs is pre-generator prose, superseded by the Behavior block below it.

What genuinely has to be reconstructed from the receipt stack rather than from a thread:

1. **Stand-by cause grouping** — hours and dates come from the workbook, but the grouping is PM editorial. Read causes out of each receipt's Shift Summary. The renderer asserts your grouping reconciles to the workbook total, so a wrong guess fails loudly rather than silently.
2. **All PM prose** — `result`, `callout`, `project_summary`, `project_close`, `duration_footnotes`, `eyebrow`. Biggest manual lift.
3. **The clean task split** — confirm hours separate cleanly by task at workbook-entry time. If the shift data does not support a clean split, say so in the report rather than allocating hours to make columns add up.

## Flow tests — passes 3+4 must be OMITTED, not rendered

Three of four circuits are real measurements and go in as-is. **Passes 3+4 must not appear in `flow_tests` at all.**

[[CAD26001-flow-tests]] carries `passes-3-4-status: placeholder-not-measured` in its frontmatter. The figures in that section's body are the mean of the other three circuits, standing in until the official sheet is found — they are **not a measurement** and must never be rendered into a customer document.

There is no partial-row option. `build_flow_tests` unpacks a fixed 5-tuple and computes `bpsi - apsi` unconditionally; there is no blank-cell path, so a row with a missing value raises `TypeError`. **Omit the tuple entirely and state the gap in `project_summary` prose.** That is also exactly what the generator spec's *omit, never annotate* rule requires — a suspect pass is left out with no row and no footnote.

Note `flow_tests` is a **required** config key (bracket access, not `.get`); `[]` renders a bare heading, omitting the key raises `KeyError`.

## Config specifics for this job

- `pumper_heater`: both `Trimax5` and `Trimax6` map to the same heater tag — single heater, two units. The extractor accumulates into the same heater dict, so this is fine and the roaming-pumper boundary does not apply.
- Keep the default `rig_unit_label` of `"Both units"`; rig is pooled at project level.
- **Render to a new path every time.** The renderer refuses to overwrite, deliberately — a delivered report gets hand-edited and a re-render destroys those edits. Never `--force` a file Jesse has open.

## Also in scope for that session — DQ-017 Phase 2

[[7-1-F-1]] has **no `## Coilset Durations` section.** The canonical exemplar added it 2026-08-21 and this card was never migrated, so **the CAD26001 actuals have nowhere to land until it exists.** The capture sheet at [[cad26001-coilset-capture-sheet]] targets that section and names the two rows to write (one per rig, Mode 2, Circuit ft 4,474).

Hard constraint: **never add a second table inside `## Task Durations`** — `tools/estimating_rollup.py` parses it as additional duration rows.

The coil condition in [[CAD26001-flow-tests]] also still needs carrying to the heater card's Field Notes: all eight coils nominal and consistent with historical run times, thickest deposits about 1/8" in the radiant tubes and removed easily on the first 6.25" oversized pig, light residual confined to radiant tubes 29–31 in select coils. Tubes 29–31 is **this heater's recurring signature, not a CAD26001 finding** — CAD24002 recorded the same three tubes.

## This report is the first live test of three changes made 2026-09-02

Say so if something behaves oddly, so a failure is read as a new rule not landing rather than as a report bug:

1. The generator spec's **omit, never annotate** rule for suspect flow-test passes.
2. **Completion criterion 3 demoted to corroborating** — effluent duration and sustained clarity carry the determination; Δ PSI confirms it.
3. The `passes-3-4-status` frontmatter marker keeping placeholder figures out of the deliverable.

## One standing rule that governs the whole report

**Flow-test reliability caveats never appear in a customer document, in any form, ever** (Jesse, 2026-09-02). About 60% of projects carry a flow-test error, usually one aspect of one pass, usually minor. The report omits a suspect pass; it does not explain one. The reasoning lives in [[business-normal-facts]] and stays internal.
