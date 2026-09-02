---
type: concept
status: active
source_authority: primary
confidence: high
created: 2026-08-15
last_reviewed: 2026-08-15
related:
  - "[[knowledge-system-governance]]"
  - "[[rfq-intake-protocol]]"
tags: [workflow, estimating, knowledge-system, flags]
---

# Business-Normal Facts

## Scope

Some artifacts of normal USADebusk business look like defects to a reader who doesn't know the business. A quotation naming a Project Manager who isn't running the job, an execution date that doesn't match the RFQ, a PO whose line item names a different service, a job with no USA# eight days before mobilization — each reads as a discrepancy, an open item, or a broken rule, and each is simply how the work operates.

This note does two things: it records the convention for where a struck-down flag gets written down, and it carries the register of the facts themselves. It does not govern how to *evaluate* a candidate flag in general — that judgment lives in the per-subclass tests below, because no single universal rule was found to cover them.

## The convention — where a struck-down flag goes

When a flag is raised and ruled not-a-finding, the reasoning gets written where the next reader will land, at one of three tiers. Which tier depends on how far the fact generalizes, not on how important it felt.

1. **Point-of-use vault note**, one sentence, when the reasoning is specific to one job or one piece of equipment. Example: `02-facilities/ExxonMobil/Baytown-TX/DSP26071.md:44` names Travis Trenholm as the standing template default and closes with "Not a discrepancy." The reader who would re-raise the flag is the reader who opened that file.
2. **Skill guardrail rule**, when the *shape* will recur across any future job. Promoted once the first instance shows it isn't job-specific. Example: `usadebusk-estimating` SKILL.md carries the execution-date-inside-the-customer's-window rule, so it stops regenerating on every bid rather than being re-litigated per quote.
3. **Assistant memory**, when it is a meta-rule about how to evaluate a fact rather than a fact about a job. "Owned by someone else's queue isn't an open item" is not a fact about the F-501 job; it is a rule for reading every job. No single skill file is the right owner.

This was not designed. Four independent instances converged on the same shape before anyone named it, which is the reason it is written down here rather than proposed — the convention describes observed practice.

Tier 3 is the one with no vault footprint, which is why the register below exists: assistant memory is coupled to one harness and one machine, and a tool switch or memory reset loses it while tiers 1 and 2 persist.

## The register

| Fact | Why it reads as a defect | Why it isn't |
|---|---|---|
| Project Manager on every quotation reads "Travis Trenholm" | Looks like a stale or superseded assignment | A PM cannot be assigned at bid time; the dispatching ops manager is the permanent placeholder. Never an assignment, never superseded, never a thing to confirm |
| Execution-plan date differs from the RFQ's stated date | Looks like a schedule discrepancy | Customers name a *window* and settle the exact date with the winner. DSP26095 ran 8/31–9/1 against an RFQ headed "September 7 2026". A wrong *year* is worth one mention; a date inside the customer's own window is not |
| No USA# assigned close to mobilization | Looks like missing paperwork blocking the job | The USA# is the ops manager's to create when he gets to it. Same shape: crew assignment and badging |
| A heater card or job report citing third-party smart-pig findings we cannot produce the report for | Looks like an un-ingested document, a follow-up owed, or a citation we should go substantiate | **Third-party inspection vendors do not share their data or reports with us, and we should not expect them to** (Jesse, 2026-09-02). This holds for Quest Integrity and Steadyflux alike — it is not one vendor being difficult. Sharing reports carries real commercial risk in both directions: **Quest is already a competitor with its own decoking division**, and either company could branch into the other's market. What reaches us is verbal communication on the job, and that is the ceiling. So a note reading "Quest has the data showing the exact passes and locations" is a complete, closed statement of where the evidence lives — not a retrieval task. Record the verbal account with its source and date, cite the vendor as the holder, and never open it as an item awaiting the report |
| PO already approved by the VP, however odd the line reads | Looks like a commercial question to raise | It is closed. Someone above Jesse already ruled |
| One PO covering hydroblast and pigging scope across divisions | Looks like evidence the decoke-scope rule was broken | A shared agreement can cover both scopes. USA26041's PO 4411473422 at $256,250.56 is the worked instance |
| "Sea-Can Double Pumper" vs the skill's "single 48' trailer" | Looks like two conflicting equipment descriptions | Same unit — a 48' trailer with a sea-can container retrofitted onto the bed, both pump assemblies housed inside |
| Zero or short per-diem line on the mob and demob tabs of a ticket breakdown | Looks like unbilled per diem — the receipts record a headcount for those days and the workbook bills none | **Mob and demob bill as lump sum and the per diem for those days is carried inside the lump sum.** As long as the lump-sum amount is on the invoice, that per diem is billed. The receipt's "Per Diem: 6" records headcount, not a separate claim. (Jesse, 2026-08-15 — after I reported a phantom gap on USA26041 twice, at $1,800 then $1,350) |
| A lost bid at a site whose rep has a preferred contractor | Looks like the price was wrong — and a repeat loss at one site looks like a pricing pattern worth correcting | **Some facility reps have a preferred contractor and go out to bid only because procurement requires competing quotes.** The bid was a compliance exercise and a sharper price would not have won it either. So a loss there is not evidence about the number, and two losses are not a trend. Recorded instance: **Westlake South prefers DDT** (Jesse, 2026-08-16), which is 0 for 2 across 2024 and DSP26095. Do not infer a pricing problem, and do not re-price the next one against the loss |
| A bid built for an opportunity nobody expects to win | Looks like wasted estimating effort, and invites a no-bid recommendation | **USADebusk bids every opportunity.** Jesse, 2026-08-16: *"I don't believe it's worth bidding, but we will anyway. We don't turn down opportunities to bid."* Expected win probability is not an input to whether a bid gets built or how much effort it gets. Never raise no-bid as an option, never propose reallocating estimating hours on win-odds. The only thing that stops a submission is a hard disqualifier — wrong form, missed deadline — which is mechanics, not judgment |
| No answer available on who won a lost bid, or why | Looks like an unresolved open item on the quote note | **Award results, competitor pricing, and the customer's stated reason are not information Jesse can get** (2026-08-16: *"I won't be able to give answers like 'DDT actually took this award'."*). This is a permanent condition, not a gap awaiting follow-up. `lost-reason` is a best-available label, never a measurement — record it, do not open it as a question, and do not build analysis that depends on it being accurate |
| A Suncor Commerce City, CO bid sitting in the estate with no job behind it | Looks like an unfiled award, a missing job folder, or a data-integrity gap worth chasing | **USADebusk has never worked that facility and every bid there was lost — Clean Harbors usually wins it** (Jesse, 2026-08-18). The DSP#25099 TA 2026 pigging RFQ and its 25099.1 revision are the recorded instance. Treat Suncor Commerce City artifacts as closed history: do not open them as questions, do not build a facility folder or quote notes for them, and do not use them as evidence about pricing. Distinct from the Westlake/DDT row above in that this is a whole *site* we have no presence at, not a single rep's preference |
| Convection tube ID larger than radiant tube ID | `usadebusk-core` flags this as stop-and-confirm, true on 99%+ of heaters | Genuine and correct on a **same-OD, mixed-schedule** heater: F-501 runs one 5.563" OD throughout with 0.400" convection wall against 0.464" radiant, so the heavier radiant wall gives the smaller bore. The core heuristic is written around pipe *size*; it does not hold when a heater changes schedule instead of diameter. Pig sizing is unaffected — it keys off the smallest ID wherever it sits |

## The tests

The category resists one universal rule, but two subclasses have usable tests.

**Someone else's queue.** Ask who owns the item before writing it anywhere as open. Owned by Jesse and actionable now is an open item. Owned by someone else, or already ruled on by someone above him, is one factual line naming the owner — in the job sheet or quote note, never in a flags/risks/open-items list and never in a closing summary. (Jesse, 2026-07-29: "No need to continue flagging. I'll bring it here the moment it's created.")

**Template default, not an assignment.** A field that carries the same value on every document regardless of job is a placeholder, not data about this job. Confirming it, marking it superseded, or reconciling it against reality all generate false work.

If an instance fits neither test, it is not automatically a real finding — but it does need Jesse, not a rule.

## Why this is a category and not a coincidence

Six instances arrived in a single session on 2026-07-29 and were all struck down. The open question at the time was whether that was one unusual day. It wasn't: a seventh arrived the next day (the cross-division shared PO) and cost the same round trip, with six prior fixes already in place. Each fix closes one instance; none of them closes the category. That is the argument for a register rather than another point-of-use sentence.

## Boundary

Recording a fact here does not make it permanent truth. These are business-normal *as of now* — if the PM field ever becomes assignable at bid time, the first row stops being business-normal and becomes a real check. Re-read before treating a row as settled.

## Provenance

Resolved from `06-reviews/2026-08-02-idea-research-business-normal-register.md` (approved 2026-08-15), which researched `[[idea-business-normal-register]]` and recommended against building a new register artifact in favor of naming the existing convention and giving tier 3 a vault copy. Underlying rulings are Jesse's, 2026-07-29 and 2026-07-30, recorded in `change-log.md`.
