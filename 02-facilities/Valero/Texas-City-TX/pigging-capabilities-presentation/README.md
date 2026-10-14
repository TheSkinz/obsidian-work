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
  - `prep_cover.js` renders `img/cover_night.jpg` from `src/trimax6_night.jpg` (Jesse's AI background replacement of the real TriMax 6 photo; rig real, night tank-farm background generated) and `img/card_ready.jpg` from OneDrive `Marathon Carson RFQ/_Presentation photos/IMG_1973` (real TriMax 4, front closest).
  - `prep_slots.js` renders the photo crops:
    - Services panel: from `src/onsite_heater.jpg`, with the concrete foreground cropped off.
    - (The readiness card is made in prep_cover.js. The LAR `trimax6.jpg` and `slot_ready.jpg` are the same TriMax 6 shot as the cover, so they aren't used.)
    - Capabilities card: the LAR `hero.jpg`.
    - TriMax slide (full bleed): `src/trimax1_dusk.jpg`, Jesse's AI background replacement of the real TriMax 1 yard photo (rig real, dusk refinery generated).
    - Closing card: `src/road_night.jpg`, Jesse's AI background replacement of the real road photo. The rig is real; only the night terminal background is generated. Fully generated rig images were rejected.
  - `src/` holds the original photos the crops are made from.
  - `img/` holds the processed images. Each photo appears on exactly one slide (Jesse, 2026-10-13). Landscape photos sit in landscape cards, never in tall blur-filled panels, so the rig fills the frame. The agenda and Q&A slides have no photo because there aren't enough distinct photos to go round.

**Status: final, cleared by Jesse and Jason (2026-10-13).** "Same day" response and "largest triple-pass fleet" are confirmed with Jason. The references slide (21) claims **14 heaters at 5 Valero refineries**, built from Jesse's verified heater list (2026-10-13) plus the Texas City coker heater, which Jesse confirmed. The other Valero sites a Copilot SharePoint pull suggested are left off. Three entries were dropped as doubtful:
  - Port Arthur AVU-146: the unit name of the H-102A/B job, so it would double count.
  - Port Arthur B-301: the only vault record is USA26056 passivation support, not a cleaning.
  - The Copilot-sourced 2022 Texas City F501-A and H2 heater jobs: Exxon Baytown has its own 2022 F-501 decoke, so they may be conflated.

The Texas City row reads "Coker heater", with no tag and no year. Jesse ruled H-57 off the deck on 2026-10-13. Don't reintroduce the H-57 tag or the Copilot "Coker C B-301" label. The org chart (slide 10) and the safety stats (slide 18) match the LAR deck by design (Jesse, 2026-10-13). On slide 10, Jason is highlighted as presenter instead of Marshall.

Case study (slide 22): Valero Port Arthur [[H-102A]] / [[H-102B]], USA26025. The figures come from those cards. Cost, overrun and the emergency framing are deliberately left out.

To rebuild:
1. Install the dependencies **outside the vault**, because `node_modules` isn't gitignored: `npm install` in a scratch folder, using this `package.json`.
2. From `build/`, run `NODE_PATH=<scratch>/node_modules node prep_map.js`, then `NODE_PATH=<scratch>/node_modules node build.js`.
3. Render the PDF with `soffice.exe --headless --convert-to pdf`.
