---
type: concept
status: draft
source_authority: secondary
confidence: medium
created: 2026-07-19
last_reviewed: 2026-07-19
tags: [workflow, quotes, estimating]
---

# RFQ Intake Protocol

## Scope

This governs the front half of a bid: from the moment an RFQ lands in your inbox to the moment the proposal is submitted and the vault records it. [[quote-lifecycle]] picks up from there — what happens when the quote is decided, and how an award becomes a job.

It does not govern proposal *content*. Section composition, the intake checklist, pricing structure, and duration math are canonical in the `usadebusk-estimating` skill and are referenced here, not restated.

## Current Rule / Knowledge

### 1. Land the source documents

Keep the RFQ package — contract terms, bid instructions, drawings, data sheets — intact and unrenamed in that facility's own OneDrive folder, alongside everything else for that site. Do not build a separate RFQ tree; the per-facility layout already mirrors the vault's `02-facilities/<Client>/<City-ST>/` shape, and a parallel structure is a second system to maintain for no retrieval gain.

The vault is the index, OneDrive is the store. What makes this work is not the folder layout but the link between them: the full path **must** be recorded in the quote note's `## Source Files` section, as DSP26058, DSP26039, and DSP25084 all do. An unrecorded path is how a bid trail goes cold. Note the path is the only pointer — nothing syncs, and moving the folder later silently breaks it.

### 2. Assign the DSP# and open the quote note

DSP##### = DSP + YYNNN, assigned at proposal start, before any work product exists. Create `02-facilities/<Client>/<City-ST>/DSP#####.md` immediately with `status: pending` and the frontmatter block from [[quote-lifecycle]]'s numbering section. Everything downstream keys off this number. If the facility folder doesn't exist yet, create it from `04-knowledge/_facility-template.md`.

### 3. Recon the vault before extracting anything

Read, in this order: the site's `_facility.md` for access, site constraints, and equipment limits; any existing heater card for a tag named in the RFQ; and `04-knowledge/estimating-actuals-rollup.md`.

**Rates do not come from the facility card.** They are a property of the contract, and one site can carry several concurrent contracts at different rates — see the frontmatter fields in [[quote-lifecycle]]. Read prior quote notes at that site for what was charged before, treating each as one contract's rates rather than the site's rates, and take the governing figures from the contract or bid instructions for this opportunity. Where facility cards do carry a rates block, it is labeled with the specific quote it came from and should be read that way. A repeat heater with recorded Task Durations means durations come from that heater's actuals, not from the 6/6/4 generic defaults — verified numbers govern. Consult `INDEX.md` before concluding a facility or heater isn't already in the vault.

### 4. Extract drawings into the heater card, not the proposal

Drawing and data-sheet extraction produces or updates a heater card conforming to [[_canonical-heater-card]]. The proposal's Section 5 Technical Data table is then read *from the card*. This ordering is what keeps the vault and the client-facing document from drifting apart.

Expect several correction rounds before a tube count is trustworthy. Full-PDF context is useful for orientation, but BOM tables must be extracted from targeted snippets — full-document passes misread them.

### 5. Run the intake checklist and honor the incomplete-input gate

Work the 17-item RFQ Intake list in `usadebusk-estimating`. Whatever the drawings did not answer becomes an explicit clarification request back to the customer. Do not price past the gate. Contract rates and applicable third-party markup are the two most commonly missing items and both move the number materially.

### 6. Review contract terms and bid instructions as a separate pass

This is the pass that loses bids on technicalities rather than on price, and it is independent of the technical estimate. Confirm the submission platform (ARIBA, GED, or direct email), the due date with time zone, required forms and attachments, insurance and safety qualification requirements, whether pricing must be submitted on the customer's own sheet, and any page or format constraints.

Then read the commercial terms against how USADeBusk actually bills, and flag conflicts *before* pricing rather than after: a stand-by definition narrower than the two-rate-line model, a markup cap below the contract rate, payment terms longer than 30 days, a lump-sum mandate where T&M is standard, or liability and indemnity language outside the norm. Where a term genuinely cannot be met, raise it as a clarification or exception in the bid, not silently in the pricing.

### 7. Build durations, then price

Duration math is shown explicitly for Jesse's verification before the Execution Plan is finalized. Line-item hour × rate calculations go in a working note before the Quotation table is produced. Mob and demob are costed per the four-part model in the skill, off Deer Park one-way miles.

### 8. Generate and submit

Follow the 14-section proposal structure in `usadebusk-estimating`. Submit per the platform the bid instructions named.

### 9. Close the loop in the vault

Fill in the quote note: scope summary, technical timeline, equipment and manpower, pricing, hourly rates, internal financials, pig specifications, source-file paths, and any controlling-date conflicts found in the workbook. Add the row to the Pending/Bidding table in `01-context/active-jobs.md`. Commit the quote note, the heater card(s), and any facility updates together.

## Source Basis

| Source | Authority | Date | Notes |
|---|---|---|---|
| `usadebusk-estimating` skill | Primary | 2026-06-15 | Intake checklist, section order, pricing structure, duration model |
| [[quote-lifecycle]] | Primary | — | Back half of the lifecycle; numbering convention |
| `02-facilities/Marathon/Garyville-LA/DSP26058.md` | Observed practice | 2026-05-12 | Quote-note schema exemplar; source-file path convention |
| Session with Jesse | Primary | 2026-07-19 | Protocol assembled and approved; steps 1, 6, 9 identified as the undocumented gap |

## Exceptions

Emergency decokes compress steps 1 through 6 into a single call — the customer often has no formal bid instructions and no drawings. Capture what you can verbally, state assumptions explicitly in the proposal, and treat the technical data as unverified until a heater card is built post-award.

## Open Questions

- The **existing-contract estimate** — the common case, where there is no bid packet and the scope is priced against a known regime — has no documented fast path. No longer blocked: under the corrected rate model it reads `rate-basis` off the prior quote rather than depending on a facility rate schedule. Write it against a real estimate rather than speculatively.
- Whether the `_pipeline.md` Dataview dashboard referenced in [[quote-lifecycle]] exists — no such file is present in the vault as of 2026-07-19, so the Pending/Bidding table in `active-jobs.md` is the only working pipeline view.

## Change Log

| Date | Change | Trigger |
|---|---|---|
| 2026-07-19 | Note created | Gap identified in session — no written intake protocol existed; document intake, contract-terms review, and vault write-back were uncovered by any skill |
