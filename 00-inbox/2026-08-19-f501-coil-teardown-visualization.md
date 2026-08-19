---
type: note
status: inbox
created: 2026-08-19
tags: [F-501, USA26041, ExxonMobil, smart-pig, visualization, grok, llm-tooling]
related: [[F-501]], [[USA26041-job-report]]
---

# F-501 Pass B coil teardown — 3D visualization built, Grok Build test never ran

Side project, 2026-08-19. Started as "brainstorm ideas to build in Grok Build against the
Steady Flux smart-pig report," ended with the thing built here instead.

**What exists.** A self-contained 3D visualization of **F-501 Pass B**, built to true scale from
`26-0663-002 Rev. A` — 25 straights, 24 bends, 9,768 in / 814 ft, which reconciles against the
card's measured 1,631–1,632 ft for the two-pass A/B circuit. It runs an automatic camera tour:
continuous slow orbit of the whole coil, dolly in to each of four flagged locations, hold and
orbit, dolly back out, drift to the next.

The four stops are **B_8_C** (0.224 in of a 0.400 in wall, 43.9%, at the 7:00 clock position),
**B_2_R** (0.394 in, 15.1%, the lowest reading in *original* radiant pipe), and the two weld pups
**B_4_R** and **B_11_R**.

- **Live:** https://claude.ai/code/artifact/d9227a70-78e3-4a0b-8df7-8e7deab9ed8b
- **Source:** `00-inbox/f501-coil-teardown-source.html` — the maintainable file. It expects
  `three.min.js` (r160) spliced in at the `<!--THREEJS_INLINE_HERE-->` marker; the published
  artifact is that splice, ~709 KB, no external requests.

**Two features worth keeping in mind, because they encode judgements from the card.**

*Nominal-basis toggle.* Defaults to "as reported," where the two weld pups read 23.0% and 30.9%
loss. Flip it and they render as new steel with no loss, because they are 7.3 in inserts welded in
during the August 2026 TA and the report computes them against the original 0.464 in nominal.
This is the card's "do not let the 45.7% figure travel without context" point made visual.

*Wall drawn to measurement.* In close-up the bore is drawn at (outer radius − measured wall), so
the gap between the inner surface and the translucent outer skin **is** the metal that is left.
It is geometry carrying the data, not colour alone.

**Stated on the page, deliberately:** each segment carries one recorded minimum at one recorded
distance from its upstream weld, so everything between those points is interpolated and is not a
measured thickness map; only B_8_C has a recorded clock position; and no minimum allowable wall
threshold was provided by the owner, so it makes no fitness-for-service call.

## Open

**The Grok Build comparison never happened.** That was the original point of the session. The
prompt is written and preserved at `07-llms/grok/f501-coil-flythrough-build-prompt.md` — it carries
the full Pass B segment table inline so Grok never has to extract from the 36-page PDF. It targets
the *earlier* interior-POV concept, which was abandoned here after building it proved a 4.6 in bore
is a featureless cylinder with nothing in it to look at. If the Grok test is still wanted, the
prompt should be re-pointed at the exterior-teardown choreography first.

**No MP4 was recorded.** The page has a working recorder that composites the 3D and the HTML
overlay into one canvas and writes an MP4, but page-initiated downloads are blocked in the artifact
sandbox, so the button only appears when the file is served locally. Recording it again means
re-serving `f501-coil-teardown-source.html` (with three.js spliced) over `http://localhost` and
clicking **record tour** with the tab kept in front — a hidden tab does not composite frames and
captures nothing.
