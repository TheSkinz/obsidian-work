---
type: idea-seed
status: unexplored
created: 2026-08-18
tags: [idea, estimating, invoicing, skill-guardrail]
---

# Check an invoice against the governing document, not the original quote

Idea seed captured 2026-08-18 for a future exploration session. The read below is tentative — confirm intent with Jesse before designing.

**Tentative read:** Two same-day findings on ExxonMobil Baytown jobs share a shape: a number that looked wrong against the original quote was actually correct against a later governing document — [[DSP26071]]'s billing rate was changed by the account manager before mobilization (quoted $35/hr, governing $150/hr), and the PS3 job's (USA26007, ExxonMobil Baytown Pipestill 3 decoke, filed on the Baytown facility note) $199,756.00 invoice looked like a $37,179.58 overage until a signed change order surfaced putting the authorized ceiling at $206,689.91. Both times the "discrepancy" was a stale-baseline problem, not a pricing or billing defect. That might be a recurring shape worth a guardrail in `usadebusk-ops` or `usadebusk-estimating`: before flagging an invoice-vs-quote gap, check whether a change order or rate change supersedes the original number.

**To explore:** Is two instances enough to call this a pattern rather than coincidence (see the business-normal-facts convention, which promotes to a skill guardrail "once the first instance shows it isn't job-specific")? What would the guardrail actually check for, given change orders and rate changes aren't reliably filed anywhere structured — DSP26071's rate change was undocumented until Jesse mentioned it, and the PS3 change order was found on Google Drive by chance. A guardrail that can't reliably find the governing document may just be a reminder to ask Jesse rather than an automatable check.

**Gate:** A third instance, or Jesse's read on whether this is worth a guardrail versus staying a case-by-case "ask before flagging" habit.
