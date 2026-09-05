---
type: review
status: open
review_type: architecture-audit
source_authority: observed
confidence: high
created: 2026-09-05
related:
  - "[[2026-09-05-harness-audit-number-verification]]"
  - "[[2026-09-04-harness-audit-evidence]]"
tags: [review, harness, audit, transcripts, skills, hooks]
---

# Harness route usage, re-measured at corrected scope

## What this is

The 2026-09-05 verification found that both prior harness audits were scoped to
`~/.claude/projects/C--Users-Jwuts-obsidian-work/*.jsonl`, which is **main-session transcripts only**.
Subagent transcripts sit one directory down and are fully persisted. This note re-measures, at corrected
scope, everything the 2026-09-04 audit's structural finding rests on.

**That finding does not survive.** Its claim — that the harness routes through an interface the work does
not use — was an artifact of the missing scope. Corrected, the `Skill` tool carries 199 calls, not 40.

Three blinded subagents produced the measurements; this session verified the load-bearing ones directly
and reproduced them exactly. Where a figure below disagrees with an agent's, mine is stated and the
disagreement is named.

---

## The corpus is three scopes, not one

| Scope | Definition | Files | Records | `tool_use` |
|---|---|---|---|---|
| **S1 main** | `projects/C--Users-Jwuts-obsidian-work/*.jsonl` | 187 | 75,974 | 15,233 |
| **S2 subagent** | `…/<sessionId>/subagents/agent-*.jsonl` | 117 | 4,801 | 1,372 |
| **S3 other projects** | all 20 other `projects/*/` dirs | 25 | 8,104 | ~1,000 |
| **Total** | | **329** | | |

`isSidechain` is `true` on every S2 record and `false` on every S1 record — the scopes are disjoint and
nothing double-counts. An S2 file's stem is an **agent id**, and its `sessionId` field carries the
**parent** session id, so deduping on `sessionId` silently merges distinct agent runs.

Two of the S3 directories have a vault `cwd` (`…-50-dashboards` and a `claude-worktrees` worktree). The
other 18 are USADebusk work under OneDrive facility folders plus `leverage` and scratch workspaces. S3
carries 26 `Skill` calls — more than half of S1's — so excluding it distorts the answer.

**Subagents are 8.2% of tool calls, but the mix is nothing like the main scope's:**

| Tool | S1 | S2 | S2 share |
|---|---|---|---|
| `Skill` | 40 | 133 | **76.9%** |
| `Read` | 1,730 | 326 | 15.7% |
| `Bash` | 7,578 | 762 | 9.1% |
| `Edit` | 3,051 | 1 | **0.03%** |

Delegated work here is read-and-report, not read-and-write. A main-glob-only analysis is 8% short on tool
volume generally and **inverted** on skill usage specifically.

---

## Route inventory, corrected

Verified directly this session, reproducing the agent's figures exactly:

| Route | S1 | S2 | S3 | Total |
|---|---|---|---|---|
| **`skill_listing` injected (initial)** | 187 | 117 | 25 | **329** |
| — incremental single-skill re-injection | 119 | 1 | 5 | 125 |
| **`Skill` tool call** | 40 | 133 | 26 | **199** |
| — of which `usadebusk-*` | 28 | 133 | 21 | **182** |
| `SKILL.md` direct read | 101 | 44 | 3 | 148 |
| Skill script executed | ~118 | 3 | 2 | **123** |
| Scheduled-task loop prompt | 88 | — | — | 88 |
| `Agent` prompt naming a skill | 87 | — | — | 87 |
| Slash-command expansion loading a skill | 1 | — | — | 1 |

```
python .../scratchpad/verify_routes_main.py
# S1_main 187 files / 40 Skill / 187 initial listings / 119 incremental
# S2_subagent 117 / 133 / 117 / 1
# S3_other 25 / 26 / 25 / 5   -> TOTAL 329 / 199 / 329 / 125
```

### The largest route was never counted by anyone

**Every transcript in every scope opens with a `skill_listing` attachment — 329 of 329, no exceptions**,
plus 125 incremental single-skill re-injections. It delivers skill *descriptions*, never bodies, and it is
what makes `disable-model-invocation` function: `adhd` appears in **0 of 329 listings across its entire
life** and has zero tool invocations. **The flag is not bypassed; it is load-bearing.** Any argument that
command-only skills are "stranded" has to contend with the fact that the gate works exactly as designed.

### Script runs were mentions, not executions

The audit reported the skills' scripts ran **291 times**. Measured directly at both scopes: **318 Bash
commands mention a script filename, and 123 actually execute one.** The rest are `sed`, `git`, `grep`,
`cp`, `head` and `for` loops touching the name.

| Script | Mentions | Executions |
|---|---|---|
| `render_job_report.py` | 129 | **55** |
| `backtest_workup.py` | 54 | 17 |
| `presend_gate.py` | 33 | 15 |
| `extract_workup.py` | 32 | 7 |
| `extract_ticket_breakdown.py` | 28 | 12 |
| `assert_structure.py` | 23 | 15 |
| `render_proposal.py` | 19 | 2 |

`render_job_report.py` at **123 runs** in §A is the mention count. It ran 55 times. The audit used that
figure to argue fieldpm's scripts reach their work while the skill stays unreachable — the direction of
that argument survives at 55, but the magnitude does not.

**Disagreement declared:** the route agent reported 130 total executions but only 5 for
`render_job_report.py`. Our totals agree closely; the per-script split does not. Mine is a segment-anchored
count (an interpreter token leading the segment containing the filename) and is stated above. **Treat the
total as solid and the per-script split as the softer number.**

---

## The structural finding, corrected

The audit's §Findings 1 lead evidence, restated against measurement:

| Audit claim | Measured, all scopes |
|---|---|
| "`Skill` tool called **40 times** in 185 sessions" | **199 calls**, 53 sessions, 2026-07-07 → 2026-09-05 |
| "No USADebusk skill loaded through it since **2026-08-22**" | **182 `usadebusk-*` calls**; last 2026-09-05. In S1 alone the last is **2026-09-04** |
| "Skills' scripts ran **291 times**" | **123 executions** (318 mentions) |
| "All four command-only skills at ≤2 lifetime invocations" | Holds — but because the listing gate works, not because a route was bypassed |

From S1 alone the picture is 40 calls against 101 reads and "291" runs, which reads as abandonment. At
full scope it is 199 calls against 148 reads and 123 executions.

**The routes are specialised by scope, not competing.** Script execution is ~96% main-scope. Skill-tool
invocation is 77% subagent. `Agent` prompts and loop prompts are 100% main-scope. The main session
dispatches and executes; the subagent it spawns is where the `Skill` tool actually gets used, **because
the parent's prompt told it to** — 87 of 117 `Agent` prompts name a skill.

The read channel splits the same way and it matters: main-scope `SKILL.md` reads are majority
**maintenance** (61 of 102 sessions also `Edit`/`Write` that skill), while subagent reads are **44 of 44
use, with zero edits**. "Direct file reads replace the Skill tool" conflated two different activities that
the scope split separates cleanly. That split is `inferred` — the Edit/Write proxy cannot distinguish a
read-only audit from a session following the skill.

---

## Hook coverage in subagents

**The hooks do fire on subagent Bash calls.** `usadebusk-exec-guard` blocked 7 times in S2 across 7 agent
runs in 5 parent sessions, 2026-08-15 → 2026-09-04. Block rate per Bash call is statistically flat across
scopes — S1 85/7,578 = 1.12%, S2 7/758 = 0.92%, S3 6/753 = 0.80% — which is what a user-scope
`PreToolUse` wiring predicts. `settings.json` at user scope is the only file wiring them.

| Hook | S1 | S2 | S3 | Total | Sessions |
|---|---|---|---|---|---|
| `usadebusk-exec-guard` | 85 | 7 | 6 | **98** | 68 |
| `usadebusk-staged-count-guard` | 12 | 0 | 0 | **12** | 12 |
| `usadebusk-git-guard` (retired) | 6 | 0 | 0 | **6** | 6 |
| `usadebusk-word-delta-guard` (warn) | 17 | 0 | 0 | **17** | 10 |
| `usadebusk-fixture-replay-guard` (warn) | 1 | 0 | 0 | **1** | 1 |

The `exec-guard` figure verified in this note's predecessor at 85 for S1 is a **floor of 15%** — 98 across
all scopes, and S3 adds 5 genuinely new sessions for 68.

**The commit gates' zeros are opportunity zeros, not coverage holes.** Across 758 subagent Bash calls
there is **not one `git commit`** anywhere in the corpus. `staged-count`, `word-delta` and
`fixture-replay` all exit early on non-commits, so they were never asked to judge delegated work. This
distinction matters: nobody should conclude from the zeros that the gates fail to cover subagents.

**`staged-count-guard` is 12 blocks, not 13.** The audit formally self-corrected from 12 to **13**. Four
independent measurements now return **12** — this session's own script, two hook agents, and all three
scopes. The audit's own §B row is internally inconsistent, claiming 13 while listing "the 12 with a
recorded count". The correction appears to have overshot by one. This changes no verdict — the threshold
was raised on a sweep of real commit history, not on this classifier — but the number is wrong where it
is written.

---

## Startup compliance barely moves, and the loop gap is structural

| Population | Channel | all five | at least one |
|---|---|---|---|
| Attended (100) | main, tool+Bash | 11 (11%) | 36 (36%) |
| Attended (100) | **main + subagent** | **12 (12%)** | **41 (41%)** |
| Loop (88) | main, tool+Bash | **0** | 2 (2.3%) |
| Loop (88) | main + subagent | **0** | 3 (3.4%) |

Counting subagent reads as parent compliance moves all-five by **one session**. The agent's ruling —
which I accept — is that a subagent's read is *not* the parent complying: what reaches the parent is a
summary the subagent chose to write, not the file. `output-preferences.md` governs how the parent writes
prose, and a subagent reading it transmits none of that. Both numbers are given so a reader who disagrees
can substitute.

The Bash channel remains the thing a tool-only scan misses: 8 of the 36 attended sessions with any read
are Bash-only, understating at-least-one by 22% and all-five by 27%.

**Loop sessions are 0 of 88 on all-five across every channel combination and every scope.** That is not
drift, it is a clean structural split — 88 scheduled runs, 47% of all sessions, executing against vault
content without loading the files `CLAUDE.md` says to load first.

---

## Defects found beyond the re-measurement

**`usadebusk-fieldpm`'s `disable-model-invocation` flag was inert for ten days.** The skill carried the
flag yet appears in **104 of 104 skill listings from 2026-07-19 to 07-28**, and made 7 *successful* Skill
calls inside exactly that window, the last 34 minutes before it closed. The route agent found this from
listing attachments, then independently met config commit `ab409004` (2026-07-28) attributing it to
unparseable frontmatter — an unquoted description containing `": "` that silently dropped the flag, the
`status:` field and the whole 782-character description, leaving the skill registered by its H1 title.
The agent correctly flagged that agreement as **one source, not two**, since both describe the same
registry behaviour. Worth noting because a skill's declared frontmatter is not its reachability, and the
`skill_listing` attachment is the only channel that states reachability as fact.

**`totalToolUseCount` has a 60% coverage hole and no warning.** Only **47 of 117** `Agent` results carry
the field. Where present it is exact — those 47 sum to 513 and the matching transcripts contain exactly
513 tool calls, per-agent delta zero. But summing the field from the main glob accounts for 513 of 1,372
real subagent tool calls, **under-counting by 62.6% with no signal that anything is missing**. All 5
`spawnDepth: 2` agents lack it, which explains 5 of the 70; the mechanism for the other 65 is not
established. `toolStats` must not be summed naively — it mixes line counts with tool counts.

**Delegated work is context-rich, not context-starved.** Subagents draw 63% of their vault reads from
`04-knowledge` and `02-facilities` — the domain-truth layers — against 25% for the main scope, and read
`01-context` at more than double the main rate. The main scope's most-read paths are machinery
(`.loop-runs.json`, `change-log.md`, `health.md`), which is the 88 loop sessions doing bookkeeping.

---

## What this does and does not support

**Supported.** The `Skill` tool is not bypassed. The audit's structural finding is refuted on its lead
evidence, and the refutation is a scope error rather than a reasoning error — everything the audit said
was true of the corpus it could see.

**Supported.** `disable-model-invocation` works. The listing channel enforces it in 329 of 329 sessions,
and `adhd` never once appeared.

**Supported.** Every count here is a **floor** over channels that leave a transcript record. Skill content
reaching a session through the system prompt at build time, through a `--print`/SDK session writing no
local transcript, or through a project directory outside `~/.claude/projects` is invisible to all of it.

**Not supported: any claim about intent.** The maintaining-versus-following split is a proxy over
Edit/Write co-occurrence, labelled `inferred` throughout, and this corpus is thick with sessions whose
subject matter *is* skills.

**Not supported: that all 123 executions executed.** The detector reads the proposed command; four
`PreToolUse` hooks run on Bash and two of them block. Denials are a real subtraction nobody measured.

**Not settleable by re-running these commands.** For the headline — that S2 carries the Skill tool's real
volume — the settling artifact is the harness's own invocation telemetry, because S2 transcripts omit the
`toolUseResult.commandName` field that S1 records, proving the local writer's coverage is
version-dependent and therefore not self-validating.

---

## Log

| Date | Action | By |
|---|---|---|
| 2026-09-05 | Harness route usage re-measured at corrected scope (S1 main + S2 subagent + S3 other projects) after the verification note found both prior audits scoped to `*.jsonl` alone. Three blinded agents; load-bearing figures verified directly by this session and reproduced exactly. **The 2026-09-04 audit's structural finding is refuted on its lead evidence** — the `Skill` tool carries **199 calls across 53 sessions**, not 40, with 133 in the subagent scope and a last `usadebusk-*` load of 2026-09-05. **Script runs were mentions:** 318 mentions against **123 executions**, so §A's "`render_job_report.py` 123 runs" is a mention count and the real figure is 55. **A route nobody counted:** the `skill_listing` attachment injects skill descriptions into **329 of 329 transcripts**, and it is what makes `disable-model-invocation` work — `adhd` appears in 0 of 329 across its whole life. **Hooks do fire in subagents** (7 `exec-guard` blocks, block rate flat across scopes at 1.12/0.92/0.80%); the commit gates' zeros are opportunity zeros, there being no `git commit` in 758 subagent Bash calls. **`staged-count-guard` measures 12 blocks, not the 13 the audit self-corrected to** — four independent counts, and the audit's own row lists only 12. Startup compliance moves 11→12 of 100 attended when subagent reads are counted; loop sessions stay 0 of 88 on every channel and scope. Read-only, no Verdict cell filled, no fix executed. | Claude |
