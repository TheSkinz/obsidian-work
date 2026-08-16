<!-- vault-loop: operational — tools/vault_lint.py + health.md severity-tiering; capture loop cannot write this content. -->
<!-- vault-prestaged: 2026-08-16-prestaged-pointer-dead-severity-tiering.md -->
---
type: note
status: inbox
created: 2026-08-01
tags: [inbox, vault-system, lint, observation]
---

# POINTER-DEAD sits in the warning backlog but means a live broken reference

Observed 2026-08-01 while fixing the DSP26071 folder move. Three POINTER-DEAD
warnings were open. All three were real, and **two had been dead since 2026-07-23**
— DSP26080's pair recorded `Jobs\` when the folder was under `Bids\`, and
H-2501's named a parent folder that doesn't exist. Nine days, unnoticed.

The reason they sat: `health.md` treats lint warnings as "the standing to-do list
(provenance-frontmatter backfill, stale `related:` links), not failures," and the
warning count is a single number with an `ok` status. POINTER-DEAD is grouped with
cosmetic backlog like ORPHAN and OP-FRONTMATTER, so nothing distinguishes "a
`related:` link is stale" from "the path to a customer's quote and workup no longer
resolves."

Sharpest version of the problem: DSP26071's pointer was dead with the job
mobilizing in ten days. The failure mode isn't the lint missing it — the lint
caught all three correctly — it's that a caught finding in the warning bucket has
no path to anyone's attention.

Also worth noting the trigger shape: pointers go stale when the OneDrive tree is
reorganized, which happens on award (Bids → Jobs) and at cleanup. That's an event,
not a decay — so it clusters, and a check right after a reorganization would catch
a batch.

Not proposing a fix. Recording the observation because I only found these by
reading the raw lint output during unrelated work.
