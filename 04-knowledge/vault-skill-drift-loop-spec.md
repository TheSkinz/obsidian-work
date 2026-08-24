---
type: governance
status: active
source_authority: primary
created: 2026-07-07
last_reviewed: 2026-07-29
review_after: 2026-10-29
related:
  - [[vault-capture-loop-spec]]
  - [[vault-idea-loop-spec]]
  - [[knowledge-system-governance]]
  - [[estimating-actuals-rollup]]
  - [[2026-07-25-skill-drift-review]]
tags: [knowledge-system, agent-loop, skill-drift, governance]
---

# Vault Skill-Drift Loop Spec

The fourth loop. [[vault-capture-loop-spec]] files and harvests into the vault; this loop closes the return path — it checks whether the deployed skills at `~/.claude/skills/` still agree with vault truth and with each other, and packages any drift as a ready-to-merge proposal. Skills are the only layer every session loads: knowledge that reaches a skill compounds automatically, knowledge stranded in a vault note compounds only when someone remembers to look.

Origin: the 2026-07-06 harness judgment audit found the fieldpm skill had drifted since March — contradicting three newer skills on pig-type definitions, L/C/R handling, and receipt scope — and it took a full multi-agent audit to notice. This loop is the standing, cheap version of that audit.

## Loop Name

Vault Skill-Drift Loop

## Trigger

**Scheduled monthly** — `0 3 1 * *`, day 1 of the month, task id `vault-skill-drift-loop`, `enabled: true`. Runbook prompt: `~/.claude/scheduled-tasks/vault-skill-drift-loop/SKILL.md`. It can still be started on demand by saying "run the Skill-Drift Loop" in a session. Because it is scheduled, it **is** heartbeat-tracked in `tools/vault_health.py` (ledger id `vault-skill-drift-loop`, commit prefix `skill-drift:`) — a silent scheduler here is a FAIL like any other loop.

**Why the 2026-07-19 "keep it manual" reasoning no longer holds (corrected 2026-07-25).** That paragraph argued the loop must stay on-demand because it writes outside the vault — branch, commit and push in the config repo — and because "git mutation authority is deliberately scoped to the vault," so an unattended run would stall on a permission prompt. **The premise was false.** `~/.claude/settings.json` sets `"defaultMode": "auto"` and its `allow` list contains only read verbs plus `git status/diff/log/branch/show/remote`; `git add`, `git commit` and `git push` appear in neither `allow` nor `deny`, so `auto` mode permits them unprompted. The `usadebusk-git-guard.mjs` PreToolUse hook only matches paths containing `USADEBUSK[\\/]`, which does not cover `C:\Users\Jwuts\.claude`. The gate the spec believed it was preserving never existed as a permission rule — which is exactly why the 2026-07-25 run fired unattended and pushed `drift/2026-07b` successfully instead of stalling.

The real containment is procedural, not permissional, and it is worth stating plainly: the loop never merges its own branch, never edits skills on `main`, and never edits vault content or memory. Those are properties of the runbook prompt, and they are the only thing standing between an automated run and Lane 4 domain truth. If that containment is ever judged insufficient, the fix is a `deny` rule on config-repo writes — not a belief that one is already in place.

## Scope

Reads: every `SKILL.md` and reference file under `~/.claude/skills/`; vault knowledge layers (`04-knowledge/`, `06-reviews/`, `07-llms/`, `08-systems/`); `04-knowledge/estimating-actuals-rollup.md`; the two CLAUDE.md files; git log of the config repo since the last run; **the agent memory directory** (`~/.claude/projects/C--Users-Jwuts-obsidian-work/memory/` — index + topic files), audited as a drift surface only, never edited by this loop; and **the regression suite** (`~/.claude/regression/` — `README.md`, `fixtures/`, and the `frontmatter` of every file in `frozen/`).

**On `~/.claude/regression/` (added 2026-07-25).** This surface demonstrably drifts, and it drifts silently in the one direction that matters: the regression suite is the instrument that detects skill degradation, so when it goes stale the detector is broken and nothing reports it. Two confirmed instances on 2026-07-25 alone — the `README.md` was wrong about the provenance of all six frozen fixtures, and F6's frozen output recommended equipment that no longer exists in `04-knowledge/equipment/equipment-library.md`. A frozen output encoding a retired rule does not fail loudly; it silently redefines a regression as the standard.

Audit rules for this surface, which differ from the skills surface:
- Check the `README.md`'s per-fixture claims (which model, which config commit, which skills) against each frozen file's own `model:` / `captured:` / `skills:` frontmatter. Frontmatter wins; the README is the restatement and is the thing that drifts.
- Check every fixture's and frozen output's domain references — equipment names, rate-table line labels, pig types, doc-type enums — against current vault truth, and flag any that no longer exist.
- **Never propose an edit to anything under `frozen/`.** Re-cutting a baseline is Jesse's call and requires a judged clean replay first (see the suite's own "When to re-cut frozen/"). A stale frozen output is reported as a finding with its evidence, never fixed by this loop. `README.md` prose and fixture-side staleness are ordinary proposals and may go on the branch.

Writes:

- One review note per run in `06-reviews/` (`YYYY-MM-DD-skill-drift-review.md`, `review_type: skill-drift`) — or a clean no-op report when nothing drifted.
- When findings exist: a proposal branch in the config repo (`~/.claude`), named `drift/YYYY-MM`, containing the proposed skill edits as commits, pushed to origin. **Never merged by the loop.** Jesse reviews the review note, then merges or discards the branch.

Never edits skills on `main`. Never touches vault operational content, pricing values, or SOP values directly — proposed changes to those live only on the unmerged branch and take effect only when Jesse merges.

## What counts as drift

1. A vault note (or the actuals rollup) contradicting a skill's stated fact, value, or path.
2. Two skills contradicting each other (the audit's fieldpm-vs-equipment class).
3. A skill referencing a file, folder, plugin, tool, or workflow that no longer exists.
4. A correction applied to one home of a fact while a pointer or restatement elsewhere still carries the old version.
5. An agent-memory file asserting state the vault, skills, or filesystem contradict (retired tools still listed as live, renamed files, "not yet done" claims with completion evidence in git). Memory findings are *flagged only* — the review note recommends a `/consolidate-memory` pass; this loop never edits memory files itself.
6. A regression-suite surface contradicting itself or current vault truth — `README.md` claims disagreeing with a frozen file's own frontmatter, or a fixture or frozen output referencing equipment, rates, labels or enum values that no longer exist. `frozen/` findings are *flagged only* (see Scope); README and fixture findings may be proposed on the branch.

## Ceremony Level

Low for detection, zero authority for application. Every proposed edit is a diff Jesse can read in one sitting; the review note quotes the exact current line and the exact proposed line with the evidence for why. Lane 4 content (pricing, safety, SOP values, domain truth) may appear in proposals — flagged as Lane 4 in the note — but only a merge by Jesse applies it.

## Loop Steps

**Run ledger (every run, first and last action):** Before anything else, update `50-dashboards/.loop-runs.json` in the vault (local, gitignored — create if missing): set this loop's entry (`vault-skill-drift-loop`) to `{"fired": "<now, UTC ISO-8601>", "completed": null, "result": "running"}`, merging without touching other loops' entries. As the run's very last action — after the final push, or immediately on deciding the run is a no-op or hitting a fatal problem — set `completed` to now and `result` to `committed`, `no-op`, or `error: <one line>`. Use Write/Edit tools, never shell editors. `tools/vault_health.py` reads this file to tell a dead scheduler from a quiet loop; a run that skips it surfaces as a monitoring FAIL.

1. `git -C ~/.claude fetch` and confirm a clean working tree on `main`; stop if ambiguous.
2. Read all skills; read vault layers changed since the last `skill-drift:` heartbeat (git log date-bounded); read the actuals rollup; read the regression suite's `README.md`, fixtures, and `frozen/` frontmatter.
3. Detect drift per the six classes above. Quote exact lines — no finding without a quote (audit discipline).
4. If nothing found: write nothing, commit nothing, report a clean no-op, stop.
5. Write the review note in `06-reviews/`: per finding — severity, file:line, current text, proposed text, evidence, lane classification. Decision checkboxes for Jesse. Apply Log empty.
6. Create branch `drift/YYYY-MM` from `main` in the config repo, apply the proposed edits, commit (one commit per skill touched, staged-file count checked), push the branch. Do not open a PR automatically and do not merge. If `drift/YYYY-MM` already exists (a second run in the same calendar month), suffix a letter — `drift/YYYY-MMb`, then `c` — and say so in the review note's Trigger section rather than reusing or force-updating the existing branch.
7. Run `py -3 tools/vault_lint.py` (0 errors required), then commit and push the vault review note: `skill-drift: <YYYY-MM> — N findings, branch drift/YYYY-MM` (or no commit on a no-op). The `skill-drift:` prefix is the heartbeat.

## Allowed Without Additional Approval

| Action | Limits |
|---|---|
| Read skills, vault, config-repo git log | Read-only. |
| One review note per run in `06-reviews/` | Standard template; every finding quoted. |
| Create + push a `drift/YYYY-MM` branch in the config repo | Proposals only; never merge; never touch `main`. |
| Commit/push the vault review note | `skill-drift:` prefix, staged-count discipline. |

## Blocked Without Specific Approval

| Action | Reason |
|---|---|
| Editing anything on the config repo's `main` | The whole point is propose-only. |
| Merging or deleting any branch | Merging is Jesse's act; branch deletion is hard-banned vault-wide. |
| Changing vault content beyond the review note | Other loops own the vault layers. |
| More than one drift branch **awaiting decision** | If last month's `drift/` branch is still undecided, fold new findings into a fresh review note but flag the stale branch instead of stacking a second one. An unmerged-but-*decided* branch does not count — see Branch States below. |

## Branch States — unmerged does not mean unactioned

Added 2026-07-29, correcting a defect that would have degraded the 2026-08-01 run. The original stop condition treated "a prior `drift/` branch is unmerged" as proof of a backlog. The 2026-07-25 run created a third state the spec did not model: Jesse read the review note, applied F1/F2/F5/F6 to `main` **by hand**, rejected F3, held F4, and then deliberately kept the branch — [[2026-07-25-skill-drift-review]] records the choice explicitly, striking through "Discard the branch" in favour of "branch retained, unmerged, as the record of what was proposed." Nothing is pending on `drift/2026-07b`, yet a literal reading of the old rule would have made the next run skip branch creation and report a backlog that does not exist.

Classify by the **review note's `status`**, never by the branch's merge state:

| Review note status | Meaning | Loop's action |
|---|---|---|
| `open` (or unchecked Decision boxes) | Genuinely awaiting Jesse | Real backlog. Report findings, flag it, **skip** branch creation. |
| Terminal — `decided-blocked`, `resolved`, `complete`, `superseded` | Decided; branch is a record | **Not** a backlog. Proceed normally and create this month's branch. |
| No review note found for an existing `drift/` branch | Unknown | Treat as a backlog and say the note is missing — the conservative read. |

A decided branch is never deleted (branch deletion is hard-banned vault-wide) and is never reused.

## Stop Conditions

Stop and report when: config-repo working tree is dirty or mid-operation; a prior `drift/` branch is **awaiting decision** per the Branch States table above (report findings, flag the backlog, skip branch creation); a finding requires domain knowledge the loop cannot verify from files (list it as an open question in the review note rather than proposing a guess).

## Success Criteria

A successful run either delivers a review note + branch that lets Jesse apply a month of skill corrections in one merge, or cleanly reports the skills are in sync. Proposing an edit without quoted evidence, touching `main`, or letting proposal branches accumulate unmerged without flagging are failures.
