---
type: review
status: resolved
review_type: contradiction
source_authority: inferred
confidence: medium
created: 2026-07-19
review_after: 2026-08-19
related:
  - rfq-intake-protocol
  - quote-lifecycle
tags: [review, knowledge-system, pricing, estimating]
---

# Review — Rate model is stored at the wrong grain (facility, should be contract)

## Trigger

Session 2026-07-19. While documenting the RFQ intake protocol, step 3 assumed contracted rates could be read from the site's `_facility.md`. Recon showed that step does not work, and the follow-up with Jesse showed *why* it cannot work as designed: the vault models rates as a property of a facility, but rates are actually a property of a contract, and one facility can carry several concurrent contracts with different rates.

## Source Material

| Source | Authority | Notes |
|---|---|---|
| Jesse, in session 2026-07-19 | Primary | Contracts are issued per-opportunity by different departments (turnaround, maintenance, procurement, capital projects). Most are short scope-specific contracts that end with the project. Multi-year (≈3 yr) maintenance agreements exist but are rare, and one can cover many bids. Rates are also deliberately adjusted per bid to stay competitive. |
| `02-facilities/ExxonMobil/Baytown-TX/_facility.md` | Observed | Carries `## Contracted Rates — PS8 F-802 (DSP25084 Rev 2)` with an inline warning: "No rate schedule found for DSP26039 — confirm applicability before quoting that job at these rates." A schema problem written as a caution note. |
| `02-facilities/Marathon/Garyville-LA/_facility.md` | Observed | No rates section at all. |
| `04-knowledge/pricing/Rate Reference.md` | Observed | Frames the model as "base rates, overridden per facility." Every rate cell is blank. Its own 2026-07-06 note records that no company-wide base schedule exists. |
| `04-knowledge/pricing/_cost-model.md` | Observed | Complete empty skeleton — every internal cost, markup, and mob/demob cell blank. |
| `DSP26058.md`, `DSP26039.md`, `DSP25084.md` | Observed | Each already carries its own full rate table. DSP26058 additionally carries a real Internal Financials block: revenue/cost/margin by category, 44.3% blended, plus per-heater margins. |

## Proposed Change

### A. Do not backfill contracted rates onto facility cards

Reverses the recommendation made earlier in the same session. The facility is the wrong grain; backfilling would encode the modeling error more deeply and create exactly the ambiguity the Baytown warning is compensating for. Existing facility rate blocks stay as historical record but should be relabeled with the contract or quote they belong to.

- [x] Approved
- [ ] Approved with edits
- [ ] Rejected
- [ ] Needs more source material

### B. Short scope-specific contracts — change nothing

Where a contract covers one scope and ends with the project, there is no reusable rate schedule, and recording those rates anywhere but the quote note actively misleads the next bid at that site. All three existing quote notes already do the right thing. No new structure.

- [x] Approved
- [ ] Approved with edits
- [ ] Rejected
- [ ] Needs more source material

### C. Multi-year agreements — one contract note per agreement

Only where a rate schedule genuinely spans many future bids. One note per contract in the facility folder alongside the quotes, carrying term dates, scope boundary, rate schedule, markup, and contract type. Quotes point at it.

**Deferred pending confirmation that a live multi-year agreement actually exists.** If none is currently active, this is speculative and should not be built — write it when the first one lands.

**Rejected 2026-07-19 — not on merit.** Jesse confirmed multi-year agreements exist in the industry but none are on the accounts he currently works. Building the note type now would be structure for a hypothetical. **Revisit trigger:** the first bid that arrives under a multi-year or master agreement. Until then `rate-basis: quote-specific` covers every quote.

- [ ] Approved
- [ ] Approved with edits
- [x] Rejected
- [ ] Needs more source material

### D. Add `contract-type` to quote frontmatter (not `department`)

The session first proposed recording the issuing department, on the theory that it explains rate divergence at a single site. Jesse's counter — that the **contract type / terms** is what the bid instructions actually state, and is the more useful field — is the better call and is adopted here.

Contract type changes estimating behavior: it determines billing basis (T&M vs. lump sum), whether stand-by is billable and at what scope, markup treatment, and whether the rates carry to the next opportunity. Department changes none of those; it only correlates with them. Recording the discriminator itself beats recording a proxy for it.

Proposed fields on the quote note:

| Field | Purpose | Example values |
|---|---|---|
| `contract-type` | The contract/terms form stated in the bid instructions | short-form scope contract, multi-year maintenance agreement, MSA call-off, purchase-order only |
| `rate-basis` | Where this quote's rates came from | `quote-specific`, or a link to the contract note from (C) |
| `billing-basis` | Commercial structure | `T&M + LS mob/demob`, `lump sum`, etc. |

Vocabulary for `contract-type` is not yet settled and should be drawn from real bid instructions rather than invented — start with the values seen on the next few live bids.

Department is cheap to keep as an optional secondary field and has genuine business-development value (which groups at which refineries actually send work, and which you win), but it should not be the primary discriminator.

- [x] Approved
- [ ] Approved with edits
- [ ] Rejected
- [ ] Needs more source material

### E. Populate `_cost-model.md` — highest priority item in this note

Rates flex by contract, by department, by scope, and by competitor. Internal cost does not. The cost model is the only pricing asset that stays true across every regime described above, and it is the thing that turns "adjust rates to stay competitive" from a gut call into a calculation against a known floor. It is currently a completely empty skeleton.

DSP26058's Internal Financials block is the seed of a margin history — if every quote carried one, quoted-vs-billed drift and per-heater margin would become trend data rather than anecdote.

Requires Jesse to supply internal cost figures; nothing here can be derived. Lane 4.

**Resolved 2026-07-19, same session.** Jesse supplied `Desktop\Facilities\DSP-workup-rates-vs-cost.md`, an extraction of six recent DSP# workbooks. `_cost-model.md` is populated with Tier 1 and Tier 2 at correct units, plus a margin-structure section and three flagged anomalies. Tier 3 confirmed absent from all workups.

**Correction, same session.** On first reading the extraction I concluded that because internal cost was identical across all six workups, cost is genuinely company-wide and therefore belongs in one note while rates do not — treating that as data-driven confirmation of the grain split in A–D. Jesse then clarified that the cost figures are known approximations kept for a general perception of project profitability, pending revision. The inference does not hold: identical values across unrevised workbooks show the numbers are a shared assumption, not that real cost is uniform. Uniformity from a placeholder is indistinguishable from uniformity from a fact, and it was read as the latter.

The grain split in A–D still stands, but on its original grounds — Jesse's account of how contracts are issued, and the Baytown card's inline warning — not on this. Whether cost is genuinely company-wide is now an open question, recorded in `_cost-model.md`.

The cost model is therefore usable for comparing projects on a consistent basis and sanity-checking a bid's shape. It is **not** usable as a floor or to justify how far a rate can be cut, and the file now says so at the top.

- [x] Approved
- [ ] Approved with edits
- [ ] Rejected
- [ ] Needs more source material

### F. Rewrite `Rate Reference.md` framing

Its "base rates overridden per facility" model is wrong on the same axis as (A), and its own notes already record that no company-wide base schedule exists. Either rewrite it to describe the contract-grain model or fold it into the cost model and archive it.

**Decided 2026-07-19 — archived rather than rewritten.** Three compounding reasons: the framing is wrong on the grain axis just corrected in (A); it duplicates the Baseline Rate Table already in `usadebusk-estimating`; and every rate cell was blank while its own note recorded that no company-wide schedule exists. Rewriting would have preserved a file whose job another artifact already does.

Content rescued rather than lost: the stand-by cause table (weather / client delay / equipment downtime) moved to the skill's Contract Terms review section, since billability by cause is a terms question; the 2026-07-06 SharePoint and QuickBooks findings moved to [[rfq-intake-protocol]] as the empirical backing for contract-grain rates.

Not built: a generated cross-quote rate-history rollup, the genuinely missing artifact. Deferred with a trigger (~12 quote notes under a settled heading convention) rather than built for four rows.

- [x] Approved with edits
- [ ] Rejected
- [ ] Needs more source material

## Evidence

The clearest single piece is the Baytown facility card: a rates section scoped to one quote, carrying a manual warning not to apply it to the other quote on the same facility. That warning only needs to exist because the storage grain is wrong — at contract grain, the two quotes simply reference different contracts and no caution is needed.

The 2026-07-06 QB ticket-breakdown pull recorded in `Rate Reference.md` independently supports this: quoted and billed rates diverge within a single job (Valero PA billed TriMax pigging at $550/hr against $500/hr quoted; ExxonMobil billed the PM role at the Day Supervisor rate). A model that assumes one stable rate per facility cannot represent that.

## Risks / Open Questions

The `contract-type` vocabulary is unvalidated — it should be derived from actual bid instructions, not invented, or it will be rewritten within three bids.

(C) is speculative until a live multi-year agreement is confirmed. Building a note type for a contract form that isn't currently active is the kind of premature structure this vault has rejected before.

Retrofitting `contract-type` and `rate-basis` onto the three existing quote notes may require reading the original bid documents, which live in per-facility OneDrive folders and may not still state the terms clearly.

The cost model is internal-cost and margin data — the one genuinely restricted category per the internal-vs-customer data boundary. It stays in the vault, but never flows into a client-facing document.

None of these blocks the existing-contract **estimate fast path**, which remains unwritten and is logged as an open question in [[rfq-intake-protocol]]. That fast path was deferred in this session on the grounds that it depended on facility-card rates; under the corrected model it depends on the quote's own `rate-basis` instead, which is a smaller dependency. Revisit after (D).

## Decision

Per-proposal checkboxes above. This note is open until each of A–F is dispositioned.

## Apply Log

| Date | Action | By |
|---|---|---|
| 2026-07-19 | Note filed from session; no canonical content modified | Claude (Opus 4.8) |
| 2026-07-19 | Proposal E approved and applied — `_cost-model.md` populated from Jesse's six-workup analysis | Claude (Opus 4.8) |
| 2026-07-19 | E corrected and downgraded after Jesse clarified the cost figures are approximations | Claude (Opus 4.8) |
| 2026-07-19 | A, B, D approved by Jesse and applied; C rejected (no live multi-year agreement on his accounts) | Claude (Opus 4.8) |
| 2026-07-19 | A applied: "Rates — do not add" block in `_facility-template.md`; intake protocol step 3 corrected | Claude (Opus 4.8) |
| 2026-07-19 | D applied: contract-field spec added to [[quote-lifecycle]] | Claude (Opus 4.8) |
| 2026-07-19 | F decided and applied: `Rate Reference.md` archived, content rescued to the skill and intake protocol | Claude (Opus 4.8) |
