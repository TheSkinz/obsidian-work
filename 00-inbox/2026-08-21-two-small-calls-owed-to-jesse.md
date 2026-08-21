---
type: note
status: inbox
created: 2026-08-21
related:
  - "[[2026-08-18-idea-research-researched-status-outlives-build]]"
  - "[[2026-08-20-vault-architecture-audit-evidence]]"
tags: [owed, status, archive, governance]
---

# Two small calls owed to Jesse from the 2026-08-21 close-out

Both surfaced during the architecture-audit execution. Neither is worth a decision-queue row —
each is roughly one line — but both are claims about work rather than formatting, so neither is
mine to make.

## 1. `archive/idea-pig-load-list-generator.md` sits at `status: complete`

Its own closing paragraph says the pig **load list** generator "was not built and is not closed by
this." What shipped was the shared rollup script (`tools/pig_usage_rollup.py`).

Arguably `complete` is true for the note's scope and false for its title. The risk is concrete: a
future session reads the filename at `status: complete` and concludes the load-list generator
exists. It does not, and the per-project load list is still wanted.

Options: leave it (the body is explicit), change it to something non-terminal, or split the note.
Jesse's call.

## 2. Seventeen `archive/` notes exist on disk and nowhere else

`archive/` is in `.gitignore`. Of the 34 notes with no inbound links, 17 are tracked — those were
deleted on 2026-08-21 and are recoverable from history. The other **17 are untracked**: the
pre-canonical heater-card snapshots plus an `ai-config` snapshot. They were left in place because
the verdict's justification ("git history preserves every one") is false for exactly those.

They cost nothing to keep — gitignored content carries no repo weight and `INDEX.md` has never
covered `archive/`. The open question is only whether the pre-migration card snapshots are worth
retaining at all now that every one of those cards has been migrated and committed. If they go,
they go permanently.

**Recorded in CLAUDE.md** so no future session repeats the recoverability assumption.
