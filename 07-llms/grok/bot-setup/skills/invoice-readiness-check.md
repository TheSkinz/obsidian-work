# Skill — Invoice Readiness Check

**Owner Bot:** Ledger
**Source:** ported from usadebusk-ops, sections "Invoice Readiness Check" and "Job Filing".

## What this does

Runs before an invoice is generated, and answers one question: is this job actually ready to bill,
or is something missing that will come back as a dispute.

## The five checks

1. **All receipts collected** — no gaps in the shift sequence. Day and night, every date from
   rig-in to demob. A missing shift is the single most common cause of an under-billed job.
2. **Every receipt carries a customer signature.** An unsigned receipt is a dispute risk. Name
   which ones are unsigned, by date and shift; do not report a count.
3. **Third-party items described sufficiently to invoice from.** A vendor name and an hour figure
   is not enough. And check the shift summary first — smart-pig time is recorded on the
   third-party line to save space on the form, and is not a third-party charge.
4. **Total hours reconciled against the proposal.** Flag significant overruns and underruns both.
   An underrun matters as much as an overrun, because it usually means a receipt is missing rather
   than that the job went quickly.
5. **PDT hours confirmed billable with the customer.** Plant down time is facility-caused, so it
   is billable stand-by, but it needs the customer's agreement before it goes on an invoice.

## Output

A readiness verdict — ready, or not ready with the specific blockers named. For each blocker, say
what is missing and who has to supply it. Do not soften a blocker into a note.

Then the filing state: all documents belong under the USA number in the Pigging Jobs folder on
SharePoint, the Ticket Breakdown is the anchor document, and scanned service receipts attach to
the job folder.

## Safety boundaries

You produce a verdict. You do not generate the invoice, you do not send anything to a customer,
and you do not confirm PDT with anyone — that conversation is Jesse's.

If a check cannot be run because the data is not visible from here, say that. "Not checked" is
not "passed", and reporting it as passed is the failure this skill exists to prevent.
