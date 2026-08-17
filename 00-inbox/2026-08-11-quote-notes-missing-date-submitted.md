<!-- vault-loop: no home yet, candidate for [quote-note-backfill] -->
<!-- vault-prestaged: skipped — execution correction, needs doing not deciding. The fix is to confirm the submission date with Jason (DSP26085) and ask whether DSP26080 has drawn any response since 2026-06-26, then backfill date-submitted/valid-through — both fields are still blank as of this run. No alternatives to weigh. -->

---
type: review
status: open
review_type: data-gap
source_authority: session
confidence: medium
created: 2026-08-11
review_after: 2026-09-01
related:
  - "[[quote-lifecycle]]"
tags: [quotes, data-gap, copilot]
---

# Pending quote notes carry no `date-submitted`, and the mailbox can fill it

Noticed 2026-08-11 while scoring a Copilot routing eval against the vault.

Both pending ExxonMobil-family quote notes have an empty `date-submitted`:

- **DSP26085** (ExxonMobil Baytown, 27GF1A F-201) — Copilot found it sent by Jason Harman to Doug
  Thomas on **2026-07-06**, with a customer-facing submission confirmed in the thread. The vault
  field is blank.
- **DSP26080** (HF Sinclair Navajo, H-2421 / H-30 / H-2501) — completed and handed to Jason
  2026-06-26. No customer-facing send is visible, which per [[outlook-email-architecture]] is the
  **normal** case when an account manager submits directly, not evidence of a problem.

The field matters because `50-dashboards/health.md` flags a pending quote past its validity, and
DSP26080 has no `valid-through` either — so it cannot expire, cannot be flagged, and has been quiet
since late June.

**Not a correction to make blind.** Copilot's dates come from ranked email search, which it twice
admitted is not proof of absence, and the submission date that matters commercially is the one the
customer received — which for account-manager-submitted bids is in someone else's mailbox. Confirm
with Jason rather than writing Copilot's figure into the quote note.

Worth one question at the same time: whether DSP26080 has had any response since 2026-06-26. Roughly
seven weeks quiet on a live bid is the actual signal here; the missing field is just what stopped
anything from surfacing it.
