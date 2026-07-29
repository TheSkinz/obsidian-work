---
type: idea-seed
status: unexplored
created: 2026-07-29
tags: [idea, vault-system, future, estimating]
---

# A register of business-normal facts — the things that make sound documents look defective

Idea seed captured 2026-07-29 for a future exploration session. The read below is tentative —
confirm intent with Jesse before designing.

**Tentative read:** The vault records heater facts, contract terms, rates and decisions, but it
does not record **what is routinely true about how USADebusk bids and operates** — and that gap
is what makes correct documents read as defective to anyone working from the files alone. Six
instances surfaced in a single session on 2026-07-29: a PO whose line description names a
different service line (VP-approved, one agreement covers both scopes); a USA# that has not been
issued (the ops manager creates it when he has time); crew and badging unassigned close to
mobilization (same); a Project Manager field reading "Travis Trenholm" (standing template default
— no PM can be assigned at bid time); an execution plan dated inside the customer's own stated
window rather than on the RFQ's headline date; and a quotation header date that Jesse simply did
not care about. Each was raised as a finding, each was struck down, and each cost a round trip.
The individual rulings are now written into `usadebusk-estimating` and the heater/job files, which
fixes those six — but the *class* has no home, so the seventh will cost the same round trip.

**To explore:** Is a standing register the right shape, or does this belong distributed at each
point of use the way the six fixes were applied? Distribution has a real advantage — a rule
written where the work happens is read at the moment it is needed, while a register has to be
found. But distribution is what let the DSP26071 note describe the Trenholm default as
*superseded*, which actively generated a flag rather than preventing one, so the two approaches
are not equivalent under drift. What is the actual population — is six a genuine pattern or the
tail of a single unusual day? Worth counting struck-down flags across recent session history
before designing anything. Is there an existing home that already fits (`01-context/`, the
estimating skill's guardrails section, `04-knowledge/concepts/`) rather than a new artifact? And
is the failing distinguishable from a real finding by any rule at all, or is "unexplained by the
documents in front of me" simply not the same predicate as "unresolved," with no mechanical test
between them?

**Gate:** None — researchable now.
