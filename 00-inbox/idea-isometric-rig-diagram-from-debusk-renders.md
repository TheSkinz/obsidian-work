---
type: idea-seed
status: unexplored
created: 2026-08-16
related:
  - "[[rig-diagram-corpus]]"
  - "[[2026-08-16-backtest-rig-diagram-layout-engine]]"
  - "[[idea-rig-layout-diagram]]"
tags: [idea, field-ops, visualization, sop, tooling]
---

# Isometric rig layout built from DeBusk's existing 3D equipment renders

Captured 2026-08-16 at the end of the rig-diagram session, after the flat-schematic generator was
closed out. This is a different idea, not a reopening of that one — it targets the *site plan*
Jesse has twice called useful-but-ROI-gated, not the topology schematic.

**Tentative read:** DeBusk's website and marketing video already carry professional 3D renders of
the equipment — Jesse showed the pumper unit render. That kills the objection that stopped this
idea cold: I had assessed isometric as "framework is easy, the icons are the whole cost, and
drawing them is art." The art exists and has already been paid for. The remaining work is asset
gathering, not illustration.

**Two things worth writing down because they are not obvious:**

- **Isometric is not 3D.** Diagrams of that style are flat 2D drawings on an isometric grid using
  pre-drawn isometric assets — no rendering, no camera, no perspective. The projection is one
  affine transform. The router already built in `apps/rig-diagram/` ports directly: it constrains
  segments to two axes today, and isometric constrains them to three (30° / 150° / vertical). The
  non-crossing lane rule survives unchanged.
- **The DeBusk renders are perspective, not isometric.** The pumper render is a 3/4 view with a
  vanishing point. Compositing perspective renders shot at different camera heights and angles is
  what makes assembled diagrams read as pasted together, and arranging cannot fix it.

**The hinge — one question decides the whole thing.** Do the **source 3D models** exist somewhere
reachable (whoever produced the marketing video has them), or only the finished images? With the
models, each piece re-renders orthographically at one fixed isometric camera and yields a matched,
reusable set — genuinely easy, and a strong customer-facing asset for a submittal package. With
only finished images, it is a mismatched-angle compositing job that gets fiddly fast.

**Honest limit:** this does not touch the constraint that closed the flat generator — domain
correctness still needs Jesse's review on every drawing. It fixes a *different* problem, that the
generated version looked generic. Recognisable equipment does remove one class of ambiguity
(which box is the press and which is the pump), but that is a side effect, not the case for it.

**Note for the record:** the coil-visualization exploration ruled against 3D at Tier 6, but that
ruling was about the *heater coil* — the objection was inventing input, since only one card
carries row×column tube geometry. It does not apply to surface equipment, where nothing derives
from a heater card. Do not read that note as blocking this.

---

## Tooling found the same session (applies here and to the flat diagrams)

Checked Jesse's own catalogs first: **no diagram connector in the MCP registry, no matching
skill, no plugin.** Everything below is a manual install and none of it is verified on his
Windows setup. draw.io Desktop does not appear to be installed.

- **Official draw.io MCP server** — <https://www.drawio.com/docs/manual/generate/drawio-mcp-server/>,
  `npx @drawio/mcp`. Four integration modes; the relevant one is **Skill + CLI for Claude Code**,
  which generates `.drawio` files and exports PNG/SVG/PDF (requires draw.io Desktop). First-party.
- **`lgazo/drawio-mcp-server`** — <https://github.com/lgazo/drawio-mcp-server>. Reads and edits an
  *already-open* diagram live over WebSocket, so a single shape can be changed without regenerating.
  Browser-extension path works; desktop path is experimental and currently blocked by CSP.
- **P&ID symbol libraries** — draw.io ships no P&ID template but the shapes exist, and open-source
  ISA-5.1 / ISO 10628 sets do (one gist catalogues 407 symbols across 12 categories: pumps,
  vessels, filters, valves, heat exchangers, instruments). Import via `File > Open Library from URL`.
- **draw.io isometric support** — isometric shapes and connectors in the Misc sidebar, an isometric
  grid mode, AWS 3D objects, and a **generic isometric container that accepts any SVG on its face**
  (`kew-lab/drawio-generic-3d-shape`). Snap-to-isometric-grid is still an open feature request, so
  alignment is manual.

**Why draw.io keeps surfacing:** it changes what a flaw *costs*. Today a flaw cost a conversation —
Jesse explaining an adjustment, then fixing it by hand outside the tool. In a `.drawio` file it
costs a drag. That is the binding constraint from
[[2026-08-16-backtest-rig-diagram-layout-engine]], and it is the one thing a better file format
actually improves. It also fits the template conclusion rather than reopening it: rebuild the four
shipped diagrams once as `.drawio` masters, correct them once, and per-job work becomes relabeling
in an editor Jesse controls.

Jesse has draw.io history here already — the March 2026 v7 export came out of that work, though it
is no longer on disk.

**To explore:** Answer the source-models question first; everything else is downstream of it. Then
whether one matched isometric asset set covers the real config space (single/dual Trimax,
filtration or not), and whether the site plan is worth a build at all or stays a hand-made one-off
like the four existing diagrams.
