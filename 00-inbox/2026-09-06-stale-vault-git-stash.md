---
type: review
status: open
review_type: finding
source_authority: primary
confidence: high
created: 2026-09-06
review_after: 2026-12-06
related:
  - "[[DSP26006]]"
tags: [git, housekeeping, vault-hygiene]
---

# The vault carries a six-week-stale git stash

## What it is

`git stash list` in `C:\Users\Jwuts\obsidian-work` returns one entry:

```
stash@{0}: WIP on main: e4b7cb0 vault: DSP26006 — record filtration rate-basis variance as settled
```

Verified 2026-09-06 by reading git directly, not from a note:

| Fact | Value |
|---|---|
| Base commit | `e4b7cb0`, **2026-07-27** |
| Distance to current HEAD | **431 files, ~30,500 insertions** that HEAD has and the stash does not |
| Contains the rate rollup? | No — `tools/rate_history_rollup.py` postdates it entirely |

## Why it is worth a note rather than an action

**It is a stale snapshot, not unlanded work.** The diff runs the wrong way for that reading: HEAD is
tens of thousands of lines *ahead* of the stash, not behind it. Nothing in it is waiting to be
recovered, and six weeks of vault work happened after it was taken.

**So the hazard is misreading, not loss.** A session that runs `git stash list`, sees one entry, and
treats it the way a stash is normally treated — something in flight, worth popping — would overwrite
current work with a July snapshot. That is the only way this causes harm, and it is entirely
preventable by writing down what it is.

**Do not pop it. Do not drop it either** without Jesse looking — dropping is irreversible and there is
no cost to leaving it where it is.

## A near-miss worth recording

`memory/project-knowledge-loop-os.md` carried, correctly, that *"the three Fable-branch git stashes
flagged 2026-07-07 are gone — `git stash list` is empty in both repos"* as of **2026-07-22**. That was
true when written. This stash was created **2026-07-27**, five days later, and is a different object.

The memory was not wrong; it was **superseded by an event nobody re-checked**. The failure mode is
reading a dated "verified empty" as a standing property. The memory now says so explicitly.

## Decision

- [ ] Drop the stash (irreversible — confirms nothing in it is wanted)
- [ ] Keep it and leave this note open as the explanation
- [ ] Inspect it first (`git stash show -p stash@{0}`) before deciding
