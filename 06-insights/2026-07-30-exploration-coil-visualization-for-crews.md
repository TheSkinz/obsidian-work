---
type: review
status: resolved
review_type: exploration
source_authority: primary
confidence: high
created: 2026-07-30
review_after: 2026-08-29
related:
  - "[[idea-coil-visualization-for-crews]]"
  - "[[idea-rig-layout-diagram]]"
  - "[[_canonical-job-sheet]]"
  - "[[_canonical-heater-card]]"
tags: [review, exploration, field-ops, job-sheet, visualization, heater-schema]
---

# Exploration — 2D Coil Visualization for Field Crews

## Trigger

Jesse, in session 2026-07-30: we extract coil geometry from fired-heater drawings, but the crew
only ever sees the raw numbers. Drawing snippets are the current fallback and they arrive buried
under fabrication callouts that mean nothing at a launcher. He asked for the option space from
convenience to complexity before deciding anything — explicitly no build this session. Scope he
named: coil elevation, terminal/plan view, pig-path schematic, section-stack summary, launcher and
receiver tied to a tube-count-correct pass, and a hose/pumper layout. Delivery target: job-sheet
page 2, produced as a standalone file first.

## Evidence

**1. The serpentine renderer already exists in this vault and is field-proven.**
`apps/pig-tracker/pig-tracker.html:393` — `buildGeometry()` — is a working heater-coil layout
engine. It draws two side-by-side banks (convection left, radiant right) collapsing to one centered
bank for convection-only heaters; serpentine rows with alternating direction and true SVG arc
U-bends (`A ${r},${r} 0 0 1 …`); pitch auto-scaled to tube count via
`Math.min(48, Math.max(9, 560 / maxRows))`; a crossover bridge routed convection-exit → down →
across → up into the radiant bottom row; and inlet/outlet flange stubs (`bStub`, `rStub`) at the
circuit ends. Its segment schema is
`{ zone: "convection"|"crossover"|"radiant", tubes, length_ft, id_in }` — a near one-to-one map onto
the heater card's Tube Geometry columns `Section / Tubes/Circuit / Length/Circuit / ID (in)`. The
optional per-segment `id_in` override exists specifically for step-down coils, so tube-size changes
already render. It also ships a custom-circuit builder UI with localStorage persistence
(`customCircuits`). What it does not do: read from heater cards (B-103 Suncor is hand-transcribed
into `BUILTIN_CIRCUITS`), draw more than one circuit at a time, show launcher/receiver/pumper/hoses,
or export a print-ready image.

**2. Nothing else in the vault renders coil geometry — there is no prior art to reconcile.**
Zero Mermaid blocks, zero SVG, zero image embeds across all 39 heater cards, `04-knowledge/`, or
`01-context/`. Every diagram in the skills is a generic template that disclaims per-job numbers:
`usadebusk-core/references/core-coil-template.md` states outright that "tube counts, crossover form,
and ID-transition points are per-job variables — read this as a template, not a spec." Same for
`usadebusk-sop/references/sop-pigging-diagrams.md` and
`usadebusk-equipment/references/equipment-circuit-diagrams.md`. The one adjacent parked item,
"SOP → Diagram Visualization Pipeline" in `01-context/workflow-map.md`, is about SOPs, not coils.

**3. The gap between what we capture and what the crew receives is large and measurable.**
`04-knowledge/ground-truth/h-2421.md` carries elevations (EL 102'-6 to 121'-3), the 7×4 convection
tube field, the serpentine wrap around the VC firebox, and a written travel path
("Launcher at grade → riser to A → conv circuit 1 serpentine down → X0A1 crossover → radiant circuit
A inlet elbow → 14 vertical tubes around firebox wall → outlet flange C → field jumper C↔D → …").
What reaches the crew on `02-facilities/HF-Sinclair/Artesia-NM/USA26040-job-sheet.md` is a three-row
table, one spec strip, and the parenthetical `Double mode, 2-pass (A→C→jumper→D→B)`. The rendered
`USA26040-job-sheet.html` is entirely tables plus one bordered `.connbox` — no image of any kind.

**4. Measured drawability across the portfolio: 28 of 39 cards can be drawn today.** A read-only
pass over every `type: heater` card, testing whether each `## Tube Geometry` row carries a parseable
tube count and a parseable ID:

| Result | Count | Detail |
|---|---|---|
| Fully drawable (tube count + ID on every row) | 28 | Includes all 5-row step-down cards (210-1403A, 210-1404B, VR-401C) and the 6-row B-101 |
| Partially drawable | 1 | F-201 — tube counts on 2 of 3 rows |
| Not drawable | 10 | 0 of 2 rows carry a tube count on each |

The 10 not-drawable cards are not scattered — they are two facilities whose data came from quotes
rather than drawings: eight of the nine CHS McPherson cards (`HF-0011`, `HF-0012`, `HF-009A`,
`HF-009B`, `HP-0002`, `HP-0006`, `HP-0007`, `HP-0025` — `HP-0003` is the lone exception and is fully
drawable) and both Flint-Hills Corpus Christi cards (`01-BA-105`, `02-BA-201`). That is a
data-source pattern, not a schema failure, and it means
a renderer covers roughly three-quarters of the portfolio on day one.

**5. Two secondary data facts bear on rendering quality.** `Arrangement` is missing or
`(not recorded)` on at least one row of 21 of 39 cards — more than half — which is exactly what the
exemplar predicts ("Radiant has NO default — state explicitly; genuinely ~50/50"). A renderer
therefore cannot reliably choose horizontal vs vertical tube orientation from data and must either
default and label the default, or draw orientation-neutral. Separately, 4 cards carry a compound
`ID (in)` cell holding multiple values in one string (e.g. `6.065 / 7.981 / 10.020`), which needs
parsing rather than a plain float read.

**6. Pass topology is not machine-readable anywhere.** The `configuration:` frontmatter key is the
only field carrying loop/pass structure, it is present on 37 of 39 cards, and it holds 36 distinct
free-text strings. `4 coils looped to 2 passes`, `4 pass looped to 2`, and `2 pass looped to 1` order
the same two numbers differently. The only structured precedent in the vault is the hand-built
`### Circuit mapping` table on `02-facilities/ExxonMobil/Baytown-TX/F-501.md` (Circuit / Passes /
Loop / Launcher location / Travel / Trimax pump), which is a one-off outside the canonical schema.

**7. The job sheet has an explicit one-page budget, and page 2 sidesteps it.**
`04-knowledge/_canonical-job-sheet.md`: "Six blocks fit with room to spare; nine did not. If a future
section is proposed, something else comes off." Page 2 does not compete for that space. The render
path is already headless Chrome to PDF and was used for `USA26040-job-sheet.pdf`; SVG embeds
natively in that HTML, so once a drawing exists the delivery mechanism costs nothing.

## The option ladder

**Tier 0 — clean the snippet.** Crop and white out the fabrication callouts on the drawing we
already have. Zero tooling, works today, highest fidelity. Breaks on per-job manual labor, and it
only works where a legible drawing exists — which excludes the same ten cards above.

**Tier 1 — Mermaid pig-path flow.** A text block in the card and job sheet:
launcher → convection pass (n tubes, ID) → crossover → radiant pass → jumper → receiver. Renders
natively in Obsidian and GitHub, versions as text, generates reliably. Honest limit: Mermaid is a
graph layout engine and cannot draw a serpentine to scale. It covers the circuit view well and the
coil-elevation view not at all.

**Tier 2 — static SVG coil elevation.** Lift `buildGeometry()` out of the pig-tracker into a
generator that reads a card's Tube Geometry table and emits an SVG. Delivers the stacked-pipe view,
tube counts, U-bends, the crossover, and visible size-change points. Best value per unit of effort
on the ladder, because the layout algorithm is already written and already correct.

**Tier 3 — terminal and connection layer.** Launcher and receiver boxes at the stub ends, labeled
from `## Connection Info (Facts)` with the real flange spec and adapter note, plus pass letters and
flow arrows. This is the thing Jesse named first — the launcher tied to a tube-count-correct pass.
Cheap once Tier 2 exists; it is annotation on a path that already has endpoints.

**Tier 4 — multi-pass circuit sheet.** All passes side by side, showing jumper spools, circuit
grouping, and which Trimax assembly feeds which. Blocked by evidence 6 — the topology exists nowhere
machine-readable, and F-501's circuit-mapping table would have to become a schema field or be
hand-entered per job.

**Tier 5 — rig and hose layout.** Pumper, suction and discharge hoses, filter press, tanks, diverter.
A different drawing: surface equipment, not coil geometry, and it varies with the job walk rather
than with the card. `usadebusk-sop/SKILL.md` already specifies it as the Pre-Execution PFD
("Equipment blocks L to R: Fired Heater | Trimax Pumper | 4×3 Pump | Filter Press"), and
`HU5A-F501-job-sheet.md` shows one already produced by hand as
`USADebusk-Diagram-HU5A-F501-REV1_2026-Aug.pdf`. Shares a destination with Tiers 2–4 but no data and
no code — tracked separately as [[idea-rig-layout-diagram]].

**Tier 6 — 3D.** Recommend against, with one carve-out. A 3D heater needs tube-field rows × columns,
tube spacing, and firebox dimensions. Exactly one card in the vault carries row×column geometry —
H-2421's "28 total in 7×4 field" — and it is prose in a notes block, not a field. We would be
inventing the input, which collides directly with the card schema's stated-values-only rule. The
carve-out: on vertical-cylindrical heaters the terminals wrap a circle (see
`04-knowledge/ground-truth/h-2421-snippets/rc_plan.png`) and "which nozzle is which" is genuinely
hard to read off an elevation. A **2D plan-view circle diagram** solves that at a fraction of 3D's
cost and should be considered a Tier 3 variant for VC heaters, not a step toward 3D.

## Interpretation

**The idea is sound, the enabling asset already exists, and the cheap tiers are unblocked.** The
usual reason to park a build here — premature automation ahead of data maturity — does not apply the
way it did to the actuals rollup. The data is measured, not assumed: 28 of 39 cards carry everything
a serpentine needs, the layout engine is written, and the delivery path is already in production for
job sheets. What is genuinely blocked is Tier 4 only, and it is blocked on a schema decision rather
than on thin data.

**Two things worth stating that were not in the original ask.**

First, this is an extraction QA instrument, not only a crew aid. A generated schematic cannot be
drawn without placing every tube, which forces unresolved geometry into the open.
`04-knowledge/ground-truth/h-28.md` row 4 already records exactly this failure — "2 tubes cannot
split evenly across 4 coils — which pass(es) carry them is unstated." Today that sits as a footnote
a reader may skip; a renderer would be unable to draw it. That reframes the return from per-job
convenience to something touching every bid, which is the higher-value framing.

Second, the fidelity trap. "It doesn't need to be exact" is correct as a scoping decision and
dangerous as a rendering decision — a schematic that looks like a drawing gets read as one, and
someone will eventually scale off it. The mitigation is to inherit the discipline the cards already
enforce: draw only stated values, render a missing tube count as a visibly indeterminate element
rather than a guess, use no dimension lines or elevations unless recorded, and stamp every output
"schematic — not to scale, not for fabrication."

## Recommended Action

**Build Tier 2 + Tier 3 together as a standalone per-heater SVG, and take Tier 1 alongside it.**
Tier 2+3 reuses a proven layout engine, needs only fields 28 cards already carry, and delivers the
view named first. Tier 1 is nearly free and covers the circuit view that Tier 2 structurally cannot.
They are complementary, not competing.

Concretely, if approved: (a) extract `buildGeometry()` from `apps/pig-tracker/pig-tracker.html` into a
generator that reads `## Tube Geometry` and `## Connection Info (Facts)` off one heater card and
emits an SVG file — note the vault `tools/` convention is pure standard library, and
`estimating_rollup.py` already exports the markdown-table parsers (`section_lines`, `table_rows`,
`num`, `heater_cards`) this would reuse; (b) render missing or compound values honestly rather than
guessing, and carry the not-to-scale stamp; (c) prove it against H-2421 and H-28, where independent
ground-truth records exist to check the output against; (d) only then decide whether it lands on
job-sheet page 2 or stays a standalone file. Tier 4 stays parked pending a pass-topology schema
field, which should ride the existing heater-card schema trigger rather than opening its own change.

## Decision

**Rows 1–3 are mutually exclusive scope choices — pick one.** Tier 5 is not part of this decision;
it is tracked separately as [[idea-rig-layout-diagram]].

- [x] **Approved — Tier 2 + Tier 3 + Tier 1** (Jesse, 2026-08-01) — SVG coil elevation with launcher/receiver terminals, plus the Mermaid circuit block
- [ ] ~~Approved — Tier 1 only (Mermaid circuit block; defer the SVG generator)~~
- [ ] ~~Approved — Tier 2 only (coil elevation, no terminal layer, no Mermaid)~~
- [ ] ~~Park — revisit on a trigger to be named~~
- [ ] ~~Drop~~

**Approved as scope, not as scheduled work.** The build is filed as owed at
`00-inbox/2026-08-01-coil-visualization-build-owed.md`.

It will not reach the USA26040 crew — that job mobilizes 2026-08-04 and the window is gone
regardless of what was decided here. The scope was approved anyway because the input data is as
good as it will ever be: H-2421's card was verified line-by-line against GA drawings J04917
CC1/RC1, the Navajo nozzle sheet, and the USAD Excel on 2026-07-19, and the heater recurs on
[[DSP26080]] (Feb 2027 Artesia outage, three heaters).

This decision also releases [[idea-rig-layout-diagram]], whose dormant trigger was gated on this
block resolving. That trigger is re-pointed rather than retired — it was written to fire against
"whatever render path that build establishes," and the build has not happened yet, so the
condition now names the build rather than this decision.

## Apply Log

| Date | Action | By | Notes |
|---|---|---|---|
| 2026-07-30 | Exploration written; no build | Claude (Opus 5) | Jesse asked for the option space only. Drawability count (28/39) measured, not estimated. Awaiting tier decision. |
| 2026-08-01 | **Tier 2+3+1 approved; `status` → `resolved`** | Claude | Decision only — no build this session. Owed work filed to `00-inbox/2026-08-01-coil-visualization-build-owed.md`. Source seed `00-inbox/idea-coil-visualization-for-crews.md` closed. |
| 2026-08-01 | `revisit-trigger:` on [[idea-rig-layout-diagram]] re-pointed | Claude | The old condition ("Tier decision made on this note") has now fired, but its stated action — research the rig/hose layout against the render path *that build establishes* — is not yet reachable, since the build is owed. Re-pointed at the build rather than retired, so it does not read as satisfied while the thing it depends on is missing. |
