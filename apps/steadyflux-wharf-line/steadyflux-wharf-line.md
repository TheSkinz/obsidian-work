---
type: reference
status: active
source_authority: secondary
confidence: high
created: 2026-09-06
related:
  - "[[steadyflux-pipeline-inspection-build-prompt]]"
  - "[[fable-5-1-prompting]]"
tags: [reference, visualization, pipeline-pigging, steady-flux, tools]
---

# Steady Flux Wharf Line Wall Survey

`steadyflux-wharf-line.html` — a single-file, self-contained visualization of a Steady Flux Technologies WiLBR Intelligent Pig inspection: a looped 6-inch and 8-inch marine wharf line, 5,612.69 ft of odometer, 115 recorded anomalies, 286 girth welds. Built 2026-09-06 from the brief at [[steadyflux-pipeline-inspection-build-prompt]]. No build step, no server, no runtime network requests: open the file directly. three.js r158 (the last UMD release) is vendored inline, ~650 KB of the file.

**Published artifact (private):** https://claude.ai/code/artifact/65b4714b-f98c-4048-9d3e-58ef2da5f98b

**Source.** Report 25-0532-006 Rev. C, inspection 2025-04-17. The source PDF is outside the vault (`C:\Users\Jwuts\Downloads\25-0532-006C ... REVC.pdf`) and is the customer's document, supplied informally by the Steady Flux CEO. Per the brief: **do not forward the built page to the operator or present it as work product.** The page deliberately names no operator, site or line designation; it does plot the surveyed coordinates as supplied, so it is identifiable to anyone who looks them up.

## Form

An x-ray flight along the surveyed centreline married to an unrolled-wall strip. The 3D pipe runs the real route at true axial scale with a semi-transparent wall so the bottom-of-pipe damage reads from any camera angle; the strip along the bottom carries the whole run (odometer × clock) so density and the 5:00–8:00 pattern are visible at once; a 2D cross-section ring in the record card shows how much steel is left at the current record and whether the loss came from inside or outside. The passive tour is a 178-second cycle driven from wall-clock time (a pure function of `t`, no accumulated deltas), so a backgrounded tab does not fall behind. Click a beacon or the strip to jump to a record; arrow keys step through all 115 in odometer order; Esc or a click on the pipe resumes.

## Decisions taken in the build (not in the report)

- **Odometer → route mapping.** The girth-weld chain and every anomaly are on the tool odometer (0–5,612.69 ft); the 41-waypoint GPS centreline totals 5,343.8 ft. Mapped uniformly, route = odometer × 0.9521. Every displayed distance is labelled by system.
- **Route geometry.** The survey as supplied traces an L-shape: A→I heads roughly S-SW, I→AF heads SW, and after Bend 4 the return leg heads NW, ending **4,238 ft** from the launch point. The brief says launch and receive were one site and the line doubles back. The page plots the coordinates as given and says the surveyed endpoints do not coincide. Not adjusted. *(Distance corrected 2026-09-07 from the "about 3,300 ft" originally written here: equirectangular projection at latitude 37.93 of Table 1's first waypoint A, 37.930667 / −122.399794, against its last, AM, 37.924453 / −122.412217, gives 3,579 ft west and 2,270 ft north — 4,238 ft separation. The three directional claims above were checked against the same waypoints and are correct.)*
- **Clock convention.** 0:00 top, clockwise looking toward the wharf. On the return leg (odometer past ≈4,651 ft, the mapped Bend 4) the view toward the wharf is backward relative to travel, so the clock is mirrored horizontally; bottom stays bottom.
- **Diameter exaggeration ×8.** 8-in OD renders as 5.75 ft, 6-in as 4.42 ft, so the reducers are visible and the pipe reads as a pipe. Axial positions and lengths are true. Circumferential extents are true as an angle, so a 4-inch-wide record on a 19-inch-circumference pipe spans 75° of arc.
- **Anomalies are geometry.** Each record is its own curved patch at its reported length and width, colour by remaining wall, edges fading to the steel colour (that fade is the only interpolation on the page). Internal loss sits just inside the wall surface, external just outside with an outline ring. Full-bore records (25.07 in on 8-in, 19.05 in on 6-in) are 360° patches with no gap.
- **Extents drawn downstream from the recorded position.** The report gives one position per record; the patch starts there and extends by the reported length.
- **MD-4 and D-1** (0.19 ft apart, overlapping extents) are treated as one feature and the card says so. Both records are still drawn and counted.
- **Reference grid.** No elevation data exists; the 50-ft grid under the pipe is a scale reference, not terrain.
- **P-1's report label** (41.30 ft past GW 135) and **EML-72's** (GW 162) are shown as the report wrote them, with the resolved figures beside them.

## Branding, as read from the live site (2026-09-06)

steadyflux.com is navy on black and white, not the teal the brief assumed: buttons and the diagonal header band `#22518B`, the accent `|` in "WiLBR | Intelligent Pig" `#4293DD`, tint `#ADC9EB`, greys `#E0E0E0` / `#BBBBBB`, body and headings `"Helvetica Neue", Arial, sans-serif` at weight 400 (nav uses Adobe `aktiv-grotesk`, not vendorable). The page uses those values; the remaining-wall scale (steel-blue → amber → red) is the page's own so that the one red record is unique. The round badge (`SteadyFlux_Badge_2lines_badgeA.webp`, the same asset the site serves) is embedded as a data URI in the title block; the assembler in the session scratchpad injected it from `Downloads`, so a rebuild needs that file or the site copy.

## Verification record

Ten startup assertions run on every load (counts of 115 / 286 / 41, minimum wall 0.060 at P-1, 94 records in the 5–8 band, 8 records at 25.07 in, IML-12 at 19.05 in, last weld and route totals) and print to the console; `?debug` shows them on the page. Every 0.1 s of the 178-s cycle was evaluated for a finite camera. Checked at 1440×900, 1000×640 and a phone-width emulation; console clean, one network request (the page itself).

Serve locally with the `static-apps` entry in `.claude/launch.json` (`python -m http.server 8765 --directory apps`).
