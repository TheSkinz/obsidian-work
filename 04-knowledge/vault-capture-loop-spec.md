---
type: governance
status: active
source_authority: primary
confidence: high
created: 2026-06-30
last_reviewed: 2026-06-30
review_after: 2026-07-30
related:
  - [[vault-agent-loop-spec]]
  - [[vault-idea-loop-spec]]
  - [[knowledge-system-governance]]
  - [[vault-source-of-truth]]
tags: [knowledge-system, agent-loop, capture, governance]
---

# Vault Capture Loop Spec

The scheduled, low-effort half of the vault automation. Its job: quietly file what you drop in `00-inbox/` and harvest durable findings from recent sessions, so knowledge lands in the right place without you doing it by hand. Companion to [[vault-agent-loop-spec]], which handles the high-stakes operational core on-demand.

The design intent, stated plainly: **drop `.md` files into `00-inbox/` whenever you want, and a periodic run ingests them automatically.** You should never feel audited by this loop — it files and harvests, it does not police.

## Loop Name

Vault Capture Loop

## Trigger

A local **desktop scheduled task** (weekly is plenty). It runs against the local working tree and harvests Claude Code session transcripts (plain JSONL under `~/.claude/projects/`, which are not in git), so it cannot run in the cloud. If the machine is asleep or the app closed at trigger time, it runs on next launch. There is no in-session cron variant — the scheduled task is the single mechanism.

## Scope

Governs the **content layer** only:

- `00-inbox/` — content routing and triage (the primary job)
- `07-llms/`, `08-systems/`, `09-interests/` — destination content layers

Never touches `02-facilities/`, `04-knowledge/`, pricing, SOP, safety, field-execution, customer-facing content, or heater-card facts. Those belong to [[vault-agent-loop-spec]]. If a harvested finding or an inbox item is operational, this loop leaves it in `00-inbox/` with a one-line routing note and stops — it does not write the operational core.

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
5. Run `python tools/vault_lint.py` (use `py -3` if `python` is not on PATH); it must report **0 errors** before committing. Fix any error the run introduced — warnings are acceptable. Do **not** append a run summary to `change-log.md`: per the 2026-07-05 narrowing rule, `change-log.md` is decisions-only and the run record lives in the commit message (the `vault-capture:` heartbeat) and git log.
6. **Refresh generated files** — run `py -3 tools/vault_index.py` and `py -3 tools/vault_health.py` so `INDEX.md` and `50-dashboards/health.md` reflect this run's ingested/harvested notes; include both in the commit. (Generated files are the sanctioned overwrite exception; added 2026-07-07.)
7. **Commit and push** (see Durability).

## Transcript Scope

Scan all `~/.claude/projects/` directories, incremental by file mtime since `last_run`. The vault owns the LLM/systems/interests layers, and findings on those occur across projects, so breadth is intentional.

**Self-exclusion (mandatory).** Skip the loop's own run:

- Exclude the active session's transcript and any subagent transcripts it spawned (the run's own session id, and anything under `…/<session-id>/subagents/`).
- Exclude any transcript whose mtime falls inside the current run window — it is being written as the loop executes and is not a settled source.

This rule is what prevents the loop harvesting its own reasoning. It must be applied before the Save-vs-Skip filter.

**Relevance.** Breadth is intentional, but a transcript whose project cwd is clearly unrelated to the vault (e.g. a `system32` shell session) may be dispositioned `skip` without deep reading. mtime + Save-vs-Skip + this light relevance check are the only filters.

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

- Commit message: `vault-capture: <YYYY-MM-DD> run — N ingested, M harvested`. **This `vault-capture:` subject prefix is the loop's heartbeat** — `tools/vault_health.py` reads the most recent one and flags the loop overdue in `50-dashboards/health.md` if it is older than 14 days (2x the weekly cadence). Keep the prefix exact.
- Push to `origin`. The git-guard hook does not block `obsidian-work` paths (it gates only `USADEBUSK\` paths), so the push proceeds without confirmation.
- If the working tree has unrelated uncommitted changes, commit only the loop's own touched paths (`00-inbox/`, `07-llms/`, `08-systems/`, `09-interests/`); do not sweep unrelated edits into the commit.

## Allowed Without Additional Approval

| Action | Limits |
|---|---|
| Read any vault note and any session transcript | Read-only. |
| Append to / create notes in `00-inbox/`, `07-llms/`, `08-systems/`, `09-interests/` | Content layer only. Must read cold; must cite source. |
| Add the no-home comment to an inbox file | Comment only; no content change. |
| Update `00-inbox/.capture-state.json` | State tracking only; merge, never blank-overwrite. |
| Run `tools/vault_lint.py` before committing | Pre-commit gate; must be 0 errors. Read-only check. |
| Commit and push the loop's own touched paths | Durability close, per Durability. The commit message is the run record — no `change-log.md` entry (decisions-only since 2026-07-05). |

## Blocked Without Specific Approval

| Action | Reason |
|---|---|
| Delete or move any file | Data loss / routing impact. |
| Write to `02-facilities/`, `04-knowledge/`, or any operational content | Owned by [[vault-agent-loop-spec]]. |
| Create or move a clustering hub note | Restructures the vault. |
| Commit paths outside the content layer | Keeps the loop's commits scoped and reviewable. |
| Promote any draft to canonical | Canonical fact promotion. |

## Stop Conditions

Stop and report when: a finding or inbox item is operational (leave in inbox, defer); source authority is unclear; a path is outside the canonical vault; the same failure class occurs twice; git working-tree state is ambiguous (conflicts, detached state); or a transcript's identity as the loop's own output cannot be determined.

## Success Criteria

A successful run leaves the content layer better with no manual effort: inbox items filed or tagged, durable findings harvested into the right notes, state recorded so the next run is cheap, and everything committed and pushed. Stopping with a well-documented blocker is also success. Broad silent changes, or harvesting the loop's own output, are failures.
