---
title: The unidentified Grok Bot connector was OneDrive, added deliberately — closed
created: 2026-09-06
status: closed-unactioned
type: idea-seed
tags: [grok-bot, connectors]
---

# Closed the same evening: Jesse added it

**Filed as a loose end, resolved within the hour, and there was nothing wrong.**

The marketplace header went from `2 installed` to `3 installed` mid-session and nothing in the
session had added a connector, so it was written up as an unidentified capability on a machine where
every Bot shares one credential store. The Architect enumerated the account: **Gmail, Google Drive,
OneDrive, GitHub.**

**The third was OneDrive, and Jesse added it deliberately** — against possible future use, with no
decision yet on whether to use it. Not a stray, not an auto-install, not a finding.

## Why it is kept rather than deleted

Two things worth carrying forward, neither of them a concern:

**The account's connector list is now on record** — four, with a reason for each. Gmail and Drive
auto-added at signup with Gmail never signed in; OneDrive added by hand; GitHub added for the
Git-event test with its token deleted the same evening.

**The observation method worked.** The gap was caught by watching a counter change, and closed by
asking the Architect to enumerate rather than by guessing. That is the pattern worth repeating —
the wrong move would have been to reason about what the third connector *probably* was.

## The one standing fact, not an action

OneDrive holds the per-facility bid working copies, and every Bot on the account shares one browser
session. If it is ever signed in, it is signed in for all of them. Its connector is read-only in any
case, and whether to use it is Jesse's call to make when he gets to it.
