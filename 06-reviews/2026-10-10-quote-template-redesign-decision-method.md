---
type: review
status: resolved
review_type: decision-method
source_authority: stated
confidence: high
created: 2026-10-10
related:
  - "[[2026-10-09-seed-redesign-quote-template]]"
---

# Quote template redesign: decision method

This review records the method for choosing the redesigned USADebusk quote/proposal template. It is a method only, and no template was built in the session that produced it. The rulings marked as Jesse's were given in that session. The rest is the agreed approach.

## Why the 10-08 redesign was reverted (Jesse)

The DSP26112–26114 branded rebuild (commits `1a88147` and `22f326e`) **wasn't visually impressive** and came at **the wrong moment**, the night before three live Valero quotes. It was a design failure. Approval politics had nothing to do with it. The rebuild was overwritten on 2026-10-09 and no longer exists on disk.

## What reads as amateur in the current template (Jesse, read off DSP26115)

He means all of it. Margins are uneven on every page. The images look homemade. The cover is stock geometric bands with stacked logos. Every page carries a gold header band that fades into a photo. The Execution Plan and Quotation pages are raster workup screenshots: the PDF text layer on the Quotation page is 50 characters, and that is why `presend_gate.py` returned CANNOT JUDGE. Body text is Arial while the rates table and footer are Calibri, and the footer shows a letter-spaced "P a g e". The screenshots also carry dead strings to the customer ("TriMax", "USADeBusk").

## Ownership and scope (Jesse)

Jesse makes the final decision. Jason and Travis have to like it and approve it before they start using it, so someone other than Jesse must be able to modify the template or start a quote from it with no script. Sections 10–14 (boilerplate and marketing pages) are restyled only, with the same content. Section order stays as `usadebusk-estimating` defines it.

## Format rulings

| Decision | Ruling | Why |
|---|---|---|
| Word vs generated PDF | Word `.dotx` on named styles is the master, and the PDF is exported from Word. `render_proposal.py` later fills the template and stops owning the layout. | Others must be able to edit it. A script-only format fails that. |
| Native tables vs screenshots | Native Word tables for Execution Plan, Quotation and Rates. | They fix the off-brand pages, and the exported PDF has a text layer the gate can read. |
| One template vs per-customer | One template, with a customer-logo slot. | Variants multiply what has to be approved and maintained. |

## Evaluation criteria

**Gates, all pass/fail, run before design judgement.** G1: the Word→PDF export through `presend_gate.py` returns exit 0 or 1, never 2. G2: every element is a named paragraph or table style, with no text boxes and no images standing in for text. G3: colours and type come from the `usadebusk-core` Brand Standards, and any brand change is named explicitly and mirrored to `07-llms/grok/bot-setup/skills/brand-standards.md`. G4: content is frozen, with the same words, numbers and section order as the source quote.

**Scored 1–5, weighted.** Visual impression to a refinery buyer on cover and Quotation in the first 10 seconds, 40%. Number legibility (total and line items findable in 3 seconds), 20%. Consistency (one margin grid and type scale, no half-empty pages), 20%. Production effort (Jesse's time per quote, and a from-scratch quote by someone else), 20%. Speed is a floor: no direction may be slower to produce than today. Above that floor, looks win.

**Discipline.** Jesse scores blind before seeing the builder's scores. The builder's self-assessment is not a review.

## Comparison

Three directions, each a 2-page specimen (Cover + Quotation) on the frozen DSP26115 content ($28,637.35). All are **built in Word and exported to PDF**, the target medium. An HTML mockup could promise layout Word can't deliver.

- **A, Refined corporate:** white page, thin gold rule, strong left-aligned type, generous fixed margins.
- **B, Bold:** charcoal cover with a full-bleed field photo and gold accents. Body pages stay clean.
- **C, Engineering data-sheet:** strict grid and a document-control block (quote #, rev, date, valid until).

The comparison sheet sets the current template's same two pages beside A/B/C, with gate results and the score table.

## Approval sequence

`Jesse picks direction (blind) → full 17-page build on a past/dead quote → Jesse sign-off → Jason + Travis review old vs new side by side → first use on a non-urgent bid → default`

**A new template never debuts on a bid due the same or next day.**

## Next step

Build the three specimens in Word from DSP26115 and export them with soffice.exe directly. Run G1–G4 on each, assemble the comparison sheet, and hand it to Jesse for blind scoring.

## Round 1 built (2026-10-10)

Three Cover + Quotation specimens (A Refined, B Bold, C Data sheet) were built on **DSP26112, the Wilmington 20H200 decoke** instead of DSP26115 (Jesse's call). The gate didn't recognise DSP26115's "Passivation Support" line. All three were exported **through Word**, not soffice: the real workflow exports from Word, and the gate verdicts have to hold on that PDF.

- Files: `OneDrive/USADeBusk/Company/Quote Template Redesign 2026-10/` holds the `.docx`, the `.pdf`, the comparison sheet and `build/` (docx-js scripts, `gates.py`, `word2pdf.ps1`).
- Comparison sheet: https://claude.ai/artifact/3TuJdNtT6e9auE17GVVmif
- Gates (tool output, not predictions):
  - G1: all three return SEND with a $0.00 gap. With Labor raised $100, each blocks.
  - G2: all pass.
  - G3: all pass, but each adds one rule/grid grey that the brand table doesn't define.
  - G4: all pass, 31/31 values.
- My scores (A 4.0, B 4.6, C 4.0) sit hidden in the sheet until Jesse has scored.

The gate needed three fixes before G1 could pass on any design:
- config `21d82dd`: the extractor was reading the new `Rate Sheet` tab.
- config `ab145f8`: xpdf `-layout` misplaces native-table amounts. The gate now retries with `-table`, and it strips leading item numbers.

Template rules learned:
- Never letter-space a label the gate reads ("Pricing Summary" comes out as "P R I C I N G").
- Keep each line item's label, text and amount in one table row.

## Round 2 strategy (2026-10-10, evening)

Jesse superseded round 1 with a reference he likes: a commercial "Web Design Proposal" template with a charcoal and gold diagonal cover, a black-and-white photo in a slanted frame, a grey title strip on every page, a pricing table ending in a dark total box, and a gantt with gold cells.

Rulings:
- **References are inspiration only.** No template purchase.
- **The art tooling call is mine.** I draw geometric art in code with exact brand hex, use real USADebusk photos, and never use AI image generation for equipment or people.

Revised G2: decorative art may be anchored behind cover text or sit in the header/footer layer. Variable content never sits in images, text boxes or shapes.

Harvest: Jesse's example plus 15 Behance references, broken into parts to tick, at https://claude.ai/artifact/LGNnfYucvXRpLcHszwPaQb. Next comes Direction D, three pages (Cover, Execution Plan as a gantt, Quotation), built from his picks. It needs one sharp landscape photo, at least 2400 px wide, of a Trimax on site; the OneDrive inventory has none.

## Round 2 concepts (2026-10-11)

**Jesse's mood-board picks:**

| Element | Pick |
|---|---|
| Page header | R11 |
| Pricing table | R3, R11 |
| Total callout | R3 |
| Schedule | his example's gold-cell gantt |
| Data tables | R3, R8 |
| Photo treatment | his example |
| Typography | his example, R5 |
| Cover | none picked |

He then supplied his own image-generated concept: a dark refinery cover, black title bands with a gold slash, timeline dots, an hours bar and a gold total box. Its figures ($98,134.26, 80 hrs) match no DSP26071 revision. The concepts use the real **DSP26071.2 Rev 2 ($60,287.42, 48 hrs)**, with execution dates corrected to 2026.

**Three concepts, each Cover + Execution Plan + Quotation, built in Word:**
1. His design made real.
2. A blend: reference cover, R11 numbered headers, R3 tables, gold-cell gantt in 4-hour cells.
3. A light contrast version.

Photos are placeholders. Jesse says his current photos are all from bad angles.

**Results:**
- All three return SEND with a $0.00 gap, and each $100-tampered copy blocks.
- Revised G2 passes: one behind-text cover image, no text boxes.
- 36/36 values present.

**Locations:**
- Sheet: https://claude.ai/artifact/CoqSdjjXSXLmTRdbrkqeRe
- Files: `OneDrive/USADeBusk/Company/Quote Template Redesign 2026-10/Round 2 Concepts/` (with `build/`)

**Jesse's goal for the final template (2026-10-11):** a blank template where adjustments are easy to make.

**Planned mechanics:**
- Art is a swappable behind-text layer.
- All words and numbers sit in styles and tables.
- Word content controls are used for fill-in fields.
- Picture content controls let anyone replace a photo.

The real DSP26071.2 summary folds mob into Equipment and demob into Manpower, with no Mob/Demob row. That is Jason's convention, and the concepts keep it.

## Direction D: Jesse's picks (2026-10-11)

Jesse picked **cover 1, Execution Plan 2 and Quotation 1**. He leans toward concept 1 overall, finds 2 OK and 3 mediocre.

Direction D combines them: the concept-2 gantt is restyled in concept 1's black-band look. The cover uses a real photo from the Marathon LAR technical-proposal deck (`Marathon Carson RFQ/_Bids/Marathon_LAR_Technical_Proposal_DRAFT.pptx`, `image-1-1.jpeg`): the Trimax in front of coke-drum derricks. It is graded so everything but the yellow goes grey, the sky is darkened behind the logo, and the bottom fades to black (`build/cover_photo.py`).

Checks: SEND with a $0.00 gap, and the $100-tampered copy blocks. Files are `Round 2 Concepts/DirectionD_Picks.pdf` and `.docx`.

The deck holds only two real photos. The other is the crew walking past the unit (`image-18-1.jpeg`), a black-and-white accent candidate. Jesse says finding more photos will take a while.

## Photo pipeline and cover options (2026-10-11)

Jesse rejected the LAR coker shot because the trailer's rear is closest to the camera; he wants the front end nearest with the name readable (memory `feedback-cover-photo-angle`). The Canadian branding on the unit is fine (Jesse).

**Local GPU photo pipeline built:** `C:\Users\Jwuts\photo-pipeline\` (scripts copied to `Round 2 Concepts/build/photos/` with a README). It runs on the RX 9070 XT via ROCm PyTorch:
- Real-ESRGAN x4 upscaling;
- BiRefNet matting, which must run in fp32 because fp16 returns an empty mask;
- SDXL inpainting, used only to erase.

Generated backdrops looked CGI and were dropped in favour of real plates.

**Hard rule:** the unit is never inside a generative mask. The check is a pixel diff inside the matte, and it now refuses to pass on an empty mask. The first run passed vacuously on one.

**Photo inventory:** 207 images screened. Best found:
- #106, `Marathon Carson RFQ/_Presentation photos/IMG_1973-UPDATED-USADEBUSK-scaled.jpg`: the Trimax at a refinery with its front closest.
- #107: the "Pigging in Progress" sign.
- `Valero Meraux LA/_History/Pigs.jpg`: decoking pigs.
- The Casper heater photos, which serve as plates.

**Cover options:** `DirectionD_coverH1/H2/H3.pdf`.
- **H1:** #106 as a band, barricade erased.
- **H2:** the phone-photo unit composited on the blurred LAR coker derricks.
- **H3:** the same unit on a blurred Casper heater structure.

Unit diff: 0.0, 0.10 and 0.10 levels. All three return SEND. Inside-page accents (sign, crew, pigs) are ready.

**Open:**
- Jesse picks a cover, then the full blank template gets built from Direction D.
- Safe / Fast / Sustainable cover wording needs Jason's agreement.
- Fix the "USADeBusk Services" dead string in the real template.
