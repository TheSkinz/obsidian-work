---
title: The unidentified Grok Bot connector is OneDrive — auth status still unchecked
created: 2026-09-06
status: open
type: idea-seed
tags: [grok-bot, connectors, loose-end]
---

# The third connector is OneDrive

**Identified the same evening it was filed.** The Architect Bot enumerated the account's connectors:
**Gmail, Google Drive, OneDrive, GitHub.**

Gmail and Google Drive were auto-added to the Chief of Staff Bot at signup, and Gmail was never
signed in. GitHub was added deliberately on 2026-09-06 to test the Git-event trigger, and **its
token was deleted the same evening** once the webhook path proved better. That leaves **OneDrive**,
which nobody knowingly installed — and it matches the marketplace header going from `2 installed` to
`3 installed` mid-session with nothing in the session adding one.

## The part that is still open, and it is the part that matters

**Existence is not the risk. Authentication is.** An installed connector with no sign-in is inert —
Gmail sat in exactly that state all session, listed as Added and doing nothing. An installed
connector *signed in to a Microsoft account* is a different proposition on a machine where **every
Bot shares one browser session and one credential store**, and OneDrive is where the per-facility
bid working copies live.

**To check:** Settings → installed plugins → does OneDrive show a connected account?

**If it does:** disconnect it. Nothing in the trial design uses OneDrive, its connector is read-only
in any case, and the trial has otherwise run deliberately credential-free — the one departure, the
GitHub PAT, was made for a single answer and reversed within hours.

**If it does not:** close this note. An unauthenticated connector is clutter, not exposure, and can
be removed at leisure or left alone.

## Not raised as an incident

The account is personal and holds no USADebusk credentials by design. This is a "know what is
installed, and know what it can reach" item. It became worth writing down only because the sharing
model makes any authenticated connector account-wide by construction — which the xAI docs state
outright: do not use separate Bots as a security boundary.
