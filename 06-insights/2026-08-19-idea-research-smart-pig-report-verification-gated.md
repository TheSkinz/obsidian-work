---
type: review
status: open
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

## Recommended Action

**Keep parked; make one request.** Ask Quest Integrity or Valero for the H-102B inspection report
from the Port Arthur job. It is the single highest-value document for this seed — it is the
unflattering case, we already know what it found, and it would let the "does this survive a bad
report" question be answered against real vendor text instead of a guess. A Syncrude or Flint Hills
report would open the gate too but tests a weaker case.

No build, no proposal language, and no close-out language until a second report is in hand.

## Decision

- [ ] Approved — request the H-102B report from Quest Integrity / Valero
- [ ] Approved with edits — request a different report instead
- [ ] Rejected — leave gated with no outreach
- [ ] Ungate anyway — the H-102B secondhand narrative is enough to research on

## Apply Log

| Date | Action | By | Notes |
|---|---|---|---|
|  |  |  |  |
