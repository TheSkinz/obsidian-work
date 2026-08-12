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

> **⚠ SUPERSEDED THE DAY IT WAS WRITTEN — 2026-08-11. Everything below the line describes folders that do not exist.**
>
> Written from the three-tier model in [[copilot/overview]] without checking the live mailbox. Verified the same evening and the model is wrong: the real folders are `00 Action - Today`, `01 Waiting On Others`, `02 Internal Review`, `03 Sent - Pending Response`, `04 Execution Active`, `05 Automation & Systems`, `06 IT / Security`, `07 Read Later`, `99 Archive`.
>
> The document below describes a commercial pipeline; the mailbox is a personal triage workflow. The quote-lifecycle mapping — `04-Proposals-Sent` → `05-Awarded` as the DSP-to-USA transition — refers to two folders that do not exist, and it was the section this document was built around.
>
> The projected copy in the SharePoint `Knowledge` library is set `Status: stale` / `Confidence: low`. Rewrite pending Jesse's account of what each real folder means and a confirmed category list; the structure below (legend → orthogonality rule → lifecycle join → valid/invalid inferences) is worth keeping, the content is not.

How email is organised in this mailbox, and what each folder and category *means*. Written so that
a model reading the mailbox can reason about an email's state instead of guessing from its text.

The structure is three tiers, and the reason they are separate tiers is the whole design. **Folders
encode state** — where a message sits in its lifecycle. **Categories encode meaning** — what kind of
thing the message is and who it concerns. **Copilot is the reasoning layer** over both. Because state
and subject are independent axes rather than one collapsed folder tree, a question like *"what bids
are pending for Valero?"* resolves by intersecting a folder with a category, with no search over
message bodies and no inference from wording.

## Tier 1 — Folders encode state

Nine folders define the pipeline. A message sits in exactly one of them, and the folder is the
authoritative statement of where that message is in its lifecycle.

| Folder | Meaning |
|---|---|
| 01-Inbox-Active | Needs action |
| 02-Waiting | Sent, awaiting reply |
| 03-Proposals-Active | Open bids |
| 04-Proposals-Sent | Submitted, awaiting award |
| 05-Awarded | Award confirmed, job pending |
| 06-Execution | Job in progress |
| 07-Closed | Completed |
| 08-Reference | No action, retain |
| 09-Archive | Done, low-value |

Folders 03 through 07 are a commercial progression and move in one direction. Folders 01, 02, 08 and
09 are not stages of that progression — they are handling states that any message can be in.

## Tier 2 — Categories encode meaning

Fourteen categories in three groups. A message may carry several categories at once, or none.

**Seven lifecycle categories:** Action Required, Awaiting Reply, Proposal, Awarded, Active Job,
Closed, Reference.

**Six facility roster categories**, one per key customer or facility. The roster covers the accounts
worked most often, not every customer in the business, and its membership changes as accounts do —
so read the category names off the messages themselves rather than expecting a fixed list here. A
message with no facility category is simply from a customer outside that roster.

**One risk category:** `Flag: Risk / Review`.

## The orthogonality rule

This is the most important rule in the document, because ignoring it produces confident wrong
answers.

Folder and category are independent. The folder says *where the message is*; the category says *what
it is about*. A message in `04-Proposals-Sent` carrying the `Proposal` category is not redundant, and
a message in `07-Closed` still carrying `Active Job` is not a contradiction to be resolved.

**Where the two disagree, the folder wins.** Categories are applied at the time a message is handled
and are not swept when a message moves on, so a stale category is expected and carries no meaning.
Never infer that a job is live because a message carries `Active Job`; infer it from the folder.

## How the folders map to the quote lifecycle

The commercial folders track the same progression as the document-numbering scheme, which is why
this mapping is worth stating explicitly.

| Folder | Commercial stage | Governing number |
|---|---|---|
| 03-Proposals-Active | Bid being prepared | DSP##### |
| 04-Proposals-Sent | Submitted, awaiting decision | DSP##### |
| 05-Awarded | Award confirmed | USA##### assigned at this transition |
| 06-Execution | Job running | USA##### |
| 07-Closed | Job complete | USA##### |

A quote number (DSP#####) is assigned at proposal. A job number (USA#####) is assigned **on award**,
and all job execution documents file under it. So a message moving from `04-Proposals-Sent` to
`05-Awarded` is the point where the governing number changes — that transition is the single most
useful signal in the whole folder structure, because it is where a bid becomes a job.

## What can and cannot be inferred

**Valid.** Mail in `03-Proposals-Active` or `04-Proposals-Sent` represents live commercial exposure;
mail in `07-Closed` does not. Mail in `02-Waiting` has an outstanding reply owed by someone else, so
it is the correct place to look for follow-up that has gone quiet. Mail in `06-Execution` concerns a
job that is running now.

**Not valid.** Absence of a facility category does **not** mean the message is unrelated to a
facility — only that the customer is outside the key-customer roster. `09-Archive` is low-value
retention, not a deletion queue or a rejection. A message in `08-Reference` is not inactive work; it
is material deliberately kept because it will be needed again.

**When a question spans both axes, intersect them rather than choosing one.** Pending bids for a
given customer is `03-Proposals-Active` plus `04-Proposals-Sent`, intersected with that customer's
facility category. Answering from either axis alone will be wrong.

## Out of scope

A separate five-rule email security architecture is deployed on this mailbox, covering inbound
deliverability and sorting. That is a different concern from routing semantics and its rule bodies
are not recorded in the vault — do not infer them from this document. One known gap is open and
unaudited: smtp.com in Rule 02A, flagged at design time with a 48-hour post-deploy audit
recommended that has not been confirmed.
