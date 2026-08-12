---
title: Outlook Email Architecture
created: 2026-08-11
tags: [outlook, copilot, email, routing, workflow, m365]
related:
  - "[[copilot/overview]]"
  - "[[quote-lifecycle]]"
  - "[[company-context]]"
---

# Outlook Email Architecture

How email is organised in this mailbox, and what each folder and category *means*. Written so that
a model reading the mailbox can reason about a message's state instead of guessing from its text.

The structure is three tiers. **Folders encode handling state** — what needs to happen to a message
next. **Categories encode meaning** — what the message is about, which customer it concerns, and
where it sits commercially. **Copilot is the reasoning layer** over both.

**The commercial lifecycle lives on the categories, not the folders.** This is the single most
important thing on this page. The folders are a personal triage system; they say whether something
is waiting on you, waiting on someone else, or done being handled. They do not track a bid from
proposal to award to close. The categories do. Any question about where a bid stands is answered
from the category axis, and answering it from the folder axis will be wrong.

## Tier 1 — Folders encode handling state

Nine custom folders, alongside the standard Inbox, Drafts, Sent Items, Deleted Items and Archive. A
message sits in exactly one.

| Folder | Handling state |
|---|---|
| 00 Action - Today | Needs action from Jesse |
| 01 Waiting On Others | Someone else holds the next action — customer, colleague, or vendor |
| 02 Internal Review | Package built, not yet customer-facing |
| 03 Sent - Pending Response | Customer has it, awaiting their decision or clarification |
| 04 Execution Active | Concerns a job that is running |
| 05 Automation & Systems | Non-commercial: tooling, notifications, system mail |
| 06 IT / Security | Non-commercial: IT and security traffic |
| 07 Read Later | No action, retain to read |
| 99 Archive | Done being handled |

Folders 05, 06 and 07 are outside the commercial workflow entirely. Sorting is done by hand, so
folder placement reflects attention rather than an automated rule — a message can be correctly
filed and still lag reality by a day.

## Tier 2 — Categories encode meaning

Fourteen categories in three groups. A message may carry several at once, or none.

**Seven lifecycle categories**, and these are what track commercial state: `Action Required`,
`Awaiting Reply`, `Proposal`, `Awarded`, `Active Job`, `Closed`, `Reference`.

**Six facility categories**, one per key customer, as of 2026-08-11: `Formosa Point Comfort`,
`Valero Port Arthur`, `Monroe Energy`, `Exxon Baytown`, `Targa Mont Belvieu`, `HF Sinclair`. The
roster covers the accounts worked most often, not every customer in the business, and its
membership changes as accounts do — the names on the messages are authoritative if this list ever
disagrees with them. A message with no facility category is from a customer outside the roster,
which is not the same as being unrelated to a facility.

**One risk category:** `Flag: Risk / Review`.

## The orthogonality rule

Folder and category are independent, and each answers a different question. The folder says *what
needs to happen next*; the category says *what this is and where it stands*. A message in
`01 Waiting On Others` carrying `Proposal` and `Exxon Baytown` is not redundant — it is a bid at
Exxon Baytown where the next move belongs to someone else.

**Where the two seem to disagree, prefer the category for commercial state and the folder for
handling state.** Neither overrides the other, because they are not describing the same thing.
Sorting is manual, so a message can sit in `99 Archive` while still carrying `Active Job` — read
that as the mail being done, not the job.

## The quote lifecycle — on the category axis

The lifecycle categories track the same progression as the document-numbering scheme.

| Category | Commercial stage | Governing number |
|---|---|---|
| Proposal | Bid prepared or submitted | DSP##### |
| Awarded | Award confirmed | USA##### assigned at this transition |
| Active Job | Job running | USA##### |
| Closed | Job complete | USA##### |

A quote number (DSP#####) is assigned at proposal. A job number (USA#####) is assigned **on award**,
and all job execution documents file under it. So the move from `Proposal` to `Awarded` is the point
where the governing number changes — the single most useful signal in the whole scheme, because it
is where a bid becomes a job.

## What can and cannot be inferred

**Valid.** A message carrying `Proposal` without `Awarded` or `Closed` is live commercial exposure.
`01 Waiting On Others` is where to look for follow-up that has gone quiet, whoever owes it.
`Awaiting Reply` plus `Proposal` is a bid with no customer response yet. `04 Execution Active` and
`Active Job` together concern a job running now.

**Not valid.** Do not infer commercial stage from a folder — there is no Awarded folder, no Closed
folder, and `03 Sent - Pending Response` is a handling state, not a bid state. Absence of a facility
category means the customer is outside the roster, not that the message is unrelated to a facility.
`99 Archive` means handled, not rejected, and says nothing about whether the underlying job or bid
closed. Categories are applied when a message is handled and are not swept afterwards, so a stale
category is expected.

**Where a question spans both axes, intersect them.** Open bids for a customer is the `Proposal`
category minus `Awarded`/`Closed`, intersected with that customer's facility category — not a folder
query.

## Provenance

Folder names were read directly from the mailbox on 2026-08-11, and the category list confirmed by
Jesse the same day. The descriptions of what each folder is *for* are Jesse's account of his own
practice, not a documented specification — the folders were set up quickly and are maintained by
hand, so treat the handling-state column as intent rather than a guaranteed invariant.

A previous version of this document described a nine-folder commercial pipeline that did not exist
in the mailbox. If any other note still refers to folders named `01-Inbox-Active`,
`03-Proposals-Active`, `04-Proposals-Sent`, `05-Awarded`, `07-Closed` or `08-Reference`, it is
wrong and predates this correction.

## Out of scope

A separate five-rule email security architecture is deployed on this mailbox, covering inbound
deliverability and sorting. That is a different concern from routing semantics and its rule bodies
are not recorded in the vault — do not infer them from this document. One known gap is open and
unaudited: smtp.com in Rule 02A, flagged at design time with a 48-hour post-deploy audit
recommended that has not been confirmed.
