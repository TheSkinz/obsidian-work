---
title: Grok Bot marketplace gained a third connector nobody identified
created: 2026-09-06
status: unexplored
type: idea-seed
tags: [grok-bot, connectors, loose-end]
---

# A third Grok Bot connector appeared and was never identified

**Observed, not diagnosed.** Early on 2026-09-06 the Grok Bot marketplace header read
**`2 installed`** — Gmail and Google Drive, both auto-added to the Chief of Staff Bot at signup.
Later the same evening it read **`3 installed · 3 private`**. Nothing in the session added a
connector between those two readings; the GitHub connector went in afterwards and was a separate,
deliberate act whose token has since been deleted.

**Why it is worth a look rather than a shrug.** Every Bot on the account shares one computer, one
browser cookie jar and one credential store — the docs say outright not to use separate Bots as a
security boundary. So a connector nobody installed deliberately is a capability nobody scoped
deliberately, on a machine where scope is account-wide by construction. The trial has otherwise run
credential-free on purpose.

**Also unexplained: what `3 private` counts.** The header shows `N installed · N private` and the
meaning of the second number was never established. It may be a separate axis (privately-published
plugins?) rather than a subset.

## To check

Open Marketplace → the `N installed` header → the chevron beside it, which expands to the installed
list. Name the third connector, confirm whether it was auto-added at signup like Gmail and Drive,
and decide whether it stays.

## Not urgent

No evidence of harm — the account is a personal one holding no USADebusk credentials, which was the
deliberate posture. This is a "know what is installed" item, not an incident.
