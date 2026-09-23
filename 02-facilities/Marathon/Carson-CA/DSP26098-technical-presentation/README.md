---
type: reference
facility: Marathon-Carson-CA
client: Marathon
quote-number: DSP26098
source: "Built in Claude Code session 2026-09-23 from DSP#26098 Rev 1, the LAR RFI responses, the TriMax brochure and video, CARB certificates, and Jesse's field photos"
verified: 2026-09-23
tags: [Marathon, presentation]
---

# DSP26098: LAR technical proposal presentation

The Marathon Los Angeles Refinery (Carson Coker #1 and #2, Wilmington DCU H-101) technical-proposal presentation for the MPC evaluation team: 40 minutes plus 20 minutes of Q&A. Presented by Marshall Douglas, September 2026. The underlying bid is Jason Harman's DSP#26098 Rev 1 (lump sum, mob/demob waived, 60 decokes over five years).

- `LAR_Technical_Proposal_Presentation.pptx`: the deck, 25 slides, with speaker notes on every slide (about 38 minutes). Slides 24 and 25 are the appendix: MPC references and the pump curves.
- `LAR_Technical_Proposal_Presentation.pdf`: a PDF render of the deck.
- [[LAR_QA_Prep_Notes]]: internal presenter prep. It lists where the submitted proposal disagrees with itself or with the heater-card drawings, the CARB notes, and the framing settled in the 2026-09-23 audit. It isn't customer-facing.
- `build/`: the pptxgenjs generator (`build.js`) and image prep scripts, plus the processed images in `img/`. To rebuild: `npm install pptxgenjs sharp react react-dom react-icons us-atlas topojson-client d3-geo`, then `node build.js`. `prep.js` and `prep3.js` read the original photos from a Claude session upload folder that no longer exists, so re-running those needs the originals re-pointed. `build.js` alone uses only `img/`.

Heater data for this site is on [[RW-0014-214.9]] and [[RW-0015-214.09]]. The deck repeats the proposal's Technical Data page verbatim, so where it and the drawing-derived cards disagree, the prep notes list the difference.
