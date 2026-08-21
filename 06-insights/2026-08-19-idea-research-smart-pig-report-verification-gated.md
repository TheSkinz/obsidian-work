---
type: review
status: resolved
review_type: idea-research
source_authority: inferred
confidence: medium
created: 2026-08-19
review_after: 2026-11-19
related:
  - "[[idea-smart-pig-report-as-cleaning-verification]]"
  - "[[F-501]]"
  - "[[H-102B]]"
  - "[[vault-idea-loop-spec]]"
tags: [review, idea-research, gated, smart-pig, proposals]
---

# Idea Research — Smart-Pig Report as Cleaning Verification (gated, not researched)

## Trigger

Scheduled nightly run of the Vault Idea Research Loop, 2026-08-19. Oldest unexplored idea-seed by
`created:` date is `idea-smart-pig-report-as-cleaning-verification` (2026-08-15). Three seeds carry
that date; the 2026-08-17 run fixed their order by git first-commit time (frozen-baselines 18:45:27,
researched-status 20:03:51, this seed 22:34:39) and the first two have since been researched, so this
one came up next.

Per the loop spec's step-3 gate check, the seed's stated gate was settled from files before any
research. It is shut, so this run closed the gate and moved to the next seed rather than spending a
research cycle.

## The gate

The seed states it plainly: **"Obtain a second vendor report — that is the gate, not a future job."**
The purpose is specific and worth preserving — the seed wants to test the case where the inspection
report is *less* flattering, because that case decides whether a vendor report is a durable
commercial asset or cherry-picking. A second flattering report would not settle it; a second report
of any kind would at least let the question be asked against real text.

## Evidence the gate is shut

**1. Exactly one vendor inspection report is held as a file, and it is the one the seed already
read.** `02-facilities/ExxonMobil/Baytown-TX/F-501.md:193` lists `26-0663-002 Rev. A` — *Intelligent
Pig Report, Hydrofining Unit F-501*, Steady Flux Technologies — in its Sources block, with the
appendix inventory (B_8_C detail, thin-pup list, WiLBR tool specs) that only a held copy supports.
No other heater card, job report, or inbox note names a second vendor report document.

**2. All prior smart-pig instances still reach the vault secondhand.** Checked every card the seed's
2026-08-17 correction names, plus one it missed:

| Job / heater | What the card records | Vendor report on file? |
|---|---|---|
| Syncrude 7-1-F-1, CND24002 + CND25004 | "Quest smart pig all 8 coils" (`7-1-F-1.md:92`, `:117`) | No document number, no Sources entry |
| Flint Hills 01-BA-105 | "Quest — smart pig assist, all 4 coils" (`01-BA-105.md:90`) | No |
| Flint Hills 02-BA-201 | "Quest — smart pig assist, all 4 coils, 5 hrs" (`02-BA-201.md:91`) | No |
| Valero Port Arthur H-102B | "Quest Integrity, all 8 passes (1B-8B)" (`H-102B.md:74`) | No |
| Valero Port Arthur **H-102A** | "Quest Integrity, all 8 passes (1A-8A)" (`H-102A.md:74`) | No |

H-102A is a sixth instance the seed's correction did not list. It does not change the gate — it is
secondhand like the rest — but it widens the set of reports that could be asked for.

**3. Nothing has landed since the seed was corrected on 2026-08-17.** Commits from 2026-08-17
forward cover the DSP26085 duplicate-workup work, the PS3 change-order surfaces, INDEX link
disambiguation and the loop runs; none ingest an inspection report. The only Steady Flux items in
`00-inbox/` — the owed bore-profile request (2026-08-16) and the Rev. A audit findings (2026-08-16)
— are both against the *same* Rev. A document, not a second one.

## Interpretation

**Gated — not researched.** The gate is verifiably unmet from files, so per the loop spec no web
research was performed on this seed and the run moved on to the next-oldest.

One finding is worth recording because it makes the gate cheaper to open than the seed assumes. The
seed frames the unflattering-report case as hypothetical. It is not — **Valero Port Arthur H-102B is
that case**, and the vault already holds the narrative: smart-pig inspection found a 0.25" thick
circumferential coke ring at the inlet end of the second 5" tube on Pass 6B, which required dedicated
pigging to clear and was "confirmed clear by Quest Integrity before rig-out" (`H-102B.md:116`,
`:118`). That is precisely the shape the seed wants to stress-test — a report that found something
we missed on the first pass, and then documented the clean after we fixed it. It is secondhand, so
it does not satisfy the gate as stated, but it identifies **which** report to request first, and it
suggests the answer may be favorable rather than fatal: the close-out claim survives an unflattering
finding if the finding is followed by vendor-confirmed clearance.

## Correction — 2026-08-19, Jesse: the back catalog is not obtainable

**Quest does not share project reports the way Steady Flux does.** That kills the outreach this note
originally recommended, and it changes the gate's character rather than just its target.

Every prior smart-pig instance in the vault is Quest or Quest Integrity — Syncrude 7-1-F-1 (both
jobs), Flint Hills 01-BA-105 and 02-BA-201, Valero Port Arthur H-102A and H-102B. Steady Flux, on
F-501, is the **only** vendor that has ever put its report in USADebusk's hands. So the back catalog
is not a document-access problem that a request solves; it is closed.

The consequence is that the seed's own 2026-08-17 correction — "the blocker is document access, not
elapsed time... asking Quest or the customer for one of the four earlier reports may be faster than
waiting on a quote" — is now wrong on both halves. Elapsed time *is* the blocker, and the gate
reverts to being exactly what that correction said it was not: **a future job**, and specifically one
where the vendor is Steady Flux, or another vendor that shares, or where the customer forwards the
report to us.

One route survives and is Jesse's call, not a research finding: the report belongs to the customer,
so asking Valero rather than Quest is a different channel with a different answer. It is a
relationship ask on a closed job, which may not be worth spending.

## Recommended Action

**Keep parked. No outreach to Quest.** The gate stands and now waits on a future smart-pig job whose
report actually reaches us — Steady Flux being the demonstrated case. Nothing to do until one lands.

Optionally, and only if the relationship makes it cheap: ask Valero directly for the H-102B report.
It is still the unflattering case worth testing against, and the customer holds a copy even though
the vendor will not release one. Kill this line if it costs any goodwill.

No build, no proposal language, and no close-out language until a second report is in hand.

**Worth keeping regardless of this seed:** *Quest does not release project reports; Steady Flux does.*
That is a vendor-selection fact with commercial weight beyond this idea — if a vendor's report is an
asset we want, that is an argument for who gets recommended when the customer asks. It has no
canonical home today (the business-normal register was researched 2026-08-02 and never built), so it
lives here until Jesse routes it.

## Decision

- [x] Approved — keep parked, no outreach at all — **ruled 2026-08-21.** Overtaken: the 2026-08-19 finding that Quest does not release project reports already settles this. The gate waits on a future smart-pig job with a sharing vendor, and that trigger is recorded on the seed itself.
- [ ] Approved — keep parked, but ask Valero for the H-102B report
- [ ] Route the Quest-vs-Steady-Flux report-access fact to a durable home (which?)
- [ ] Ungate anyway — the H-102B secondhand narrative is enough to research on

## Apply Log

| Date | Action | By | Notes |
|---|---|---|---|
| 2026-08-21 | Closed as overtaken. Jesse ruled "keep parked, no outreach." | Claude | The 2026-08-19 finding that Quest does not release project reports had already answered this; the note was open for a decision that events had made. No queue row. |
|  |  |  |  |
