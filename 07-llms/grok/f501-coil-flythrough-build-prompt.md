# Grok Build prompt — F-501 Pass B POV flythrough (wormhole style)

Paste everything below the line into Grok Build as a single message.

**Reference for the visual style:** first-person POV flying down the tunnel — motion streaks
radiating outward and converging to a point ahead, a dense field of small particles rushing
past, saturated overlapping color washes (cyan/teal, orange, purple, pink), high energy and
glowing. Think a hyperspace/wormhole tunnel sequence, but happening inside a real pipe. No
vehicle or figure needs to be visible in frame — pure POV, camera is the traveler.

---

Build a single-file HTML app: an interactive 3D visualization of a real fired-heater
process coil, with a cinematic first-person POV flythrough of the entire coil interior, in a
hyperspace/wormhole visual style.

## Technical format

Code in a **single-file HTML** format. Use **three.js v0.180.0** loaded via the **import map**
method from a CDN, including `OrbitControls`, `EffectComposer`, `RenderPass` and
`UnrealBloomPass` from the matching `three/addons/` path. No build step, no external asset
files, no frameworks. Everything — geometry, data, shaders, UI — inline in one file.

## What this is

This is a hydrotreater fired heater coil at an oil refinery: ExxonMobil Baytown, unit HU5A,
heater F-501, process Pass B. It was mechanically decoked in August 2026 and then inspected
with an ultrasonic "smart pig" — a tool that travels inside the pipe and measures remaining
wall thickness. The data below is the real inspection result.

The pipe is a continuous serpentine. Fluid enters the convection section at the top of the
heater, snakes down through 9 horizontal tubes, crosses over to the radiant section, then
snakes down through 15 vertical tubes to a grade-level outlet. The camera flies through the
inside of that pipe, end to end, like a POV shot travelling down a wormhole — except the
tunnel is a real pipe with real dimensions and its walls are painted with real inspection data.

## Geometry — build exactly this, do not invent segments

All dimensions in inches. The path is 49 elements in strict order: 25 straight segments and
24 bends, totalling **9,768.2 in (814.0 ft)**. Display the total as 814 ft and verify your
built path length matches within 1 ft.

**Pipe cross-section.** Outside diameter is 5.563 in everywhere. The sections differ by WALL
THICKNESS, not by pipe size, so the bore actually gets SMALLER as you go:

| Section | Inside diameter (bore) | Nominal wall | Metallurgy |
|---|---|---|---|
| Convection | 4.763 | 0.400 | 9Cr-1Mo alloy |
| Crossover | 4.635 | 0.464 | 9Cr-1Mo alloy |
| Radiant | 4.635 | 0.464 | 9Cr-1Mo alloy |

This bore change at the convection-to-crossover transition is a real and visually important
event. The tunnel must visibly tighten there.

**Bends.** The lengths given for bends are ARC LENGTHS along the pipe centerline.
- 18.9 in and 15.7 in bends are **180° close return bends**. Centerline radius = arc / π
  (6.02 in and 5.00 in respectively). Tube-to-tube center spacing = 2 × radius.
- The two 9.4 in bends are **90° elbows**. Centerline radius = arc / (π/2) = 5.98 in.
  These are the convection-to-crossover turn and the crossover-to-radiant turn. Do not
  build them as 180° bends — the routing will not close if you do.

**Layout in space.**
- Convection section: 9 horizontal tubes running along the X axis, stacked vertically in a
  single plane, tube 1 at the TOP. 180° return bends alternate between the two ends. Flow
  runs downward through the stack.
- Crossover: leaves the bottom of the convection bank via a 90° elbow, runs 113 in as
  external piping, then turns 90° down into the top of the radiant section.
- Radiant section: 15 vertical tubes running along the Y axis, side by side along the Z axis,
  in a single plane. Tube 1 starts at the TOP and flows DOWN. Return bends alternate: bottom,
  top, bottom, top — 7 at the bottom, 7 at the top. Tube 15 (odd numbered, therefore flowing
  down) terminates at the BOTTOM. That terminal point is the grade-level radiant outlet where
  the pig launcher was connected.
- Net result: a heater roughly 24 ft wide and 40 ft tall in the radiant firebox, with a
  smaller convection bank above it. Build it to true scale.

**The path, in travel order.** `id | type | length(in) | min remaining wall(in) | wall loss(%) |
distance of that minimum from the segment's upstream weld(in) | ovality(%)`. A dash means the
report recorded no value.

```
CONVECTION  (bore 4.763, nominal wall 0.400)
B_1_C   straight  250.0  0.435  -      101.0  1.2
B_1B_C  bend180    15.7  0.458  -       14.6  -
B_2_C   straight  226.0  0.421  -       66.9  1.7
B_2B_C  bend180    15.7  0.467  -       14.9  -
B_3_C   straight  226.0  0.435  -       19.6  2.6
B_3B_C  bend180    15.7  0.458  -        8.7  -
B_4_C   straight  226.0  0.417  -      195.1  1.6
B_4B_C  bend180    15.7  0.408  -       14.6  -
B_5_C   straight  226.0  0.412  -      109.2  1.8
B_5B_C  bend180    15.7  0.463  -       14.9  -
B_6_C   straight  226.0  0.417  -       83.0  1.6
B_6B_C  bend180    15.7  0.449  -       14.3  -
B_7_C   straight  226.0  0.421  -      106.5  1.9
B_7B_C  bend180    15.7  0.435  -        5.9  -
B_8_C   straight  226.0  0.224  43.9   195.7  2.2   <-- WORST SEGMENT IN THE HEATER
B_8B_C  bend180    18.9  0.435  -       18.5  -
B_9_C   straight  226.0  0.431  -      127.5  1.9
B_9B_C  bend90      9.4  0.431  -        4.0  -

CROSSOVER  (bore 4.635, nominal wall 0.464)
B_1_X   straight  113.0  0.472  -       55.5  0.1
B_1B_X  bend90      9.4  0.481  -        8.3  -

RADIANT  (bore 4.635, nominal wall 0.464)
B_1_R   straight  477.0  0.412  11.2    68.7  1.2
B_1B_R  bend180    18.9  0.417  10.2     4.4  -
B_2_R   straight  477.0  0.394  15.1   235.7  1.7   <-- lowest normal radiant pipe, Pass B
B_2B_R  bend180    18.9  0.490  -       17.6  -
B_3_R   straight  477.0  0.408  12.2   389.2  1.6
B_3B_R  bend180    18.9  0.444   4.3     9.8  -
B_4_R   straight  477.0  0.435   6.2    35.3  2.0   <-- also carries a WELD PUP, see below
B_4B_R  bend180    18.9  0.472  -       17.0  -
B_5_R   straight  477.0  0.403  13.1   220.0  1.1
B_5B_R  bend180    18.9  0.440   5.2    17.8  -
B_6_R   straight  477.0  0.417  10.2   450.3  1.8
B_6B_R  bend180    18.9  0.458   1.3    17.4  -
B_7_R   straight  477.0  0.421   9.2   207.1  1.9
B_7B_R  bend180    18.9  0.431   7.2    17.7  -
B_8_R   straight  477.0  0.449   3.3    81.3  1.9
B_8B_R  bend180    18.9  0.467  -       18.2  -
B_9_R   straight  477.0  0.426   8.2   460.6  1.2
B_9B_R  bend180    18.9  0.435   6.2    17.4  -
B_10_R  straight  477.0  0.412  11.2     7.9  1.1
B_10B_R bend180    18.9  0.458   1.3    17.8  -
B_11_R  straight  477.0  0.431   7.2     0.1  1.6   <-- also carries a WELD PUP, see below
B_11B_R bend180    18.9  0.412  11.2    17.2  -
B_12_R  straight  477.0  0.417  10.2   252.4  1.3
B_12B_R bend180    18.9  0.440   5.2     8.5  -
B_13_R  straight  477.0  0.417  10.2    42.8  1.6
B_13B_R bend180    18.9  0.440   5.2    17.6  -
B_14_R  straight  477.0  0.417  10.2   472.7  1.6
B_14B_R bend180    18.9  0.444   4.3    17.2  -
B_15_R  straight  507.0  0.444   4.3   166.3  1.7   <-- exits at the grade-level outlet
```

**Weld pups — two short inserts, render them as visible features.** Radiant segments 4 and 11
each contain a short section of replacement pipe about 7.3 in long, welded in during a
maintenance turnaround days before the inspection. They have a slightly LARGER internal radius
than the parent tube, so the bore briefly flares out as you fly through. Place them at:
- Segment B_4_R: pup at 39.9 in from the upstream weld, measured wall 0.357 in
- Segment B_11_R: pup at 434.7 in from the upstream weld, measured wall 0.321 in

These read as 23.0% and 30.9% "wall loss" only because they are being compared against the
ORIGINAL tube nominal of 0.464 in. They are brand new steel. This is the single most important
interpretive point in the whole dataset and the app must handle it — see the nominal toggle below.

## Visual design — this needs to look genuinely cinematic, wormhole-energetic, EVERYWHERE

The visual energy of this piece must NOT be gated by data severity. A perfectly healthy stretch
of pipe should look just as alive and impressive as a damaged one — the spectacle is constant;
the inspection data is an accent layer riding on top of it, not the thing generating the
excitement. Do not make "boring" pipe look boring.

**Camera.** Pure first-person POV, moving continuously down the tube centerline, looking ahead
into the tunnel. Add a slow, continuous lazy roll (a few degrees of rotation around the direction
of travel) so the color streaks appear to swirl past rather than sit static — this is a large
part of what makes the reference image feel alive.

**Motion streaks — constant, everywhere, not tied to data.** The dominant visual layer is
radial motion streaks: thin, glowing, elongated strands stretched along the direction of travel,
denser and brighter near the tunnel walls, converging toward a vanishing point ahead of the camera,
in overlapping saturated hues — cyan/teal, orange, purple, magenta/pink, occasional white-hot
highlights. Build this as a large instanced/particle system of stretched quads or thin tubes with
additive blending, continuously spawned ahead and recycled behind, speed-linked to travel speed
so faster playback = more stretched, more intense streaks. This layer runs at full intensity down
the ENTIRE coil, convection and radiant alike, regardless of wall condition at that point — the
goal is that every foot of this thing looks great, not just the damaged spots.

**Ambient particle field.** A secondary layer of small bright points (dust/condensate/debris
suspended in the flow) drifting past at a different speed than the streaks, for parallax depth —
same trick as a hyperspace starfield, scaled to fit inside a ~4.6 in bore.

**The tunnel itself.** Interior surface built as a swept tube along the centerline path with
correct radius per section, high tesselation so bends read smooth. The pipe wall should be
translucent/energetic rather than flat matte steel — let the streak and particle layers behind
and around the pig read through it, with the wall picking up a subtle Fresnel glow at grazing
angles so the tunnel silhouette stays legible even under all the color. Circumferential weld
rings as subtle pulsing bands at every segment boundary — each one is a small "event" the camera
passes through. Bloom via UnrealBloomPass, pushed strong — this piece should feel closer to the
reference image's saturation and glow than to a restrained engineering render.

**Data as an accent layer, toggleable.** This is the "plus," not the core. A control that
overlays the inspection data on top of the wormhole visual without breaking it:
- OFF (default): pure wormhole spectacle as described above, uniform energy the whole 814 ft.
- ON: the streak/particle color near the pig subtly biases toward a data-condition hue —
  cool blue-white in healthy stretches, warming through yellow/orange as remaining wall drops,
  hot red at the worst readings — so the same swirling-streak language now also carries the
  inspection result, rather than switching to a flat painted-wall thickness map. Each segment's
  one recorded minimum, at its one recorded distance from the upstream weld, is the peak of the
  color bias; it blends back to the healthy baseline elsewhere in the segment. Label this
  on-screen as "data-accented" and interpolated between measured minima — never claim it is a
  full measured surface.
- At B_8_C specifically, when data mode is ON, intensify the effect into a genuine set-piece:
  the streaks and particles swarm and thicken low-and-left in the tunnel (7 o'clock position,
  the segment's one recorded clock reading) for nearly the full 226 in, going hot red/orange.
  This is the one segment with real clock data, so it is the one place a directional effect is
  honest. Every other segment has no clock data: keep any data-mode color bias circumferentially
  uniform there, don't invent a side.

**The nominal-basis toggle.** A control with two states, defaulting to "as reported":
- *As reported*: everything computed against the original nominal wall. The two weld pups
  glow red at 23.0% and 30.9% loss and the headline "worst radiant reading" is a pup.
- *Corrected for new steel*: the two weld pups are recomputed as new hardware — show them
  neutral grey with a "new steel, installed 2026-08" tag, and the worst radiant reading becomes
  B_2_R at 0.394 in / 15.1%.
Animate the color transition when toggled. This is the difference between a coil that looks
half destroyed and one in normal condition, and the toggle is the app's most useful feature.

**HUD.** Persistent overlay showing: current segment ID, section name, current bore, remaining
wall at the current position, ovality, distance travelled in feet, and total 814 ft. A thin
progress bar along the bottom with tick marks for section boundaries and a red marker at B_8_C.

**Minimap.** Corner inset rendering the entire coil in wireframe from an external three-quarter
view, with a glowing bead tracking the camera's live position along the path. Without this the
flythrough reads as an abstract tunnel and the viewer loses all sense of place.

**Controls.** Play / pause. Speed slider from 0.25× to 8×. A scrub bar to jump anywhere in the
814 ft. A "jump to B_8_C" button. A direction toggle that reverses the flight — radiant outlet
first, then crossover, then convection — because that is the direction the actual cleaning pigs
travelled. And an "exterior view" button that pulls the camera out of the pipe into a free
OrbitControls orbit of the whole coil, with the tube rendered semi-transparent so the interior
data colors show through, then flies back in on demand.

**Camera behavior on the flythrough.** Constrain the camera to the centerline, look-ahead
tangent to the path. Use a stable up-vector — parallel transport frames or an equivalent — so
the view does NOT roll or flip when passing through the 180° return bends. This is the most
likely thing to go wrong. The bends are tight, roughly one pipe diameter of radius, so the
camera should whip through each 180° reversal in about half a second at 1× speed; that whip is
the best-looking moment in the piece, so make sure it is smooth and not a snap.

**Opening.** Start on the exterior orbit view with the whole coil visible and the title
"F-501 Pass B — 814 ft", then have the camera fly in through the convection inlet and hand off
to the flythrough. One continuous move, no cut.

## Hard constraints

- Use only the numbers given above. Do not invent segments, readings, clock positions or
  colors for data that is not present. Where a value is a dash, show it as "not recorded".
- The path must contain exactly 25 straight segments and 24 bends and total 814 ft.
- Include a short "About this data" panel: source is Steady Flux Technologies intelligent pig
  report 26-0663-002 Rev. A, inspection 2026-08-13, ExxonMobil Baytown HU5A F-501, Pass B.
  Note that no minimum allowable wall thickness threshold was provided by the owner, so the app
  makes no fitness-for-service judgement and shows condition only.
- Dark UI. No missions, no score, no gamification. This is an engineering visualization that
  happens to look like a ride.

---

## Follow-up prompts if the first pass falls short

Send these one at a time, in this order, only for what actually broke:

1. "The camera rolls or flips at the return bends. Rebuild the camera frame using parallel
   transport along the path so the up-vector stays stable through the 180° reversals."
2. "The path does not close correctly at the crossover. The two 9.4 in bends are 90° elbows,
   not 180° return bends. Rebuild those two and re-verify total path length is 814 ft."
3. "Add the interior wall data coloring — right now the tube is a uniform material. Color by
   remaining wall thickness on a 0.20–0.60 in scale, with the recorded minimum for each
   segment placed at its recorded distance from the upstream weld."
4. "Add the minimap inset and the HUD."
5. "Add the nominal-basis toggle for the two radiant weld pups."
