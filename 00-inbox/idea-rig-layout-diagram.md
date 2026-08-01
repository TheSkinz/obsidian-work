---
type: idea-seed
status: unexplored
created: 2026-07-30
revisit-trigger: "Coil-visualization Tier 2+3 build lands (approved 2026-08-01, owed at [[2026-08-01-coil-visualization-build-owed]]) -> research the rig/hose layout diagram against the render path that build establishes — event: check when the coil-viz SVG generator exists"
related:
  - "[[2026-07-30-exploration-coil-visualization-for-crews]]"
  - "[[idea-coil-visualization-for-crews]]"
tags: [idea, field-ops, job-sheet, visualization, sop, future]
---

# Generated rig / hose layout diagram for the crew

Idea seed captured 2026-07-30, split out of
[[2026-07-30-exploration-coil-visualization-for-crews]] as Tier 5. It shares a destination with the
coil-visualization work — the crew's job sheet — but no data and no code, so it is a separate build.
The read below is tentative; confirm intent with Jesse before designing.

**Tentative read:** Jesse asked for the coil view and, alongside it, "the lay-out of hoses connected
to a representation of the pumper." That second half is surface equipment, not coil geometry: Trimax,
suction and discharge hose runs, 4×3 pump, filter press, tanks, diverter, launcher and receiver
positions. Unlike the coil, it does not derive from the heater card — it varies with the job walk.
Two things already exist to build on: `usadebusk-sop/SKILL.md` specifies the Pre-Execution PFD
("Two-process layout … Equipment blocks L to R: Fired Heater | Trimax Pumper | 4×3 Pump | Filter
Press"), and one has already been produced by hand for a live job —
`USADebusk-Diagram-HU5A-F501-REV1_2026-Aug.pdf`, referenced from
`02-facilities/ExxonMobil/Baytown-TX/HU5A-F501-job-sheet.md`. So the question is whether a reusable
template plus a small per-job input beats drawing it by hand each time.

**To explore:** What actually varies job to job versus what is fixed by equipment mode (single
Trimax / second Trimax / double mode / triple mode)? Is the useful artifact a scaled site plan, or a
topology schematic that shows what connects to what without claiming distances? Does it belong on
job-sheet page 2 next to the coil view, or stay a separate PDF as it is today? Is the existing
hand-drawn F-501 diagram close enough to a template that instantiating it per job is mostly
relabeling? Note the parked "SOP → Diagram Visualization Pipeline" in `01-context/workflow-map.md`
is adjacent and should be checked for overlap before designing.

**Gate:** Do not spend a research cycle until the coil-visualization decision is made — if that build
is approved, this one should reuse whatever rendering and job-sheet-embedding path it establishes
rather than inventing a second one. Mirrored into `revisit-trigger:` above so the health
dashboard's dormant-trigger registry keeps it visible while it waits.
