---
type: idea-seed
status: active
created: 2026-07-30
related:
  - "[[2026-07-30-exploration-coil-visualization-for-crews]]"
  - "[[idea-coil-visualization-for-crews]]"
  - "[[2026-08-03-idea-research-rig-layout-diagram]]"
  - "[[rig-diagram-corpus]]"
tags: [idea, field-ops, job-sheet, visualization, sop]
---

# Generated rig / hose layout diagram for the crew

Idea seed captured 2026-07-30, split out of
[[2026-07-30-exploration-coil-visualization-for-crews]] as Tier 5. It shares a destination with the
coil-visualization work but no data and no code, so it is a separate build.

**Ungated 2026-08-16.** The original read was tentative and has now been checked against the real
artifacts and confirmed with Jesse; the corrections are folded in below.

**The ask.** Jesse asked for the coil view and, alongside it, "the lay-out of hoses connected to a
representation of the pumper." That second half is surface equipment, not coil geometry: Trimax,
suction and discharge hose runs, 4×3 pump, filter press, tanks, diverter, launcher and receiver
positions. Unlike the coil, it does not derive from the heater card — it varies with the job walk.
`usadebusk-sop/SKILL.md` specifies the Pre-Execution PFD ("Two-process layout … Equipment blocks
L to R: Fired Heater | Trimax Pumper | 4×3 Pump | Filter Press").

**Correction — five diagrams exist by hand, not one.** The seed originally named only
`USADebusk-Diagram-HU5A-F501-REV1_2026-Aug.pdf` and cited it from a path that does not exist
(`HU5A-F501-job-sheet.md`; the real references are `USA26041-job-sheet.md` and `F-501.md`). Four
job-specific diagrams plus the generic REV K schematic sit in
`…\Desktop\Facilities\Active Work\Revamped Diagrams\`, inventoried at [[rig-diagram-corpus]].
That corpus answers three of the four questions below from evidence rather than by asking.

**Answered from the corpus:**
- *Fixed vs variable* — a single visual grammar holds across all four job diagrams; what varies is
  Trimax count, pumps per Trimax, circuit count and pass→pump assignment, launcher/receiver count,
  filtration elected or not, water source, and flange spec. See [[rig-diagram-corpus]].
- *Scaled site plan or topology* — settled in practice. None of the five claims a distance,
  dimension line, or plot position. All five are topology. A scaled site plan is a genuinely
  useful but separate document, ROI-gated and parked.
- *Does it need the coil view* — no. Three of the four draw the heater as an opaque box; only
  F-501 renders pass routing inside it. The rig layout stands alone.
- *Overlap with the parked "SOP → Diagram Visualization Pipeline"* (`01-context/workflow-map.md`)
  — none to reconcile. It is a one-line stub with no spec behind it, in a file that stopped
  tracking active work 2026-07-19. Absorbed by this, not a blocker.

**Still open:** whether it lands on job-sheet page 2 or stays a separate PDF. The audience is both
customer submittal *and* crew field aid, which may mean two renders of one source. Decide after the
artifact works, matching the coil-viz note's own sequencing.

**Gate — resolved 2026-08-16, was never really about rendering.** The original gate said to wait for
the coil-visualization build so this would not invent a second rendering and job-sheet-embedding
path. Checked: the rendering path already exists in production on both sides — the rig diagrams are
HTML with inline SVG printed to PDF (`…\Active Work\Schematic\DeBuskFiltrationSchematic.html`), and
job sheets use the same headless-Chrome `--print-to-pdf` route per `_canonical-job-sheet.md`. Tier
2+3 would consume that path, not establish it, and what it *does* newly establish — a Python
generator parsing heater-card markdown tables — this cannot consume, because there is no heater-card
data behind a rig layout. The embedding half is genuinely shared but is explicitly deferred by the
coil-viz note itself ("decide standalone file vs job-sheet page 2 only after it works"). So waiting
bought nothing. Ungated with Jesse's sign-off; `revisit-trigger:` retired.

**Where it goes next:** the real cost driver was never authoring or relabeling — it was geometry
correction against hand-placed absolute coordinates. Two candidate fixes (freeze the coordinates
into per-config templates, or drop coordinates entirely and compute them from layout) went to a
bounded back-test on F-901 the same day — [[2026-08-16-backtest-rig-diagram-layout-engine]].
Computed layout passed orthogonal routing, port order and the filtration swap; dual-Trimax is
unproven and is the case that decides it. Prototype at `apps/rig-diagram/`.
