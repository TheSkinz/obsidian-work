---
type: idea-seed
status: unexplored
created: 2026-08-21
tags: [idea, vault-system, decision-queue, future]
---

# Nothing catches a queue row whose decision was already made

Idea seed captured 2026-08-21 for a future exploration session. The read below is
tentative — confirm intent with Jesse before designing.

**Tentative read:** DQ-021 sat in the Open table for four days after Jesse ruled
on it. Its source note had read `status: resolved` with a checked Decision box
since 2026-08-17, and nothing noticed. `unqueued_decisions()` in
`tools/vault_health.py` tests exactly one direction — open review notes that no
queue row cites, which reads 0 — and nothing tests the reverse. The cost was not
just a stale row: walking the queue, DQ-021 was selected as the highest-priority
live decision to put in front of Jesse, and it was already answered.

**To explore:** the naive form of this check is wrong, and that is the
interesting part. Auditing all ten open rows by "is the source note terminal?"
flagged three — DQ-017, DQ-018 and DQ-021 — and **only DQ-021 was genuinely
stale**. The other two ask questions that *arose from* their source notes rather
than the questions those notes answered: DQ-017's note was parked on the original
re-grain question in July while the row asks whether to un-park it now, and
DQ-018's note is `complete` because the retirement sweep *ran*, with the row
asking about a gap the sweep exposed. So the obvious rule fires at 1-for-3, and a
33%-precision flag on a ten-row table is noise, not a finding.

What would have to be true for a real check: some machine-readable signal that a
row's ask and its source's decision are the *same* question. Frontmatter linking
a row id to the specific decision block it depends on would do it, but that is a
schema change to every review note and it has to be worth more than reading ten
rows by hand once a month. DQ-028's priority test also applies — this audits
internal governance machinery while other candidates guard customer-facing
documents.

Worth measuring before building: replay the rule over the queue's full closed
history and count how many rows it would have flagged correctly versus falsely.
One real instance in a ten-row table may not justify machinery at all, and the
honest outcome of this seed may be "read the queue by hand when walking it."

**Note on capture:** the Idea Research Loop was disabled 2026-08-21, so this seed
will not be picked up automatically. It needs a session, or the loop back.
