---
type: idea-seed
status: resolved
created: 2026-07-30
related:
  - "[[2026-07-30-exploration-coil-visualization-for-crews]]"
  - "[[idea-rig-layout-diagram]]"
tags: [idea, field-ops, job-sheet, visualization, future]
---

# 2D coil visualization for field crews

Idea seed captured 2026-07-30 from Jesse directly. Explored the same session — the full option
ladder, the measured drawability count, and the recommendation live in
[[2026-07-30-exploration-coil-visualization-for-crews]], which carries the open Decision block.
This seed exists only so the capture loop tracks the idea; do not re-research it.

**Tentative read:** Coil geometry is extracted from heater drawings and landed on heater cards at
high fidelity, but the crew only ever receives the numbers. Drawing snippets are the current
fallback and arrive covered in fabrication callouts that mean nothing at a launcher. A generated,
deliberately-schematic 2D coil view — tube count, tube size, size-change points, launcher and
receiver tied to a tube-count-correct pass — would close that gap. Delivery target is job-sheet
page 2, produced as a standalone file first.

**Already answered by the exploration:** the serpentine renderer already exists at
`apps/pig-tracker/pig-tracker.html:393` (`buildGeometry()`), and its segment schema maps almost
one-to-one onto the card's Tube Geometry columns; 28 of 39 heater cards carry enough data to draw
today; pass topology (`configuration:`) is free text across 36 distinct strings and is the one thing
genuinely blocked.

**Open — awaiting Jesse's ruling:** which tier to build. See the Decision block on the exploration
note. Tier 4 (multi-pass circuit sheet) additionally needs a pass-topology schema field and should
ride the existing heater-card schema trigger rather than opening its own change.
