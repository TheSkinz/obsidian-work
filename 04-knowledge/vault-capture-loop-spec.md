---
type: governance
status: deprecated
source_authority: primary
confidence: high
created: 2026-06-30
last_reviewed: 2026-07-29
review_after: 2026-10-29
related:
  - [[vault-agent-loop-spec]]
  - [[vault-idea-loop-spec]]
  - [[vault-prestaging-loop-spec]]
  - [[knowledge-system-governance]]
  - [[vault-source-of-truth]]
tags: [knowledge-system, agent-loop, capture, governance]
---

# Vault Capture Loop Spec

> **STOPPED 2026-08-21 — this loop does not run.** The scheduled task is disabled; it had become a net producer of work (its last run ingested 1 item and harvested 2). The spec is kept because the loop is disabled, not deleted, and can be re-enabled. `status: deprecated` above means "no longer running", not "superseded" — nothing replaced it. Current status of all six loops: `01-context/system-workflow-reference.md`.

The scheduled, low-effort half of the vault automation. Its job: quietly file what you drop in `00-inbox/` and harvest durable findings from recent sessions, so knowledge lands in the right place without you doing it by hand. Companion to [[vault-agent-loop-spec]], which handles the high-stakes operational core on-demand.

The design intent, stated plainly: **drop `.md` files into `00-inbox/` whenever you want, and a periodic run ingests them automatically.** You should never feel audited by this loop — it files and harvests, it does not police.

## Loop Name

Vault Capture Loop

## Trigger

A local **desktop scheduled task**, daily at ~05:00 local (`0 5 * * *`). Was weekly/Mondays until 2026-07-28, when it moved to daily to cut worst-case inbox latency from 7 days to 1. The **05:00 fire time is deliberate**: the first daily setting used 08:00, which sits inside Jesse's working hours, and its very first run landed concurrently with a live session mid-edit. A pre-working-hours fire keeps the loop clear of interactive sessions and the git index contention that comes with them. A run with nothing new is a clean no-op and produces no commit — that is the expected majority case at daily cadence, and the dashboard reads it as healthy. It runs against the local working tree and harvests Claude Code session transcripts (plain JSONL under `~/.claude/projects/`, which are not in git), so it cannot run in the cloud. If the machine is asleep or the app closed at trigger time, it runs on next launch. There is no in-session cron variant — the scheduled task is the single mechanism.

## Scope

Governs the **content layer** only:

- `00-inbox/` — content routing and triage (the primary job)
- `07-llms/`, `08-systems/`, `09-interests/` — destination content layers

Never touches `02-facilities/`, `04-knowledge/`, pricing, SOP, safety, field-execution, customer-facing content, or heater-card facts. Those belong to [[vault-agent-loop-spec]]. If a harvested finding or an inbox item is operational, this loop leaves it in `00-inbox/` with a one-line routing note and stops — it does not write the operational core.

**The defer marker is a handoff, not a dead end (documented 2026-07-29).** The `<!-- vault-loop: -->` comment this loop writes is the **only input queue** [[vault-prestaging-loop-spec]] watches — that loop fires an hour behind this one at 06:00 precisely so it reads the current day's deferrals. Two consequences worth stating on this side of the coupling, because until now it was documented only on the other: the marker's comment form is load-bearing and must not be changed casually, and a deferred item is not abandoned — it is scheduled for analysis. Items carrying `<!-- vault-prestaged: -->` have already been through that loop and are not re-deferred.

`02-facilities/` deserves a note. The 2026-07-06 facility-data ruling in [[knowledge-system-governance]] made heater-card and facility content **Lane 1 in full**, and that policy's own area map says inbox filing in all domains is Lane 1 with operational docs filed **as drafts, not deferred** — so this loop's blanket refusal is stricter than governance requires. It is kept deliberately: the difference is that Lane 1 contemplates an interactive session, and this loop runs unattended at 05:00 with no one reading the result. Widening an unattended loop's write scope into operational folders is its own decision, not a consequence of the Lane 1 ruling. Audited 2026-07-29 and the restriction is currently costing nothing — every deferred item then in the inbox was estimating, pricing, tooling, or governance content that is Lane 4 regardless.

## Ceremony Level

Low. The content-layer blast radius is small and every write is versioned in git:

- Appending to or creating notes in the governed folders is allowed **without** a prior review note.
- Silent deletion is never allowed. Removals are proposed, not executed.
- The run ends by committing (and pushing) — see Durability. Git is the backup and the single source of truth; a commit is recoverable, not a corruption risk.
- Operational findings always defer to the on-demand operational loop.

## Loop Steps

**Run ledger (every run, first and last action):** Before anything else, update `50-dashboards/.loop-runs.json` (local, gitignored — create if missing): set this loop's entry (`vault-capture-loop`) to `{"fired": "<now, UTC ISO-8601>", "completed": null, "result": "running"}`, merging without touching other loops' entries. As the run's very last action — after the final push, or immediately on deciding the run is a no-op or hitting a fatal problem — set `completed` to now and `result` to `committed`, `no-op`, or `error: <one line>`. Use Write/Edit tools, never shell editors. `tools/vault_health.py` reads this file to tell a dead scheduler from a quiet loop; a run that skips it surfaces as a monitoring FAIL.

1. Load last-run state from `00-inbox/.capture-state.json` (create if missing; default `last_run` = 7 days ago).
2. **Ingest inbox** — for each `.md` file in `00-inbox/`, apply the three-outcome routing model. This is the primary job and runs first.
3. **Harvest transcripts** — scan transcripts in scope (see Transcript Scope) modified since `last_run`, applying the self-exclusion rule and the Save-vs-Skip filter. For each durable finding: rewrite declarative present-tense, then route to an existing note (append) or create a new one.
4. Update `00-inbox/.capture-state.json` (see Delta Tracking).
5. Run `python tools/vault_lint.py --worktree` (use `py -3` if `python` is not on PATH); it must report **0 errors** before committing. Fix any error the run introduced — warnings are acceptable. **The `--worktree` flag is load-bearing** (added 2026-08-15): a bare invocation skips the diff rules entirely, so `CHECKBOX-DELTA` — the guard against a decision silently recorded on an already-closed note — had no unprompted trigger anywhere in the vault. This loop's daily cadence is now that trigger. A `WORD-DELTA` finding on this loop's own edits is expected where the run legitimately rewrote a harvested note; read it, don't reflexively clear it. Do **not** append a run summary to `change-log.md`: per the 2026-07-05 narrowing rule, `change-log.md` is decisions-only and the run record lives in the commit message (the `vault-capture:` heartbeat) and git log.
6. **Refresh generated files** — run `py -3 tools/vault_index.py` and `py -3 tools/vault_health.py` so `INDEX.md` and `50-dashboards/health.md` reflect this run's ingested/harvested notes; include both in the commit. (Generated files are the sanctioned overwrite exception; added 2026-07-07.)
7. **Commit and push** (see Durability).

## Transcript Scope

Scan all `~/.claude/projects/` directories, incremental by file mtime since `last_run`. The vault owns the LLM/systems/interests layers, and findings on those occur across projects, so breadth is intentional.

**Self-exclusion (mandatory).** Skip the loop's own run:

- Exclude the active session's transcript and any subagent transcripts it spawned (the run's own session id, and anything under `…/<session-id>/subagents/`).
- Exclude any transcript whose mtime falls inside the current run window — it is being written as the loop executes and is not a settled source.

This rule is what prevents the loop harvesting its own reasoning. It must be applied before the Save-vs-Skip filter.

**Relevance.** Breadth is intentional, but a transcript whose project cwd is clearly unrelated to the vault (e.g. a `system32` shell session) may be dispositioned `skip` without deep reading. mtime + Save-vs-Skip + this light relevance check are the only filters.

**Coverage hole: only local sessions are harvestable (documented 2026-07-29).** The scope is `~/.claude/projects/`, which exists only for sessions running as a local Claude Code process. Cloud sessions (`claude --cloud`, the Code tab on web and mobile) keep their transcripts on Anthropic infrastructure, and Cowork/Dispatch tasks that stay in the Cowork tab are not Claude Code sessions at all — neither is reachable, and neither leaves a trace this loop can find. Remote Control is the exception that matters: it runs locally and is driven remotely, so a session steered from a phone harvests normally. The rule that follows for those two surfaces is that a durable finding must be **written to a file during the session**, because nothing downstream will catch it. See [[mobile-field-access]].

## Harvest: Save-vs-Skip Filter

(Mined from claude-obsidian `save`.) Capture:

- Non-obvious insights or synthesis
- Decisions with rationale
- Validated patterns and configurations
- Research conclusions

Skip:

- Mechanical lookup Q&A
- Pure execution sessions with no lasting insight
- Setup steps already documented
- Anything already in the vault (update the existing note instead of duplicating)

Write knowledge, not conversation: "X works by Y" not "the user asked about X." Each note must read cold.

## Inbox Routing: Three-Outcome Model

| Outcome | Action |
|---|---|
| Clear home in an existing note | Append the content; cite source. |
| Folder exists but no matching note | Create the new note in that folder. |
| Nothing fits | Leave in inbox, add top-of-file comment `<!-- vault-loop: no home yet, candidate for [topic] -->`, and report it. |

If `00-inbox/` holds 3+ untagged notes on one theme with no existing home, propose a hub note (suggested filename, target folder, one-line scope). Propose only — do not create the hub or move items without approval.

## Terminal-Note Sweep

Added 2026-07-28 as an idea-seed-only sweep; **extended to all note types 2026-07-29** (Jesse, in-session). A finished note left in `00-inbox/` is noise that inflates the inbox count and buries live items — and the type it happens to carry never made that more or less true. At the end of inbox ingestion, move any file whose `status` is in this **exact allowlist** to `archive/`:

`executed` · `resolved` · `complete` · `superseded` · `spec-complete` · `closed-unactioned`

The extension was measured, not assumed: on 2026-07-29 a 49-item inbox held 19 terminal-status notes, of which the seed-only rule covered 9 and left **10** — `type: note`, `task`, `capture`, `spec`, `insight` — sitting indefinitely. Six of those ten also carried a defer marker, so the Pre-Staging Loop was queued to spend runs analyzing questions already closed. `2026-07-23-three-dead-source-pointers.md` was the worked case: opened and resolved the same day, body headed RESOLVED, still in the queue five days later.

**`closed-unactioned` added 2026-08-21** (Jesse, DQ-018). It was terminal to `vault_lint.py` but absent here, so a correctly-retired commitment stayed in `00-inbox/` permanently — four such notes when the question was raised on 2026-08-16, **seven** by the time it was ruled. The "deliberate, a retirement should stay visible" reading was rejected on the list's own contents: `superseded` was already here and is the same shape, a commitment that ended without being done. Note that adding a status here is **inert on its own** while the capture loop is disabled (2026-08-21) — the sweep runs at the end of inbox ingestion and nothing else calls it, so the seven were moved by hand in the same pass.

Rules that make this safe (all of them now apply to every type, not just seeds):

- **Never sweep `researched` or `unexplored`.** `researched` means the Idea Research Loop is done but *Jesse has not decided* — sweeping it would silently discard a pending decision. `unexplored` is the loop's own input queue. Both statuses are idea-seed-specific in practice, but the prohibition is written on status, not type, so a `researched` note of any type is protected.
- **Status must be read with the loop's own markers in mind.** A `<!-- vault-loop: -->` or `<!-- vault-prestaged: -->` comment sits *above* the frontmatter fence, and a naive line-0 frontmatter parser returns nothing for those files — which is exactly the 6-of-10 subset. `tools/vault_lint.py`'s `frontmatter_start()` handles this correctly (fixed 2026-07-29); use that behavior, not a fresh line-0 check. A parser that silently sees no status must **skip**, never sweep.
- **Never rename.** Inbound **wikilinks** resolve by basename and `vault_lint.py` includes `archive/` in its resolution set (deliberately, per the script), so a plain move keeps them green. Renaming breaks them — the initial sweep found 19 inbound links across 7 seeds.
- **A move does not protect backticked *path* references, and nothing lints them** (found 2026-07-29 by cross-checking specs against the code). A repo-relative path written in prose between backticks is a plain string: DEAD-LINK only reads `[[wikilinks]]`, and POINTER-DEAD only reads absolute source paths, so a swept file's path references dangle silently. After any sweep, grep the moved basenames across the vault and convert **live** references to wikilinks. Do not touch references inside `change-log.md` or dated `06-reviews/` notes — those are historical records stating where a file was at the time, and history is not rewritten. The 2026-07-29 sweep produced exactly one live break, on [[DSP26085]], against a dozen correct-as-history mentions.
- **Never sweep a seed carrying `revisit-trigger:`** — that field is a live dormant trigger the health dashboard reports on, regardless of the seed's status.
- Status values outside the allowlist are left alone and reported, not guessed at.

Report the sweep in the run summary (`N swept`). The move is recoverable rather than destructive, but the reason is subtler than it looks: **`archive/` is listed in `.gitignore`**, and `.gitignore` governs only *untracked* files. A seed that was already tracked in `00-inbox/` stays tracked when moved (git records it as a rename — the first sweep staged all 7 as `R100`), so its history survives. A file that was **never committed** would become invisible to git the moment it lands in `archive/`. Therefore: **only sweep a seed that `git ls-files` already shows as tracked.** An untracked seed is left in place and reported, never swept.

## Delta Tracking

(Mined from wiki-ingest `.manifest.json`.) State lives at `00-inbox/.capture-state.json`. Documented schema:

```json
{
  "last_run": "2026-06-30",
  "window_start": "2026-06-23",
  "notes": "free-text operator/run annotations; preserved across rewrites",
  "processed_transcripts": {
    "<project>/<session-id>.jsonl": {
      "hash": "md5",
      "harvested_at": "2026-06-30",
      "disposition": "harvested:<path> | skip:<reason> | defer:operational-<reason>"
    }
  }
}
```

- `last_run` is the high-water mark; `window_start` is the start of the scan window for the run that produced this state (normally `last_run` of the prior run, or 7 days back on a cold start).
- `disposition` records the harvest decision per transcript and is **load-bearing** — preserve it on rewrite.
- When updating state, **merge**: keep prior `notes` and per-transcript `disposition` entries; never blank-overwrite the file.
- Before harvesting a transcript, compare its hash; if unchanged since last run, skip.

## Durability

OneDrive sync has been removed; git is the only backup and the single source of truth. The run therefore ends by committing its writes and pushing to the `obsidian-work` remote:

- Commit message: `vault-capture: <YYYY-MM-DD> run — N ingested, M harvested`. **This `vault-capture:` subject prefix is the loop's heartbeat** — `tools/vault_health.py` reads the most recent one and flags the loop overdue in `50-dashboards/health.md` if it is older than 14 days. That 14-day window is deliberately monitoring-grade rather than 2x the daily run cadence, because a no-op run commits nothing; the tight daily signal is the run ledger, whose staleness threshold is 3 days. Keep the prefix exact.
- Push to `origin`. The git-guard hook does not block `obsidian-work` paths (it gates only `USADEBUSK\` paths), so the push proceeds without confirmation.
- If the working tree has unrelated uncommitted changes, commit only the loop's own touched paths (`00-inbox/`, `07-llms/`, `08-systems/`, `09-interests/`); do not sweep unrelated edits into the commit.

## Allowed Without Additional Approval

| Action | Limits |
|---|---|
| Read any vault note and any session transcript | Read-only. |
| Append to / create notes in `00-inbox/`, `07-llms/`, `08-systems/`, `09-interests/` | Content layer only. Must read cold; must cite source. |
| Add the no-home comment to an inbox file | Comment only; no content change. |
| Move a terminal-status note of any type from `00-inbox/` to `archive/` | Terminal-Note Sweep only; exact status allowlist; tracked-only; never renamed. |
| Update `00-inbox/.capture-state.json` | State tracking only; merge, never blank-overwrite. |
| Run `tools/vault_lint.py --worktree` before committing | Pre-commit gate; must be 0 errors. Read-only check. `--worktree` is required, not optional — it is what runs the diff rules. |
| Commit and push the loop's own touched paths | Durability close, per Durability. The commit message is the run record — no `change-log.md` entry (decisions-only since 2026-07-05). |

## Blocked Without Specific Approval

| Action | Reason |
|---|---|
| Delete any file | Data loss. |
| Move any file, **except** a terminal-status note under the Terminal-Note Sweep | Routing impact. The sweep is the single sanctioned move; everything else is proposed, not executed. |
| Write to `02-facilities/`, `04-knowledge/`, or any operational content | Owned by [[vault-agent-loop-spec]]. |
| Create or move a clustering hub note | Restructures the vault. |
| Commit paths outside the content layer | Keeps the loop's commits scoped and reviewable. |
| Promote any draft to canonical | Canonical fact promotion. |

## Stop Conditions

Stop and report when: a finding or inbox item is operational (leave in inbox, defer); source authority is unclear; a path is outside the canonical vault; the same failure class occurs twice; git working-tree state is ambiguous (conflicts, detached state); or a transcript's identity as the loop's own output cannot be determined.

## Success Criteria

A successful run leaves the content layer better with no manual effort: inbox items filed or tagged, durable findings harvested into the right notes, state recorded so the next run is cheap, and everything committed and pushed. Stopping with a well-documented blocker is also success. Broad silent changes, or harvesting the loop's own output, are failures.
