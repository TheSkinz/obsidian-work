<!-- vault-loop: operational — 50-dashboards/decision-queue.md structure/governance; capture loop cannot write this content. -->
---
type: note
status: inbox
created: 2026-08-01
tags: [inbox, vault-system, dashboards, observation]
---

# decision-queue.md has two different Closed tables

Noticed 2026-08-01 while closing DQ-004 and DQ-005.

`50-dashboards/decision-queue.md` carries two separate closed sections with
different column sets:

- `## Closed` — `id | opened | closed | source | ask | outcome` (holds DQ-003,
  and now DQ-004 and DQ-005)
- `## Closed / expired` — `id | decided | date | by` (holds DQ-001 and DQ-002)

They're split by a long `## Why the queue is empty at launch` prose block, so it
isn't obvious both exist unless you read to the bottom. I put the two new rows in
the first one because it matches DQ-003's shape and carries the ask, which is the
more useful record — but that was a judgment call, and the next person or agent
closing a row has the same coin-flip.

The `## Why the queue is empty at launch` section is also stale as written: it
explains a launch-time state from 2026-07-05 and asserts the queue has no
genuinely-open decisions to seed, which stopped being true once DQ-003 through
DQ-005 were filed.

Small and cosmetic, but it's a dashboard the loops write into, so ambiguity about
where a row goes will compound. No fix proposed — flagging the choice.
