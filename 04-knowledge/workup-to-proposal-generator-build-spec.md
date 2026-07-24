---
type: build-spec
status: active
created: 2026-07-23
source-idea: [[idea-workup-to-proposal-generator]]
source-review: [[2026-07-23-idea-research-workup-to-proposal-generator]]
back-test: [DSP26071.2, DSP26085, DSP26068.1]
related:
  - job-report-generator-build-spec
  - rfq-intake-protocol
  - quote-lifecycle
tags: [spec, estimating, automation, cross-cutting, workup-to-proposal]
---

# Workup-to-Proposal Generator — Build Spec

Specification produced 2026-07-23 from [[2026-07-23-idea-research-workup-to-proposal-generator]]
(approved, back-tested) and the deferred build brief [[2026-07-23-deferred-workup-proposal-build-spec]].
Mirrors [[job-report-generator-build-spec]]. The mapping below is proven against three
structurally different real pairs.

> [!done] Built and validated 2026-07-24. The generator lives in
> `~/.claude/skills/usadebusk-estimating/scripts/` (`extract_workup.py` mapping front-end +
> `render_proposal.py` branded-docx renderer + `proposal_input_template.py` optional config +
> `backtest_workup.py` regression harness), wired into the `usadebusk-estimating` SKILL.
> **Regression PASSED:** all three submitted totals reproduced EXACTLY, line-item by line-item and
> Pricing-Summary-box row by row — DSP26071.2 $60,287.42, DSP26085 $40,477.08, DSP26068.1
> $112,642.23 — read against the submitted PDFs (DSP26085 rendered docx→PDF via LibreOffice). A
> fourth workup (DSP26075, Fixed Price + Training + `Decoke Only:` subtotal) validated the
> reconciliation path as a bonus. Rendered drafts were visually confirmed against the submitted
> quotations (branding, line items, hour-breakdown sub-line, Pricing Summary box all match).
> All four open decisions below are resolved. See the resolution notes inline.
>
> **Key architecture discovery:** the `Insert Quote` tab is the pre-built customer quotation,
> **fully formula-linked to the work tab** — it carries the line-item prose, the Pricing Summary
> box (already resolved to values), prepared-by, bill-to, special instructions and footer. The
> generator reads amounts from the work-tab Project Financials block (the spec's proven mapping)
> and prose/box/header from the `Insert Quote` tab, then reconciles the two — catching any desync
> (and the stale-paste errors frozen into the old image-pasted quotations, e.g. DSP26085's
> submitted image shows quote # "26000" while the live workup is 26085).

## Why

Every bid is built in an Excel workup, then its pricing is hand-carried into a Word proposal and
converted to PDF. That transcription recurs on every bid and is where a transposition error would
enter a six-figure quote. A generator that reads the finished workup and emits the proposal's
commercial content removes the step from every future bid. Cross-cutting — applies to every
proposal, not one facility.

Confirmed during this spec's back-test: current proposals carry the pricing as **Excel ranges
pasted into Word** (EMF/PNG in the docx; DSP26085 has no text-extractable totals in its docx at all).
That is *why* a generator adds value — it emits real, correct, text-based tables instead of pasted
screenshots — and it is also why the back-test had to read the submitted **PDFs**, not the docx.

## Architecture — a transfer step in the document-lineage chain

Governing model (shared with the job-report generator):

```
heater drawings → heater card → quote → job sheet → job report
```

This generator is the **`workup xlsx → proposal docx` transfer step**. It converges with the
job-report generator as **one shared "structured-source → branded-docx" render core + shared
brand/layout library, two separate mapping front-ends** (this one = workup → proposal; the other =
job sheet + actuals → job report). Prove each front-end against its own back-test before merging
render cores — this note is this front-end's proof.

**Where it lands:** `usadebusk-estimating` (parallel to the job-report generator in
`usadebusk-fieldpm`). Render via python-docx / the `docx` skill; brand values from `usadebusk-core`.

## What the workup feeds (and what it does not)

The workup produces the proposal's **commercial** content only:

| Proposal section | Source |
|---|---|
| **7 — Quotation** (line items, total, Pricing Summary box) | workup financials block + header |
| **9 — Hourly Charge-Out Rates** | workup master bill-rate table |
| **3 — Requested Service** (scope/basis header) | workup header block |
| 4 — Execution Plan | duration model (not the workup) |
| 5 — Technical Data | heater card |
| 6, 10–14 | boilerplate |

Sections 4/5/6/10–14 are inherited from elsewhere and out of this front-end's scope — the generator
composes them but does not derive them from the workup.

## Source structure (confirmed across 3 workups)

Consistent tab set: `Insert Quote` · **work tab (varies)** · `Pricing Table` · `Execution` ·
`Heater Data`. The work tab name is job-specific (`Full Conv+TG+ Rad`, `F-201`, `1 Heater`) and a
workup may carry **multiple pricing-scenario tabs** (DSP26071.2 has `Full Conv+TG+ Rad` **and**
`Conv + Treat Gas Only`).

Work-tab regions (old-style exemplar, per `Workup-Template-v1-design.md`):

| Region | Location | Role |
|---|---|---|
| Header | `B2:C8` (+`A1`, `A8`) | date, quote #, type, facility, address, bid, scope |
| **Project Financials** | `H1:K~9` | Mob/Equip/Labor/Per Diem/[Training]/Materials/Demob/Total — **rev = col I**, cost = col J, margin = col K |
| Duration strip | `A14:K25` | per-heater task hours (rig-in/pig/smart/rig-out) |
| Master bill rates | `I43:K59` (dup `D43:F59`) | Section 9 rates |
| Pig catalog | `I62:K75` | pig cost + markup → charge |

## Load-bearing rules (each proven or forced by the back-test)

1. **Locate the work tab by role, not name.** It is the tab not in
   {`Insert Quote`, `Pricing Table`, `Execution`, `Heater Data`}. If more than one remains, pick the
   scenario whose quote # (`C3`) matches the submitted revision — DSP26071.2's `Full Conv+TG+ Rad`
   carries `DSP#:26071.2` and totals $60,287.42 (submitted); `Conv + Treat Gas Only` carries
   `DSP#:26071` and totals $50,631.36 (superseded).
2. **Read the financials block by H-column LABEL, never by fixed row.** DSP26068.1 inserts a
   `Training:` line, pushing `Total:` from row 8 to row 9. Scan column H for label text
   (`Mob:`, `Equip:`, `Labor:`, `Per Diem:`, `Materials:`, `Demob:`, `Total:`, and any extra e.g.
   `Training:`) and read the revenue value from column I on that row.
3. **Revenue is column I. Column J (cost) and column K (margin) never reach the customer document.**
   The duplicate rate tables (D vs I) and hardcoded cost rates in heater blocks are internal-only.
4. **Round to cents** (workup carries full float: Materials 5094.225 → $5,094.23).
5. **Flag-don't-guess.** An unmatched line, an unresolved markup, or an unidentified Pricing-Summary
   region is surfaced for Jesse — never silently filled or dropped.

## Mapping — Section 7 line items (PROVEN, exact on 3 pairs)

Source tags: **WU-fin** = financials block (col I, by label) · **WU-dur** = duration strip ·
**WU-hdr** = header · **⚙** = computed · **J** = needs Jesse.

| Quotation line | Source | Rule |
|---|---|---|
| `(Lump Sum) Mobilize [equipment list]` | WU-fin `Mob:` | equipment list ⚙ from scope/resource plan |
| `Mechanical Decoke: [heater]` + hour breakdown | WU-fin `Equip:` ; hours WU-dur | breakdown "N Rig-in \| N Pig \| N Smart \| N Rig-out" |
| `Labor & Per Diem` | WU-fin `Labor:` **+** `Per Diem:` | the two are summed into one line |
| `Materials: DEF & Decoking Pigs` | WU-fin `Materials:` | |
| `Safety Training: …` (when present) | WU-fin `Training:` | extra category → its own line, keyed by label |
| `(Lump Sum) Demobilize [equipment list]` | WU-fin `Demob:` | |
| **Total** | WU-fin `Total:` | |
| Header: quote type (T&M / Fixed Price) | WU-hdr `C4` | itemized structure identical either way |
| Header: quote #, facility, address, bid, scope, date | WU-hdr `C3/C5/C6/C7/C8/C2` | also feeds Section 3 |
| Prepared-by name | **J / setup** | varies per job (Travis Trenholm; Jason Harman) — not in financials |
| Valid date | **J** (90-day default) | |
| Third-party markup % | **J** — confirm per contract | never defaulted (skill rule) |

**Needs-Jesse boundary (the human-input stop):** everything above tagged **J** — prepared-by, valid
date, markup confirmation — plus Section 3 scope prose (templated but reviewable) and Section 5
technical/as-built confirmation (from the card). Everything tagged WU-* / ⚙ is mechanical, because
the finished workup already contains every pricing decision Jesse made.

## Pricing Summary box — RESOLVED (open decision #1)

The Section 7 **Pricing Summary box** (Equipment · Manpower · Materials · [Training] · Total) is
**always present in the `Insert Quote` tab**, already resolved to plain values (col D labels, col E
values, ending in a `Total` row). Two derivation styles exist under the hood, which is why it does
not reduce to one formula over the six line items:

- **Old style (DSP26071.2, DSP26085):** the box is computed from the quotation line items —
  Equipment = Mob + Equip; Manpower = Labor + Per Diem + Demob; Materials = Materials. (Mob groups
  with Equipment, Demob groups with Manpower — odd but consistent.)
- **New style (DSP26068.1):** the box reads a genuine per-resource-type **cost rollup** on the work
  tab (`I80:J82`) — Equipment $75,188 (≠ Mob + Equip; e.g. Filter and Rig-in equipment bucketed in)
  — plus a Training row. Note the work-tab rollup even *mislabels* the 4th row "Third Party" while
  holding the Training value; the `Insert Quote` box fixes the label to "Training".

**Resolution: read the box straight from the `Insert Quote` tab and reconcile its Total to the grand
Total — do not re-derive the varying bucketing.** This is version-agnostic and trivial (the box is
already computed there). The generator falls back to the old-style line-item derivation only if the
`Insert Quote` box is absent, and flags that. Reconciled exactly on all four workups.

## Back-test results (this session)

Standard: reproduce the submitted proposal's Quotation line items and grand total 1:1 from the
workup financials block (read via openpyxl; submitted side read from PDF — DSP26085 rendered docx→PDF
via LibreOffice, since its docx pricing is image-embedded).

| Pair | Type | Structure | Workup Total (col I) | Submitted Total | Line items |
|---|---|---|---|---|---|
| DSP26071.2 | T&M | 6-line, Total row 8 | $60,287.42 | $60,287.42 | 1:1 (proven in review) |
| DSP26085 | T&M | 6-line, Total row 8 | $40,477.08 | $40,477.08 | 1:1 ✓ |
| DSP26068.1 | Fixed Price | 7-line (+Training), Total row 9 | $112,642.23 | $112,642.23 | 1:1 ✓ (incl. Training) |

**Verdict: mapping generalizes.** Three structurally different real jobs, every Section-7 line item
and grand total reproduced exactly. The one non-generalizing element (Pricing Summary box bucketing)
is isolated, documented above, and non-blocking.

## Source decision (settled)

Build the mapping against the **old-style workup as it exists today** — proven, multi-heater, in
active use (four confirmed live instances). Treat `Workup-Template-v1.xlsx` (single-heater,
unfinished) as a parallel input-cleanup track Jesse finishes on his own timeline. Do not block the
generator on a template rewrite.

## Open decisions — ALL RESOLVED (2026-07-24 build session)

1. **Pricing Summary box source region — RESOLVED.** Read the already-resolved box from the
   `Insert Quote` tab; reconcile its Total to the grand Total; fall back to old-style line-item
   derivation (flagged) only if the box is absent. See the Pricing Summary box section above.

2. **Multi-heater line items — DETECT-AND-FLAG (split path deferred).** All three back-test pairs
   are single-heater; no genuine multi-heater workup exists in the Facilities tree today (the
   closest, DSP25156's `OLD_` tab, is multi-*event* same-heater and superseded, its `Insert Quote`
   unwired). The generator **detects** a multi-heater workup (duration strip carrying >1 furnace)
   and **flags** it for manual review rather than emitting a single mis-scoped Mechanical-Decoke
   line — mirroring the job-report extractor's UNMAPPED-rather-than-misallocate discipline. The
   per-heater split path (one Mechanical-Decoke line per furnace, read from the `Insert Quote`
   Financial-Summary rows) is designed but stays unvalidated until a real multi-heater workup is
   available. This does not block single-heater jobs (the overwhelming majority of bids).

3. **Mobilize/Demobilize equipment-list prose — RESOLVED.** It is a hardcoded string in the
   `Insert Quote` description column (e.g. "(Lump Sum) Mobilize (1) Trimax Pumper, (1) Support Unit,
   Filtration, Manpower, & Launchers." / "Lump Sum: Mob: (1) Pumping Unit, (1) Support Unit, (1)
   Filter, (1) 4x3 Pump"). The generator reads it verbatim (Mobilize = a description with "mob" but
   not "demob"; Demobilize = has "demob") and falls back to a flagged placeholder if absent. Not a
   J field — the workup already carries it.

4. **Authoring vs operating — RESOLVED: yes.** Mapping authored once (this build, Opus); per-job
   operation is mechanical — `python render_proposal.py <workup.xlsx> <out.docx> [quote#]` — and can
   be driven by a cheaper model (Sonnet/Codex), as with the job-report generator. No config is
   required; the "REVIEW BEFORE SENDING" box carries every human-input decision to Jesse.

## Additional variations found during the build (beyond the 3-pair back-test)

The reconciliation-driven line placement (place the canonical roles, verify they sum to Total, then
any leftover nonzero label is a subtotal/dupe to flag) was hardened against extra financials-block
labels seen in a 4th workup (DSP26075) and DSP25156's tab: `Decoke Only:` (a Total − Training
subtotal), `Third Party:`, `SteadyFlux:`, and quantity-prefixed `(2) Mob:` / `(2) Demob:`. Header
fields are read by label (the `Date:` vs `Due Date:` variation, and the `Scope:` label sitting in
column A with its value in C while B is blank). The Section 9 rate table is variable-length and read
by label-scan (DSP26068.1 has a single `Supervisor` not Day/Night, adds a `750 CFM Compressor` line,
and lands `Mark-up` on a different row).
