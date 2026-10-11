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

**Open:**
- Jesse scores blind and picks a direction.
- B needs a sharper field photo; the current one is about 134 dpi at full width.
- Fix the "USADeBusk Services" dead string in the real template.
