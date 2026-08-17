---
type: review
status: open
review_type: contradiction
source_authority: verified
confidence: high
created: 2026-08-17
related:
  - "[[F-501]]"
  - "[[USA26041-job-report]]"
  - "[[idea-smart-pig-report-as-cleaning-verification]]"
tags: [review, smart-pig, field-execution, manual, rig-out]
---

# Review — the §14.6 rig-out gate is honored on some inspection-supported jobs and not others

## The rule

`manual/14` §14.6 carries this as a WARNING, not as guidance:

> On inspection-supported scopes, the customer's written acceptance of the inspection data is
> required before dewatering, hose disconnection, or any rig-out activity begins.

`manual/10` §10.5 repeats it and states the reason, which is the part that makes this worth raising:
"Rig-out ahead of that acceptance forecloses a re-run, and the gate exists to protect against that."

## The two jobs that record the sequence

**Valero Port Arthur H-102B — gate honored.** The heater card records that Quest Integrity performed
smart pig inspection on all 8 passes "and provided final clearance before rig-out."

**ExxonMobil Baytown F-501 / USA26041 — gate not honored.** Steady Flux ran the tool 2026-08-13.
Report `26-0663-002 Rev. A` issued 2026-08-15, roughly 48 hours after the run, against a spec sheet
promising a preliminary areas-of-concern report in 2 hours and a final in 24. The card states
plainly: "Rig-out proceeded on the preliminary." Rig-out ran 08-13 night into 08-14, so the circuit
was broken down before the final report existed.

## What the sample actually is

Six USADebusk jobs are known to have carried a customer-elected smart pig: Syncrude 7-1-F-1 on
CND24002 and CND25004, Flint Hills 01-BA-105 and 02-BA-201, Valero H-102B, and ExxonMobil F-501.
Only two of the six — Valero and F-501 — record the rig-out sequence relative to inspection
acceptance at all. The other four record the smart-pig election and hours but say nothing either way
about acceptance before rig-out, so they are silent rather than supporting evidence.

So this is n=2, opposite outcomes. That is a small sample and it is stated deliberately: what makes
it worth a decision row is not the frequency, it is that one of the two is a documented deviation
from a written WARNING on a job that closed 2026-08-14.

## Why this is not a drafting question

The `idea-smart-pig-report-as-cleaning-verification` seed asks whether the §14.6 acceptance gate is a
better commercial hook than the vendor report's text. It is a good hook precisely because it is
customer-signed and USADebusk never has to characterize a C-scan. But writing it into a proposal
advertises a commitment the field record shows is not consistently kept, and a customer who later
learns rig-out went ahead on a preliminary has been handed a real grievance. The commercial question
is downstream of the practice question, and the practice question is this one.

The F-501 case also cost something concrete. B_8_C — convection Pass B pipe 8, 0.224" remaining,
internal, bottom-of-pipe, full-length in a horizontal tube — is the one segment in the heater that
could plausibly read as residual deposit rather than corrosion, and it is an open question with
Steady Flux as of 2026-08-16. That is exactly the question a re-run could have settled, and rig-out
foreclosed it. §10.5's stated rationale is not hypothetical here; it happened.

## Decision

Not proposed here. `manual/10` and `manual/14` are SOP content and field-execution practice, which is
Lane 4 — the call is Jesse's. The fork, stated neutrally:

- **Tighten practice** — rig-out waits for the customer's written acceptance of the *final* report, and
  the standby exposure between end-of-run and acceptance gets priced rather than absorbed.
- **Amend the manual** — a preliminary areas-of-concern report is sufficient to release rig-out, and
  §14.6 / §10.5 are rewritten to say so, since a WARNING that is routinely not followed is worse than
  no WARNING.

What cannot stand is the present state, where §14.6 says one thing and the most recent
inspection-supported job did another with no exception recorded.

- [ ] **Decision:**

## Provenance

Surfaced 2026-08-17 while verifying cited specifics from an ADHD-skill back-test. Every quotation
above was read back against its source file: `04-knowledge/manual/14-ancillary-smart-pig-support.md`
§14.6, `04-knowledge/manual/10-verification-and-completion.md` §10.5,
`02-facilities/Valero/Port-Arthur-TX/H-102B.md`, and
`02-facilities/ExxonMobil/Baytown-TX/F-501.md`. The four-job silence was checked by grep across the
Syncrude, Flint Hills and CHS cards.
