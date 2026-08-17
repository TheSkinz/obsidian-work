# Rig Diagram — back-test prototype

**Status: back-test evidence, not production tooling.** Filed so it is not lost the way the
March 2026 draw.io export was. The build/no-build decision is
[[2026-08-16-backtest-rig-diagram-layout-engine]]; nothing here should be used on a live job
until that is signed off.

## What it is

`rig-diagram.html` renders a single-Trimax rig / hose layout from a `JOB` data object at the
top of its script. Everything below that object is generic machinery — **there is not one
hand-placed coordinate in the file.**

- Blocks are placed by CSS grid and flex.
- Wires are derived from measured element rects at draw time and emitted as **H/V segments
  only** — `ortho()` structurally cannot produce a diagonal.
- Heater ports are drawn at the measured centre line of their own launcher/receiver box, so
  they cannot drift out of alignment with it.
- Pumps and L/R pairs are emitted from the same ordered `circuits` list, so pump stack order
  matches launcher order top-to-bottom by construction.
- Which blocks exist (filter press + transfer pump, vs. a drain to coke pit / sewer) is a
  data question, driven off `filtration` and `waterSource`.
- Jetting hoses run as a **planar fan** — one lane per run, ordered by launcher height, with
  sources ordered to match. Two hoses structurally cannot cross, and this holds unchanged at
  F-802's ten launchers.

**It encodes the drawing rules in [[rig-diagram-corpus]]**, which came from Jesse's review of an
earlier render: the frac tank is off-system and separated, launchers bolt to the heater flanges
(one hose run, not two), the Trimax never out-scales the heater, and return flow points back
into the pump. A renderer cannot infer any of those — they are domain facts.

## Render

```bash
chrome.exe --headless --disable-gpu --no-pdf-header-footer --virtual-time-budget=8000 --print-to-pdf="out.pdf" "file:///<abs-path>/rig-diagram.html"
```

Same headless-Chrome route the job sheets use (`04-knowledge/_canonical-job-sheet.md`).
`--virtual-time-budget` is required: the wires are drawn by script, and without it Chrome
prints before layout settles. Append `#debug` to the URL for a rect dump.

## Proofs in this folder

- `backtest-f901-filtration.pdf` — F-901 as shipped (1 Trimax, triple mode, 3 passes, 6 L/R,
  filtration elected).
- `backtest-f901-no-filtration.pdf` — the same file with **two data fields changed**
  (`filtration: false`, `waterSource: hydrant`). The press and transfer pump disappear, a
  coke-pit/sewer drain block appears, and the effluent re-routes. No geometry was edited.

Note the rendered `Max Pig OD` reads **5.25"**, the rule-correct figure from the heater card —
not the 5.5" that the shipped F-901 diagram and SOP-DCK-F901-001 REV 0 both carry in error.

## Known limitations

**Dual-Trimax is not implemented and not tested.** Both F-802 and 70H1 run two units, and that
is precisely the case where a frozen-template approach gets expensive and a computed layout
should pull ahead. Until it is proven, the back-test result is partial.

**The diverter is not drawn.** The hand-made originals show it — 90° plunger, operator-controlled
from the cab, routing return water to the clean or dirty tank on clarity. Its absence
misrepresents how the loop actually works and it should be added before this is used for
anything real.

**Looped passes are drawn as single runs.** F-901 Pass 1 is two coils looped via JS-1; the
render shows one straight run like the other two.
