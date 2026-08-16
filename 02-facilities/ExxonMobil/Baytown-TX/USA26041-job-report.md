---
type: job-report
job-number: USA26041
client: ExxonMobil
facility: ExxonMobil-Baytown-TX
heaters: [F-501]
po-number: 4411473422
quote: DSP26071
execution: 2026-08-11 to 2026-08-14
condition: first
source: service receipts 10780–10786 + USA26041 EXXON HU5 TriMax Ticket Breakdown.xlsx + 2026-08-12 XOM Flow Tests.pdf + Steady Flux 26-0663-002 Rev. A + Jesse interview 2026-08-16
verified: 2026-08-16
last-updated: 2026-08-16
tags: [job-report, ExxonMobil, USA26041]
---

# USA26041 — ExxonMobil Baytown HU5A F-501 Job Report

> Vault-native index of the customer-facing job report. Canonical deliverable is
> `USA26041_Job Report_ExxonMobil Baytown F-501_2026-08.docx`, built by the `/report` generator
> and living in the job's `Job Files\` folder. The report is **operational only** — no financial
> or change-order data. Actuals and as-built config also fold onto [[F-501]].

## Links

- Facility: [[02-facilities/ExxonMobil/Baytown-TX/_facility|ExxonMobil Baytown Refinery, Baytown, TX]]
- Heater card: [[F-501]]
- Job sheet (quoted plan): [[USA26041-job-sheet]]
- Quote: [[DSP26071|DSP26071.2]]
- Prior decoke: none — first USADebusk decoke of this heater

## Summary

Planned mechanical decoke with filtration of the HU5A F-501 process coils and Treat Gas coil,
August 11–14, 2026, as part of the August 2026 HU5A turnaround. One Trimax (Pumper 4) in triple
mode cleaning all three circuits concurrently, one pump per circuit, on a DeBusk filter press
loop. Jesse Utsey ran the job. Post-decoke smart-pig inspection by Steady Flux Technologies.
Condition `first` — no prior job history, so these actuals do not move the routine baseline.

## Actuals (reconciled to the ticket breakdown)

| Heater | Rig | Pig | Smart Pig | Stand-by | Operating |
|---|---|---|---|---|---|
| F-501 | 21 | 16 | 6 | 11 | 43 |

Quoted 48 hrs (8 rig-in / 24 pig / 8 smart pig / 8 rig-out). Pigging came in 33% under and
rig-out 75% over — the shape matters more than the −5 total. Crew 6, matching the quoted plan.
43 pigs used against 25 quoted: 4.25" TC 4 · 4.5" TC 10 / HR 6 · 4.75" TC 8 / HR 4 / Foam 8 ·
5" Foam 2 · 6" Swab 1. Stand-by 11 hrs, all ExxonMobil-caused — 3 of them the filter press stuck outside the **asphalt
gate**, unable to clear security until later that day because ExxonMobil's gate policy for
third-party equipment was unclear (Jesse, 2026-08-16). Standing site constraint, now on
[[02-facilities/ExxonMobil/Baytown-TX/_facility]].

## Cleaning result

Light fouling throughout. The radiant was the heaviest section but only slightly, and no pass or
coil was notably dirtier than the rest. Treat Gas had no fouling — complete within two hours of
fill and flush, and its flow test is flat as a result. Final pig size 4.75" on the process
circuits. Steady Flux confirmed the clean on all three circuits.

Flow-test Δ PSI at matched GPM (700 / 650 / 600 / 550): Pass A/B 45 · 35 · 28 · 27 ·
Pass C/D 57 · 45 · 38 · 31 · Treat Gas 0 · 0 · 0 · 5.

## Field findings

**Metal restrictions on Passes A and B.** Protruding into the tubes, **Pass B the worse of the
two**. They gouged the pigs slightly but did not significantly hinder the decoke. **Location is
mapped, not confirmed** — the restrictions were located in the cross-over area and that piping is
the likely source, but the cross-overs were never opened, nothing was visually verified, and
nothing appeared in the smart-pig inspection data (Jesse, 2026-08-16). Passes A and B finished on
a 4.75" pig against the 4.875" computed from tube ID; plan those passes against 4.75" until this
is characterised. Passes C and D ran clear.

**Pig appendage wear across sections — the durable finding.** The minor convection fouling the
inspection found was too thin to register on the pressure gauges. All pigs were launched and
received at the radiant outlets, so they travelled the smaller-bore radiant before reaching the
larger-bore convection, and their appendages were worn down by the time they arrived — which made
the convection tubes slightly harder to clean than their bore alone suggests. This is a
launch-direction consequence, not a heater defect, and it generalises to any heater pigged from
the radiant outlet into a larger-ID convection.

## Editorial boundary on the deliverable

The report states that the smart-pig inspection confirmed the clean and stops there (Jesse,
2026-08-16). **No wall-loss figures, no B_8_C, no per-section loss ranges** — those belong to
Steady Flux's own report to ExxonMobil. The full inspection analysis lives on [[F-501]], not in
the customer document.

## Source files

All in `…\Exxon Baytown_HU5-F501 Heater_2026 Aug\Job Files\`:

- Deliverable: `USA26041_Job Report_ExxonMobil Baytown F-501_2026-08.docx`
- Ticket breakdown: `USA26041 EXXON HU5 TriMax Ticket Breakdown.xlsx`
- Signed receipts 10780–10786: `2026-08-11 & 12 F-501 receipt.pdf` · `2026-08-03 DeBusk Service
  Receipt.pdf` (misnamed — this is 10783, Aug 13 day) · `2026-08-14 Exxon Service Receipt.pdf`
- Flow tests: `2026-08-12 XOM Flow Tests.pdf`
- Inspection: `26-0663-002 Exxon Baytown F501 Inspection Report.pdf` (Steady Flux, Rev. A)
- Images: `Images\` (originals) and `Images\_prepared\` (report-placed copies)

## Generator inputs

Config: `~/.claude/skills/usadebusk-fieldpm/back-test/report_input_usa26041.py`. Re-render with:

```
python render_job_report.py ../back-test/report_input_usa26041.py "<Job Files>/USA26041 EXXON HU5 TriMax Ticket Breakdown.xlsx" "<Job Files>/USA26041_Job Report_ExxonMobil Baytown F-501_2026-08.docx"
```

This job was the generator's first single-heater, single-pumper run. Two things it exposed, both
now fixed: `rig_unit_label` still defaulted to "Both units" (a two-rig assumption from USA26038),
and `build_images` only emitted a placeholder note — it now places real images from an `images`
config key, laid out as captioned rows of one or two figures. Both changes are backward
compatible; the USA26038 fixture is unaffected.
