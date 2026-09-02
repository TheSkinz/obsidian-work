---
type: reference
status: active
source_authority: primary
confidence: high
created: 2026-08-16
review_after: 2026-11-16
related:
  - "[[idea-rig-layout-diagram]]"
  - "[[2026-08-03-idea-research-rig-layout-diagram]]"
  - "[[2026-07-30-exploration-coil-visualization-for-crews]]"
tags: [reference, field-ops, visualization, sop, pfd, equipment]
---

# Rig / Hose Layout Diagram Corpus

Inventory and grammar of the hand-built rig-layout diagrams. Written 2026-08-16 because the
whole corpus existed only on the Desktop and was referenced from nowhere systematic — the seed
that spawned this work believed one diagram existed when there are five.

**Source of truth for the files themselves:**
`C:\Users\Jwuts\OneDrive\Desktop\Facilities\Active Work\Revamped Diagrams\`.
The F-501 copy is also in the ExxonMobil submittal tree under
`…\Exxon Baytown_HU5-F501 Heater_2026 Aug\2026_Submit\Job docs\`.

These are **customer submittal documents and crew field aids both** — they ship with the
pre-execution package per `usadebusk-sop` and the crew reads them at the rig. Treat any edit to a
shipped revision as a client-deliverable change.

---

## The corpus

| File | Heater / client | Config | Circuits | L/R | Filtration | Water source | Flange |
|---|---|---|---|---|---|---|---|
| `USADebusk-Diagram-HU5A-F501-REV1_2026-Aug.pdf` | F-501, ExxonMobil Baytown HU5A | 1 Trimax, triple | 3 | 6 | Elected — 1 press | Fresh condensate (HU4) + 20,000 gal frac | 5" & 6" 300# RFWN |
| `USAD_ ExxonMobil Baytown_F-802 Process Flow Diagram.pdf` | F-802, ExxonMobil Baytown | 2 Trimax (3+2 pumps) | 5 | 10 | Shared press, both units | Clean-water frac ×2 | 6" 300# |
| `USAD-ExxonBaytown-F901-Diagram.pdf` | F-901, ExxonMobil Baytown PS8 (KHF) | 1 Trimax, triple | 3 | 6 | Drawn, but **declined at execution** — see below | 1× 20,000 gal frac | 5" 300# RFWN |
| `USAD-Marathon Detroit-Diagram-70H1.pdf` | 70H1 coker, Marathon Detroit (REV 6) | 2 Trimax, 6 pumps | 6 | 12 | **None** | Hydrant → coke pit / oily water sewer | 4" 300# RFWN |
| `USAD-Suncor Montreal-Filtration Schematic.pdf` | Generic — PFD-DCK-001 REV K | — | — | — | Shown | — | — |

The Suncor file is the **canonical generic schematic**, not a job instance. It matches the PFD
output format in `usadebusk-sop/SKILL.md` exactly — CLOSED-LOOP / FLOW REVERSIBLE header, the
two-process P1 PIGGING / P2 FILTRATION split, Fig. 200 at the pump end, 3" Camlock on all
filtration connections. It is branded DeBusk Services Canada and carries the press spec
(73 polypropylene plates, 1,243.4 ft², 100 PSI, 400 GPM) and the diverter description
(90° plunger, operator-controlled from the cab).

---

## Fixed grammar

Identical across all four job diagrams. This is the template, whether or not one is ever
formalised:

- **Trimax module** — gold-bordered box containing a brown DIRTY TANK, a blue CLEAN TANK, and a
  vertical stack of pump circles, one per pump, each coloured to the circuit it feeds. Ports
  label out as `P<n> Out` / `P<n> In`.
- **Heater** — green-bordered box at the right edge.
- **Hose runs** — dashed lines, one colour per circuit, routed orthogonally from pump port →
  launcher/receiver box → heater port. Pump stack order matches launcher order top-to-bottom.
- **Launcher / receiver** — paired boxes labelled `L-n` / `R-n`, in circuit colour.
- **Support equipment** — filter press as a plate stack, 4×3 trash pump, frac tank.
- **Footer legend** — three or four columns: Circuit Assignments | Heater Architecture |
  Equipment Scope (+ Legend Symbols on 70H1).
- **Title block** — heater name, then Trimax count and mode as a subtitle
  ("SINGLE TRIMAX / TRIPLE MODE OPERATION"), then client and unit.

## What varies — the real per-job input

- Trimax count (1 or 2) and pumps per Trimax (2 or 3)
- Circuit count and the pass→pump assignment
- Launcher/receiver count (6, 10, 12)
- **Filtration elected or not** — the largest structural swap. Elected gives press + tanks +
  4×3 pump on the left; not elected gives hydrant supply and "To Coke Pit or Oily Water Sewer"
  drains, as on 70H1.
- Water source: condensate, frac tank, or hydrant
- Flange spec and adapters: 4" / 5" / 6" 300# RFWN, plus reducers and temp adapters
- Loop/U-bend pairings where passes are looped (F-802 lists five: P2=P3, P1=P5, P9=P4,
  P10=P6, P8=P7)

## ⚠ The diagrams are planning artifacts and can diverge from the card

Two defects are already logged against F-901's diagram on [[F-901]], and both matter to anyone
reading or rebuilding it:

- **Filtration was declined immediately before execution** and none ran on the job (per Jesse,
  2026-07-26). The diagram and SOP-DCK-F901-001 REV 0 both draw a DeBusk press with a full
  recycle loop. The diagram records the *plan*, not the outcome.
- **Max pig OD reads 5.5", which breaches the ceiling.** The governing ID is 5.043", capping the
  pig at 5.25". The SOP repeats the same error. Jesse ruled 2026-07-26 that the issued documents
  stay as-is because the project is closed, and the card carries the correct figure. **If F-901
  is worked again the SOP must be corrected before reissue.** Do not propagate 5.5" into any
  rebuild or template.

This is the strongest available argument for sourcing diagram data from the heater card rather
than re-keying it: a card-driven render would have carried 5.25" and would have made the
filtration election a field rather than a drawn-in assumption. It is the same
extraction-QA framing that earned the coil visualization its approval.

Note also that F-901 has **two copies under different names** — `USAD-F901-Diagram.pdf` in
`…\_History\Exxon Baytown KHF F-901\` and `USAD-ExxonBaytown-F901-Diagram.pdf` in Revamped
Diagrams. Confirm which is current before treating either as the reference.

## Drawing rules (Jesse, 2026-08-16)

Stated while reviewing a generated rebuild. These are how the rig actually works, so they
govern any diagram of it — not style preferences.

- **The frac tank is off-system.** Water is drawn from it at the *start* of the job to fill the
  system; it is not part of the circulating loop. Draw it separated, and never route filtration
  hoses through or past it. Its hose runs **directly into the Trimax pumper**.
- **Launchers and receivers bolt to the heater flanges.** There is one jetting-hose run, pumper
  → launcher/receiver. Drawing a second hose from the launcher to the heater is wrong — the
  launcher *is* on the heater. **Which flanges they bolt to is a per-job election, not a fixed
  convection-inlet/radiant-outlet split** — on a looped circuit both land at the same end and the
  180s take the other (corrected 2026-09-02; see `manual/08-phase-i-rig-in.md` §8.2).
- **Scale: the Trimax is about the size of a frac tank.** It is a trailer. It must never be
  drawn taller or larger than the heater, and the rig as a whole does not need to be tall or
  long. Jesse notes this was a standing failure in the chat-built versions — the pumper came out
  far too tall and threw the whole scale off.
- **Jetting hoses from the pump ports to the launchers must not cross.** Route them as a planar
  fan: order the lanes to match the launcher order, so crossings are impossible rather than
  merely avoided.
- **Return flow direction.** Water returns *from* the receiver *into* the pump. Arrowheads on
  receiver legs point back toward the Trimax, not toward the heater.

Still unrepresented in the generated rebuild, and present in the hand-made originals: the
**diverter** (90° plunger, operator-controlled from the cab, routing return to clean or dirty
tank on water clarity) and the **loop/jumper** on passes that are looped rather than single
(F-901 Pass 1 is two coils looped via JS-1).

## Two facts that shape any future tooling

**The heater is opaque in three of four.** F-802, F-901 and 70H1 draw it as a plain green box.
Only F-501 renders pass routing, 180° temp bends and radiant outlets inside it. **A rig layout
does not require coil rendering** — that merge is optional, and F-501 is the exception.

**None of the five claims a distance.** No dimension lines, no elevations, no plot positions.
All five are topology schematics. A spatially scaled site plan is a genuinely useful but
separate document and is currently parked on ROI.

---

## Build history and the real cost driver

The corpus was built across three chat threads in Feb–Mar 2026 (original filtration schematic
27 Feb; Suncor REV K 6 Mar; F-802 dual-pumper 6–7 Mar, v1 through v7 plus a draw.io XML export
generated by a Python script — **that export is no longer on disk**).

Cost breakdown, per Jesse's own account:

- **Pure relabeling: under 5%.** Global name swap for the Canada division, title and rev
  changes, dropping legend entries, label size bumps. Roughly twenty minutes across everything.
- **Genuine authoring: 20–25%.** The original coordinate architecture (absolute-positioned divs
  with an SVG overlay, orthogonal-only routing, iframe-safe measurement), the linear→hub/manifold
  topology decision for the dual-pumper, and ten-pass routing where pump order had to match
  launcher port order top-to-bottom.
- **The majority: geometry correction in a screenshot feedback loop.** Diagonal lines that should
  have been orthogonal, arrowheads reversed because x1/x2 were swapped, a missing segment at a
  T-junction, a 10px gap that needed to be 20, the filter press rendered at half scale, ports
  clustered horizontally that should stack vertically.

**"Relabel vs author" is the wrong axis.** Every item in that third bucket is a symptom of
hand-placed absolute coordinates, and the same failure classes recurred across all three threads.
A separate sink — rebuilding the DeBusk Canada logo across multiple formats and a detour through
another model — netted zero and ended on the original website PNG. Standing practice since: use a
simple `[logo]` placeholder Jesse swaps himself, never rebuild a wordmark.

**The rendering path is already settled and is not an open question.** These are HTML with
hand-authored inline SVG, printed to PDF. The one recovered source is
`…\Active Work\Schematic\DeBuskFiltrationSchematic.html` — 593 lines, one `<svg>`, CSS-grid
footer, zero JavaScript. Job sheets use the same headless-Chrome `--print-to-pdf` route recorded
in `_canonical-job-sheet.md`. Any future work inherits this path rather than choosing one.

**Open, and the subject of a back-test:** whether to freeze the coordinates into a small set of
per-config templates that get filled by find-and-replace (Jesse's own May-2026 conclusion, never
built), or to drop coordinates entirely and declare topology to a layout engine. See
[[idea-rig-layout-diagram]].
