---
type: concept
tags: [workflow, quotes, jobs]
---

# Quote Lifecycle

This covers what happens when a quote is decided — won or lost — and how to create a job record when one is awarded. The front half — RFQ arrival through proposal submission — is [[rfq-intake-protocol]].

---

## Numbering Convention

- **Quotes:** DSP##### format — DSP + YYNNN (e.g., DSP26058)
- **Jobs:** USA##### format — USA + YYNNN (e.g., USA26001)
- **Facility ID** (for Dataview joins): Client-City-State string (e.g., Marathon-Garyville-LA) — must match exactly

---

## Quote Frontmatter — Contract Fields

Adopted 2026-07-19 (proposal D, [[2026-07-19-rate-model-grain-review]]). Rates are a property of a contract, not of a facility — one site can carry several concurrent contracts at different rates. These three fields record which regime a quote was priced under, so two quotes at the same site showing different rates is answerable rather than alarming.

| Field | Purpose | Values |
|---|---|---|
| `contract-type` | The contract/terms form named in the bid instructions — **what governs the rates and how long they live** | Vocabulary is **open** — take the value from the actual bid instructions rather than inventing one. Seen so far: `short-form scope contract`, `purchase-order only`, `spot PO`. |
| `rate-basis` | Where this quote's rates came from | `quote-specific` (the common case — rates negotiated for this scope, contract ends with the project), or a wikilink to a contract note where a multi-project agreement governs |
| `billing-basis` | Commercial structure — **how the work converts to money** | `T&M + LS mob/demob` (95%+ of jobs), `lump sum`, or as stated |

Leave a field blank rather than guessing. On older quotes the bid instructions may no longer be at hand, and a blank is honest where an inferred value is not.

### The default posture is uniform rates

Before the distinctions below: **USADeBusk prefers to run the same rates at every facility** (Jesse, 2026-07-26). The house standard in `usadebusk-estimating` and `_cost-model.md` is the intended rate, and most bids should land on it. A quote that diverges has a reason — most often that the RFQ was contested and rates were cut to win it — and that reason is worth a line on the quote note, because it cannot be reconstructed from the rate table afterwards. Read divergence as a flag, not as evidence that each site has its own regime.

### Contract type is about term; billing basis is about structure

These two are easy to collapse and shouldn't be. Jesse, 2026-07-26, on what actually drives rate divergence:

**Long-term maintenance contract** — a multi-year agreement (≈3 yr is typical) establishes base rates for its whole duration. Within the term, *scope does not matter*: any work bid under it is served at contract rates. Rates are **inherited**, and they outlive any single job. This is the case that would need the contract note deferred as proposal C.

**Short-term scope-specific contract** — the majority of wins. Rates are established during the bidding of one identified scope ("4 specific heaters for the 2026 turnaround", "1 heater for the January 2027 outage"), the resources and task durations are billed against them during execution, and **the contract ends when the scope completes**. Rates are **set per bid and then expire**. This is why a superseded quote's rate sheet is not a rate history entry to reuse — that contract is over.

`lump sum` belongs in `billing-basis`, not here. Lump sum describes how the customer is billed — the quoted amount, altered only by a signed change order — and it is orthogonal to term. Cost is still tracked internally through the ticket breakdown sheet on a lump-sum job, so the internal record exists even where the invoice is one line.

**Customers sometimes state the taxonomy for you.** ExxonMobil purchase orders carry a literal `Lump Sum, T&M, or Spot:` field — [[DSP25123]]'s PO reads `Spot`. Take that value verbatim; it is the bid instruction the field was designed to capture.

**Quoted basis and billed basis can diverge, so record what happened, not what was proposed.** [[DSP25123]] was quoted `T & M`, issued on a spot PO, and then invoiced as a single fixed-price line at exactly the quoted total — no hours ever re-measured. That divergence is the same class of finding as the QuickBooks quoted-vs-billed drift in [[rfq-intake-protocol]], and it is invisible unless the field records the outcome.

The **issuing department** (turnaround, maintenance, procurement, capital projects) is optional and not a pricing field. It has business-development value over time — which groups at which refineries send work, and which convert — but it only correlates with the terms, it does not determine them. Contract type is the discriminator.

There is no contract note type yet. It is deliberately unbuilt: as of 2026-07-19 none of Jesse's active accounts carry a long-term agreement, so `rate-basis` is `quote-specific` everywhere. Build it when the first multi-year agreement actually lands.

**Backfill status (2026-07-26):** the three fields were adopted 2026-07-19 but applied to almost nothing — of 7 quote notes, only DSP26080 carried any of them, and it lacked `contract-type`. Backfilled this session where a source document actually states the answer: [[DSP25084]], [[DSP25123]], [[DSP26039]]. **Still empty: DSP24005 (CHS), DSP26030 (P66), DSP26058 (Marathon)** — their bid instructions weren't reviewed this session, and per the rule above a blank beats a guess. Worth filling next time any of those files is open, because these fields are what a future rate-history rollup would segment on; without them it can only compare rates it cannot explain.

---

## On Decision

Open the DSP##### quote note and update these frontmatter fields:

| Field | If Won | If Lost |
|---|---|---|
| `status` | `awarded` | `lost` |
| `awarded-as` | USA##### job number | leave blank |
| `lost-reason` | leave blank | short phrase (e.g., `price`, `competitor`, `no award`) |
| `date-decided` | YYYY-MM-DD | YYYY-MM-DD |

The `_pipeline.md` Dataview queries pull on `status` automatically — no manual dashboard update needed. Once the frontmatter is saved, the quote moves from Open Quotes to the correct section.

---

## The Three Field-Document Types

Three documents carry a job, and the distinction is what keeps each one trustworthy. Confirmed on USA26038, 2026-07-11.

The **job sheet** is static, created at bid-win from the quoted work-up. It is crew-facing and printable, and it holds the quoted resource plan plus how to key service receipts against it. It never carries actuals, status, or timeline. Schema authority: [[_canonical-job-sheet]]; template: `templates/_job-sheet-template.md`.

The **heater card** is persistent. It holds the heater's fixed physical facts plus actuals accumulated across every job on that unit. Schema authority: [[_canonical-heater-card]].

The **job report** is post-job. It carries the timeline and actuals for one job — what really happened, who was really there, real hours. This is where quoted-versus-actual gaps live.

The quoted resource plan and the mobilized crew routinely differ (USA26038 quoted 12 people, sent 10). That gap is a job report finding. Correcting a job sheet to match what happened destroys the only record of what was sold.

---

## If Awarded: Create the Job Sheet, Record on the Heater Card(s)

There is no standalone job note — the `03-jobs/` folder is retired and jobs dissolve into the heater card(s) they touch. On award, set `awarded-as: USA#####` on the source quote so the link carries forward; the operational record then accrues on each heater card as the job runs.

Create the job sheet at bid-win from `templates/_job-sheet-template.md`, saved as `02-facilities/<Client>/<City-ST>/<USA#####>-job-sheet.md` alongside that site's heater cards. Build it from the quoted work-up, not from any later revision — the billing math and section rules are canonical in [[_canonical-job-sheet]].

The heater card is the operational record. Job-level commercial data (revenue, cost, margin, crew) lives in the file estate, not the vault.

---

## After Award: active-jobs.md

Move the quote row from Pending/Bidding to Awarded/Pre-Execution in `01-context/active-jobs.md`. Update it again when the job mobilizes (move to Active) and when it completes (move to Recently Completed).

---

## Job Closeout

When the job completes, record the actuals on each heater card the job touched:

- Add the `## Job History` row (Job #, quote, dates)
- Fill the `## Task Durations` actuals row (elapsed hours, Rigs, Stand-By, Total — actuals only)
- Add the `### USA##### — Month Year` narrative under `## Field Notes`

Commercial close (revenue, cost, margin against the final ticket breakdown) is handled in the file estate, not the vault.
