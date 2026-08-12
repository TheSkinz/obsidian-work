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

## Tier 2 — Categories encode commercial stage

Seven meaningful categories, and they form a single ordered pipeline. A message may carry more than
one where a thread spans a transition.

| # | Category | Stage |
|---|---|---|
| 1 | RFQ | Inquiry received, nothing quoted yet |
| 2 | Proposal Draft | Bid being built |
| 3 | Submitted | With the customer, awaiting decision |
| 4 | Awarded | Won |
| 5 | Execution | Job running |
| 6 | Post-Job | Work complete, closeout and invoicing |
| 7 | Closed / No-Go | Finished, or lost / not pursued |

Outlook's six stock colour categories — `Blue category`, `Green category`, `Orange category`,
`Purple category`, `Red category`, `Yellow category` — are unused defaults and carry **no meaning**.
Ignore a colour category entirely; it says nothing about the message.

**There are no facility or customer categories.** Which customer a message concerns is determined
from its content, the account manager on the thread, or the DSP/USA number — never from a category.

## The orthogonality rule

Folder and category are independent, and each answers a different question. The folder says *what
needs to happen next*; the category says *where the work stands commercially*. A message in
`01 Waiting On Others` carrying `Submitted` is not redundant — it is a bid with the customer, where
the next move belongs to someone other than Jesse.

**Where the two seem to disagree, prefer the category for commercial state and the folder for
handling state.** Neither overrides the other, because they are not describing the same thing.
Sorting is manual, so a message can sit in `99 Archive` while still carrying `Execution` — read that
as the mail being done, not the job.

## The quote lifecycle — on the category axis

The category pipeline tracks the same progression as the document-numbering scheme.

| Category | Governing number |
|---|---|
| RFQ | None yet |
| Proposal Draft · Submitted | DSP##### |
| Awarded | **USA##### assigned at this transition** |
| Execution · Post-Job · Closed / No-Go | USA##### |

A quote number (DSP#####) is assigned at proposal. A job number (USA#####) is assigned **on award**,
and all job execution documents file under it. So the move from `Submitted` to `Awarded` is the point
where the governing number changes — the single most useful signal in the whole scheme, because it
is where a bid becomes a job.

`Closed / No-Go` covers two different endings, a completed job and a bid that was lost or never
pursued. Which one it is depends on whether the thread ever reached `Awarded`, not on the category
itself.

## Who submits a bid — a structural blind spot

Many proposals are written by Jesse for **other people's accounts**, because of their complexity, and
are then handed to Jason or the account manager, who submits to the customer directly.

The consequence for anything reading this mailbox: **the customer-facing send frequently does not
exist here.** A thread can legitimately end with the finished proposal going to a colleague
internally, with the actual submission, the customer's reply, and the award landing in someone
else's mailbox.

So absence of a customer-facing send is the *normal* case for these bids, not evidence of a problem,
and absence of a customer reply is not evidence that none came. Never report a bid as unsent or
unanswered on the strength of this mailbox alone — say the submission is not visible here, and name
the colleague the thread was handed to.

## What can and cannot be inferred

**Valid.** A message carrying `Submitted` without `Awarded` or `Closed / No-Go` is live commercial
exposure. `01 Waiting On Others` is where to look for follow-up that has gone quiet, whoever owes it.
`04 Execution Active` with `Execution` concerns a job running now. `RFQ` with no later
`Proposal Draft` on the same opportunity is an inquiry that was never quoted.

**Not valid.** Do not infer commercial stage from a folder — there is no Awarded folder, no Closed
folder, and `03 Sent - Pending Response` is a handling state, not a bid state. Do not infer anything
from a colour category. Do not conclude a bid was never submitted, or never answered, from this
mailbox alone — see the blind spot above. `99 Archive` means handled, not rejected, and says nothing
about whether the underlying job or bid closed. Categories are applied when a message is handled and
are not swept afterwards, so a stale category is expected.

**Where a question spans both axes, intersect them.** Open bids is the `Submitted` category minus
`Awarded` and `Closed / No-Go`; the customer comes from the thread's content or its DSP/USA number,
not from a category, and the handling folder tells you who owes the next move.

## Provenance

Folder names were read directly from the mailbox on 2026-08-11 and category names from Outlook's own
category list the same day. Both are first-hand readings of the system, not descriptions of it.
Folder meanings and the category ordering are Jesse's account of his own practice — sorting is
manual and the folders were set up quickly, so treat the handling-state column as intent rather than
a guaranteed invariant.

**Two earlier versions of this document were wrong, and in the same way.** The first described a
nine-folder commercial pipeline that did not exist; the second kept fabricated categories —
`Action Required`, `Awaiting Reply`, `Proposal`, `Active Job`, `Closed`, `Reference`, a
`Flag: Risk / Review`, and six customer-named facility categories that were never real. Both wrong
versions came from asking a model to describe the mailbox instead of reading it. Of the fourteen
categories originally claimed, exactly one — `Awarded` — turned out to exist.

Any note still referring to folders named `01-Inbox-Active`, `03-Proposals-Active`,
`04-Proposals-Sent`, `05-Awarded`, `07-Closed`, `08-Reference`, or to facility categories, predates
this correction and is wrong.

## Out of scope

A separate five-rule email security architecture is deployed on this mailbox, covering inbound
deliverability and sorting. That is a different concern from routing semantics and its rule bodies
are not recorded in the vault — do not infer them from this document. One known gap is open and
unaudited: smtp.com in Rule 02A, flagged at design time with a 48-hour post-deploy audit
recommended that has not been confirmed.
