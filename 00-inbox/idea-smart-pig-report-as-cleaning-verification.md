---
type: idea-seed
status: gated
created: 2026-08-15
revisit-trigger: "A second smart-pig vendor inspection report reaches USADebusk as a held file -> unpark and research whether the vendor's report becomes proposal language, close-out language, or both. The back catalog cannot supply it: every prior instance is Quest, and Quest does not release project reports (Jesse, 2026-08-19) — Steady Flux is the only vendor that has. So this waits on a future smart-pig job with a sharing vendor, or on Valero forwarding the customer's copy of the H-102B report if that ask is ever cheap — event: check when any vendor inspection report is filed to a job folder"
related:
  - "[[2026-08-19-idea-research-smart-pig-report-verification-gated]]"
tags: [idea, estimating, proposals, smart-pig, future]
---

# Smart-pig report as a cleaning-verification asset

Idea seed captured 2026-08-15 for a future exploration session. The read below is tentative —
confirm intent with Jesse before designing.

**Tentative read:** On scopes where the customer elects smart pigging, the inspection vendor's own
report is third-party evidence that USADebusk's cleaning met scope, and USADebusk is not currently
using it that way. Steady Flux's `26-0663-002 Rev. A` on USA26041 states the convection, radiant and
treat gas sections are "generally clean with only minor fouling remaining," reports no denting,
swelling or bulging in any straight segment, and ovality never above 2.7% — and the WiLBR spec sheet
lists "identified areas of coke buildup that may not have been cleaned properly" as a tool
capability, which it then found none of. That is a stronger close-out than effluent clarity and a
before/after flow test, and it is on the vendor's letterhead rather than ours. The physics behind it
is real: UT wall measurement needs acoustic coupling to steel, so a clean low-noise C-scan across a
full coil is itself evidence the pigging reached bare metal.

**To explore:** Is this proposal language, close-out language, or both? Whether it is safe to lean on
— the manual's role boundary is explicit that nothing in the USADebusk scope constitutes inspection
and USADebusk makes no representation about the data, so the claim has to be "the vendor's data
shows a clean coil," never "we certify the coil." Whether it survives a job where the report is less
flattering, which is the case that decides if this is a durable asset or cherry-picking. Whether the
customer's own acceptance of the inspection data (the `manual/14` rig-out gate) is the better hook
than the report text. And whether it changes anything commercially — does it help win the next bid,
shorten a dispute, or is it just nice to have.

**Gate:** Needs at least one more smart-pig-elected job's *report* to test the "what if the report is
unflattering" case before this becomes proposal language. **Obtain a second vendor report** — that is
the gate, not a future job.

**Corrected 2026-08-17.** This seed originally read that DSP26085 (F-201, Jan 2027) "would be the
second instance." That is wrong, and it set the gate five months out for no reason. Smart pigging has
been elected on at least five prior USADebusk jobs: Syncrude 7-1-F-1 on both CAD24002 and CAD25004
(Quest, all 8 coils each), Flint Hills 01-BA-105 and 02-BA-201 (Quest, all 4 coils each), and Valero
Port Arthur H-102B (Quest Integrity, all 8 passes). The Syncrude card even carries the claim shape
this seed is reaching for — the heaviest-fouled radiant tubes at the outlet, where "smart pig found
minimal fouling there, 'typical of previous decokes.'"

What is actually true is narrower: **F-501 is the first instance where USADebusk holds the vendor's
own report as a file** (`26-0663-002 Rev. A`, USA26041 Job Files). The prior instances reach the vault
secondhand, quoted inside USADebusk job reports. So the blocker is document access, not elapsed time,
and asking Quest or the customer for one of the four earlier reports may be faster than waiting on a
quote that is still `status: pending`.

Found during the ADHD-skill back-test, 2026-08-17; every instance above verified against the heater
cards.

**The unflattering case has a published base rate, 2026-09-03.** This seed's central question — *"whether
it survives a job where the report is less flattering, which is the case that decides if this is a
durable asset or cherry-picking"* — is partly answered by Quest Integrity's own ADCV white paper (v1.0,
2020-12-07, read in full during the DQ-030 terminology work). Quest states that smart-pigging
inspections have found **"varying amounts of leftover fouling that have followed decoking activities
in a vast majority of heaters since 2001,"** footnoted to **"over 2,400 heater inspections."**

Three consequences, none of which needed the second report this seed is gated on:

- **The unflattering result is the base rate, not a contingency.** The seed treats it as the edge case to
  survive; the leading ILI vendor publishes that it is the normal outcome of a conventional decoke.
- **The gate was set correctly and now has a stated reason.** Leaning on a favourable report as proposal
  language, against a vendor-published base rate that says most decokes leave fouling, is the exact
  shape of cherry-picking the seed was worried about.
- **It also raises the value of a clean result.** A vendor confirming minimal residual fouling means
  more, not less, when that same vendor publishes that most cleans do not achieve it. Whether that is
  usable turns on the first point, not on the strength of any single report.

Note this cuts against the "obtain a second vendor report" framing of the gate. Quest does not release
project reports, but the *result* reaches us anyway — USA26038's own job report states "a Quest smart
pig confirmed only minimal residual coke," and the Syncrude card carries "smart pig found minimal
fouling there, 'typical of previous decokes.'" A stated result may be enough to test the unflattering
case even where a report is unobtainable, which would make the gate cheaper to clear than it reads.
**Not unparked and the gate stands** — this is evidence added to the open question, not a decision.
Related terminology work and the full source read: [[2026-09-03-fouling-terminology-vocabulary]].
