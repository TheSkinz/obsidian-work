---
type: note
status: inbox
created: 2026-09-05
review_after: 2026-09-19
tags: [inbox, tooling, dashboards, integrity]
---

# The health dashboard reverted to an older generation and read `ok`

**Found by accident, which is the part that matters.** During the 2026-09-05 close-out, `git status`
showed `50-dashboards/health.md` modified when nothing in the session had touched it. The diff ran
**backwards**: the working tree held a file stamped `Generated: 2026-08-24` against a committed
`2026-09-03`.

The stale copy understated everything and hid a failure:

| Metric | Stale copy (08-24) | Committed (09-03) | Regenerated (09-05) |
|---|---|---|---|
| Inbox items | 60 | 72 | 73 |
| Inbox oldest item | 27 d — `ok` | 35 d — **FAIL** | 37 d — **FAIL** |
| Inbox median age | 6 d | 13 d | 15 d — **FAIL** |
| Lint warnings | 6 | 8 | 9 |

**A stale generated file that reads `ok` is worse than a missing one, because nothing about it looks
wrong.** The header carries a `Generated:` date, but nothing compares that date to anything, and the
vault's startup routine reads this file precisely to surface red rows. For two days the routine would
have reported a clean dashboard.

Regenerated in config `5313e98`. Both FAIL rows now stand and were deliberately left standing.

## What is not known

**Who wrote it.** A concurrent session and a restored copy are both plausible; neither is established
and this note is not going to guess. Two other Claude sessions were live in this vault on 2026-09-04.

## Why it belongs in the same file as the rest of that day's findings

This is the same failure class the 2026-09-05 harness audit work kept hitting: **a mechanism that
reports health while measuring nothing.** The `fixture-replay-guard` had never fired in 185 sessions.
`git-guard` fired 6 times with 0 true positives. `staged-count-guard` counted the wrong repository.
Each looked like a working control. This one looked like a working dashboard.

## To decide — not urgent, and possibly not worth mechanising

- **Cheapest option: nothing.** The file is regenerated whenever anyone runs `vault_health.py`, and this
  is the first observed instance. One incident is not a pattern.
- **Cheap and probably enough:** have `vault_health.py` refuse to leave a file whose `Generated:` date is
  older than the one it is replacing, or warn on it. That catches a revert without watching for one.
- **What NOT to do:** build a checker that watches the dashboard. A monitor for the monitor is the shape
  this vault has already retired twice.

The honest read is that the regeneration is one command and the failure is rare, so the value here is
mostly the *record* — that generated files in this vault can silently go backwards, and that a
`Generated:` date is worth glancing at before trusting a dashboard.

---

## Second instance, opposite direction — a FAIL that is an artifact of *when* the file was written (2026-09-15)

The 09-05 case was a stale dashboard reading `ok` and hiding a real failure. This one is the mirror: a
**current** dashboard reading `FAIL` on a failure that did not happen.

Session startup on 2026-09-15 surfaced `Loop heartbeats overdue | yes | FAIL`, from:

| Loop | Last fired | Last heartbeat | Status |
|---|---|---|---|
| Consolidation loop | 2026-09-15 (0 d ago) | 2026-08-15 (31 d ago) | `FAIL: started, never finished` |

The run finished cleanly. `.loop-runs.json` records `completed: 2026-09-15T08:34:00Z, result: committed`,
and its heartbeat commit `49fb3b6` exists with the exact prefix `vault_health.py:74` looks for
(`vault-consolidate:`).

**The cause is ordering inside a single commit.** The consolidation loop regenerates `health.md` as part
of its run, then commits. So the dashboard is written *before* the heartbeat commit it is searching for
exists, and `git log` cannot yet see it. `health.md` and `49fb3b6` are the same commit — the file is
reporting on a commit it is contained in.

**Every consolidation run produces this**, not just this one. It is not a concurrency accident and not
rare; it is structural to a loop that both regenerates the dashboard and is measured by its own closing
commit. It self-clears the next time anyone runs `vault_health.py`.

**Why it belongs beside the 09-05 finding rather than in its own note.** Same class, both directions now
observed: a generated dashboard whose *timing relative to its own inputs* decides what it reports. The
09-05 note's proposed guard — refuse or warn when the `Generated:` date goes backwards — would not catch
this one, because this file is perfectly current. That is the useful thing the pair says together:
freshness is not the same property as correctness.

**Cost of the false FAIL is not zero.** Vault `CLAUDE.md` instructs every session to surface red rows at
startup, so this one buys a diagnosis on every session that opens after a consolidation run until someone
regenerates. This session spent four tool calls on it.

**To decide — still probably not worth mechanising, but the options changed.** The cheapest real fix is
ordering, not monitoring: have the consolidation loop regenerate `health.md` **after** its heartbeat
commit rather than inside it, or skip the heartbeat row for a loop whose ledger shows `completed` on the
same day. Both are small. Doing nothing is also defensible, but it now has a recurring cost rather than a
one-off one, which is the thing 09-05 could not yet say.
