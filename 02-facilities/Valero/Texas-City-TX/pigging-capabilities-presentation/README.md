---
type: reference
facility: Valero-Texas-City-TX
client: Valero
source: "Built in Claude Code session 2026-10-13 by forking the DSP26098 Marathon LAR deck generator; Valero case study from the H-102A/H-102B cards (USA26025); reference-site list supplied by Jesse 2026-10-13, partly unconfirmed"
verified: never
tags: [Valero, presentation]
---

# Valero Texas City: pigging capabilities presentation

A general heater pigging and decoking presentation for the Valero Texas City site. It is not tied to a bid. Jason Harman presents it, October 2026. It is forked from the Marathon LAR deck (`02-facilities/Marathon/Carson-CA/DSP26098-technical-presentation/`). Company-level slides carry over unchanged. The LAR heater data, five-year program, CARB fleet slide and MPC contacts are dropped. The scope, pig progression, coil controls, execution, emergency response, references and case study slides are rewritten for Texas City.

- `Valero_TXC_Pigging_Capabilities.pptx`: the deck, 24 slides, with speaker notes on every slide (about 30 minutes plus Q&A).
- `Valero_TXC_Pigging_Capabilities.pdf`: a PDF render of the deck.
- `build/`:
  - `build.js` is the pptxgenjs generator.
  - `prep_map.js` renders `img/valero_map.png`.
  - `img/` holds the processed images copied from the LAR build.

**Status: draft specimen, not cleared for release.** Slide 21's reference map carries a DRAFT note and asterisks on sites that are unconfirmed: Oklahoma City, Houston and both Diamond Green Diesel sites. The headline count of 15 includes them. Confirm or cut them, then remove the DRAFT line and the asterisks before the deck goes to Valero. The org chart (slide 10) is the LAR team unchanged, with Jason highlighted.

Case study (slide 22): Valero Port Arthur [[H-102A]] / [[H-102B]], USA26025. The figures come from those cards. Cost, overrun and the emergency framing are deliberately left out.

To rebuild:
1. Install the dependencies **outside the vault**, because `node_modules` isn't gitignored: `npm install` in a scratch folder, using this `package.json`.
2. From `build/`, run `NODE_PATH=<scratch>/node_modules node prep_map.js`, then `NODE_PATH=<scratch>/node_modules node build.js`.
3. Render the PDF with `soffice.exe --headless --convert-to pdf`.
