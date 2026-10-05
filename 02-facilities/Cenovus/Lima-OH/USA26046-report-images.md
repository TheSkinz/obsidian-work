---
type: reference
job-number: USA26046
client: Cenovus Energy
facility: Cenovus-Lima-OH
source: photos supplied by Jesse, 2026-10-02 onward
verified: 2026-10-02
tags: [job-report, images, Cenovus, USA26046]
---

# USA26046 — Report Images

Images for the combined USA26046 project report, gathered as Jesse uploads them. The files sit beside this note. Caption facts are Jesse's own words; the report's final captions are written at build time. **Do not build the report until Jesse says "build"** (2026-10-02).

| File | Heater | What it shows (Jesse) |
|---|---|---|
| `files/USA26046-vac-pass5-12in-coke-1.jpg` | [[PR-170029]] Vac | Coke removed from the 12" tube, pass 5, the dirtiest of the eight passes. Held up in front of the launcher barrel and a red valve |
| `files/USA26046-vac-pass5-12in-coke-2.jpg` | [[PR-170029]] Vac | The same pass 5 12" coke, resting on the launcher, with a nut beside it for scale |
| `files/USA26046-vac-radiant-outlet-layout-sketch.png` | [[PR-170029]] Vac | Jesse's rough sketch of the radiant outlet flange layout, seen facing the outlets: upper 8 5 · 4 1, lower 7 6 · 3 2. **Source for a clean graphic, not for use as-is** |
| `files/USA26046-vac-conv-inlet-piping-deposits.jpg` | [[PR-170029]] Vac | Thick deposits removed from the external 6" convection inlet piping, a collection from all passes. Each pass's external inlet piping was extremely fouled |

## Report content decisions

- **Vac Decoking Analysis carries the pass-by-tube detail** (Jesse, 2026-10-02): it names passes 4 and 5 by tube size, notes the other six were light throughout, and covers the inlet-piping-first strategy. Source: the coil-condition table and inlet-piping paragraph on [[PR-170029]].
- **A shift-by-shift timeline chart for every heater** (Jesse, 2026-10-02), in the style of the Vac cost summary's chart: one bar per shift, coloured by task (rig-in/over/out, pigging, smart pig support, stand-by), labelled by receipt and date. The Vac's data is in that summary; the Crude, HDS and Coker take theirs from receipts 8401–8428. The renderer has no timeline section yet, so it gets built at build time. Use the re-split hours for the Crude and HDS, so each chart matches its Task Durations row.
- **Vac radiant outlet layout graphic** (Jesse, 2026-10-02): a small, clean drawing redrawn from the sketch, captioned as the view facing the outlet flanges, with each number being the pass and its matching convection inlet. Place it in the Vac's Heater Data section. Say plainly that the field chalk marks and flange tags were wrong and that the numbering here governs.
- **Pigs Used = service-receipt pig counts** from each heater card (Crude 201, HDS 16, Coker 64, Vac 97), sizes only (Jesse, 2026-10-02). The run-sheet and admin counts stay internal while they are being investigated.
- **No PO field; the per-heater work orders go in its place**: Crude 82036534, Vac 82036776, Coker 82096135. No work order is written on the HDS receipts (Jesse, 2026-10-02).
- **Hours come from the heater cards' receipt actuals, not admin's ticket-breakdown workbook** (Jesse, 2026-10-02). The renderer needs an option to take actuals from config without a workbook.
- **Fouling grades received 2026-10-02** and on the cards: Crude heaviest in the upper 8" radiant tubes 1–5; HDS light throughout; Coker light in convection, moderate in radiant. **Decoking Analysis paragraphs for those three were drafted from the pig progression, pig hours and effluent returns, and sent to Jesse for review.** Use his edited wording at build. Build holds until Jesse says "build".
- **Decoking Analysis wording approved in substance (Jesse, 2026-10-02)**: where the fouling was, plus the average pigging time per pass, or per circuit when looped, and the looping arrangement. Crude: most fouling in the upper 8" radiant tubes 1–5; about 39 hrs per pass. HDS: light throughout; looped 1 + 2 and 3 + 4; about 20.5 hrs per circuit. Coker: light in the convection, moderate in the radiant; pigged as 3 circuits (convection, 4 coils as one; radiant A + B; radiant C + D, crossovers removed); about 51 hrs per circuit. Vac: the pass-by-tube grades.
- **Rev 0 rebuilt grouped by heater (Jesse, 2026-10-02):** one chapter per heater; flow tests two per row with the top three GPM steps; Jesse's white-background outlet graphic. 7 pages.
