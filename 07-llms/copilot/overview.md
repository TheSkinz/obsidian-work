---
title: Microsoft Copilot — Overview
created: 2026-06-29
tags: [copilot, microsoft, email, outlook]
---

# Microsoft Copilot

Copilot is used primarily through Outlook (email triage and drafting) and as a reasoning layer over the Outlook folder/category architecture.

## Email architecture — three-tier model

**Tier 1: Outlook folders** — encode state (where is this email in its lifecycle?). Nine folders define the pipeline:

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

**Tier 2: Categories** — encode meaning (what kind of thing is this?). Fourteen categories total:

- 7 lifecycle categories (Action Required, Awaiting Reply, Proposal, Awarded, Active Job, Closed, Reference)
- 6 facility roster categories (one per key customer / facility)
- 1 risk category (Flag: Risk / Review)

**Tier 3: Copilot** — the reasoning layer. Reads folder state + categories to answer questions like "what bids are pending for Valero?" or "what's outstanding from last week?" without manually searching.

## Outlook email security architecture

Deployed a 5-rule corrective architecture to fix email deliverability and sorting issues. Known gap: smtp.com in Rule 02A was flagged during design — confirm whether it's still a live gap.

## Agent creation

(Placeholder — add notes from any Copilot agent setup sessions when they occur.)

## Sycophancy-reduction custom instructions

(Placeholder — document the custom instructions approach once finalized.)
