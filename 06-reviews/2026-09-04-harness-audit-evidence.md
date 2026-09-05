---
type: review
status: open
review_type: architecture-audit
source_authority: observed
confidence: high
created: 2026-09-04
related:
  - "[[2026-08-20-vault-architecture-audit-evidence]]"
  - "[[knowledge-system-governance]]"
tags: [review, harness, config-repo, hooks, skills, audit]
---

# Harness audit — evidence pass

## What this is

The 2026-08-20 vault architecture audit measured 54 vault components by effect and named three things it
deliberately left out: the skills in the config repo, the hook scripts, and whether the loops' scheduling
matches their declared cadences. The vault has been audited by effect; **the harness never had.** This is
that audit, run 2026-09-04 against the same method — *audit by effect, not by inspection.*

**How to use it.** Overwrite the `Verdict` column. That is the whole interaction — one sitting, one
artifact. Nothing here is a decision, nothing has been retired, no fix has been executed, and no file
outside this note was touched.

**Conflict of interest, stated.** Your assistant built almost every component graded below. Where the
evidence was ambiguous the component was failed, not passed. Four of the brief's own premises turned out
to be wrong and are corrected in the next section rather than carried.

### Reading the channel labels

Every number carries how it was obtained. `measured (tool channel, floor)` is the important one: a file
read through `cat` or `sed` inside a Bash command carries no `file_path` and is invisible to the tool-call
scan. The prior audit measured that undercount at **20–25%** on `01-context/`. Every attended read count
below is therefore a floor, not a total.

| Label | Means |
|---|---|
| `measured (tool channel, floor)` | Counted from `tool_use` blocks in 185 transcripts; undercounts by ~20–25% |
| `measured (transcript, exact)` | Counted from a structural marker that cannot be typed by hand — hook `tool_result` errors, `attachment` + `additionalContext` injections |
| `measured (git)` | `git log` in the vault or `~/.claude` |
| `measured (scheduler)` | The live scheduled-task registry, not the vault ledger |
| `measured (fs)` | Filesystem, this machine, 2026-09-04 |
| `carried-in` | From the 2026-09-04 research session; not re-derived here, no command recorded |
| `not measurable` | Attempted and abandoned; the reason is stated |

Corpus: **185 session transcripts** (88 loop, 97 attended), `~/.claude` git (264 commits), vault git.
Commands for every number are in the appendix.

---

## Brief premises corrected

The audit brief asserted four things as settled. None survived measurement. They are corrected here
because the brief mandated adversarial grading, and three of the four would have steered a verdict wrong.

| Brief said | Measured | Why it was wrong |
|---|---|---|
| `fixture-replay-guard` "had been firing and being walked past since 2026-08-15" | **0 genuine firings, ever** — 185 transcripts, 29 qualifying commits | The cited source derived this from reading the hook's logic, not from observing a firing. It is an inference wearing a measurement's clothes — the exact failure mode this audit was told to look for |
| "Stale `__pycache__/*.pyc` is **checked into**" two skills | **Not tracked.** `git ls-files \| grep -c __pycache__` = 0. Not stale either — `render_job_report.cpython-312.pyc` is dated today | Present on disk, absent from git. Two errors in one line |
| `usadebusk-fieldpm` is `status: dormant`; "measure whether it wakes" | **Never slept.** `render_job_report.py` ran **123 times**, last today; SKILL.md read in 17 sessions through 2026-09-04 | It is the single most-executed component in the harness. The frontmatter is stale, not the skill |
| "4 of 6 frozen baselines are `behind`" | **5 of 6.** Only F2 is current | `regression/README.md` says F1/F4/F6 current as of 2026-09-03; the checker disagreed one day later |

---

## Findings

### 1. Every gate and every route is built on an interface the work does not use

This is the audit's structural finding, and every table below is an instance of it. The harness routes
through the **Skill tool**, **slash commands**, and **`git commit` in the repo the session sits in**. The
work routes through **direct file reads**, **script execution**, and **cross-repo commits issued from a
vault working directory**. Mechanisms built on the first set gate a road nobody drives on.

- The `Skill` tool was called **40 times in 185 sessions**, and **no USADebusk skill has been loaded
  through it since 2026-08-22**. Over the same period those skills were read directly as files through
  2026-09-04 and their scripts executed 291 times.
- All four command-only skills sit at **≤2 lifetime invocations**.
- `fixture-replay-guard` has **never fired**, because it resolves which repo it is judging from the
  session's working directory rather than from the repo the commit targets.
- `git-guard` fired 6 times with **zero true positives**, because the directory it protects does not
  exist and its pattern matches ordinary prose.

### 2. A prose instruction has a compliance rate; a gate with a hatch has a hatch rate

The prior audit's headline was that the startup protocol is not executed — 43% of attended sessions.
Mechanizing an instruction into a hook was the obvious answer, and two of the hooks are exactly that.
Measured, the mechanized versions did not do better; they moved the failure from *ignored* to *waved
through*, which is harder to see.

| Mechanism | Kind | Fires | Walked past | Outcome actually changed |
|---|---|---|---|---|
| `01-context` startup protocol | Prose instruction | n/a | — | **7% of attended sessions read all five files**; 0 of 88 loop runs |
| `staged-count-guard` | Hook with hatch | 12 blocks | 12 × `staged-ok` — **100%** | **Zero commits prevented, ever** |
| `exec-guard` | Hook with hatch | 85 blocks | **416** commands carried `exec-ok`, ~372 pre-emptively | 44 paid the hatch and ran anyway; 38 switched tool |
| `word-delta-guard` | Hook, warn-only | 17 firings / 10 sessions | 11 × `word-delta-ok` / 5 sessions | The one gate that lands |

The tell is the ratio. `word-delta-guard` warns more often than it is hatched and is the only mechanism
here with an honest claim to changing outcomes. `staged-count-guard` has a hatch rate of 100% — it has
never once stopped a commit, only added a round trip to twelve of them.

### 3. A declared, enabled loop that has never run

The prior audit's third un-audited item was whether loop scheduling matches the declared cadence. It does
not, in one case completely. `vault-review-loop` is enabled, holds a valid monthly cron, and has **no
`lastRunAt` and zero sessions across all 22 project directories**. It has never executed.

The wider shape: **83 of 88 loop runs came from the three loops retired on 2026-08-21.** The three
survivors have produced five sessions in seven weeks, and one of those three has produced none.

---

## A. Skills — 10 directories in `~/.claude/skills/`

| Component | Evidence | Effect | Verdict |
|---|---|---|---|
| `usadebusk-estimating` | 71,259 B / 511 lines. 33 sessions loaded it (24 read + 9 Skill), last Skill-load 2026-08-22. Scripts ran 135× — `backtest_workup.py` 54, `presend_gate.py` 33, `extract_workup.py` 31, `render_proposal.py` 17. *measured (tool channel, floor)* | Largest SKILL.md; Duration Model is 139 of 511 lines. Its **scripts** are in continuous use through today while the prose is loaded through the Skill tool no longer | |
| — its load-bearing fraction | A per-section demand probe was built and **discarded**: the tokens unique to each section are ordinary English and matched 185/185 sessions. *not measurable* | The brief's question ("measure what fraction is ever load-bearing") cannot be answered from transcripts. Reporting a number here would have been fabrication | |
| `usadebusk-fieldpm` | `status: dormant`. 19,743 B SKILL.md, ~330 KB directory. `render_job_report.py` **123 runs**, `extract_ticket_breakdown.py` 27, both last today. Read in 17 sessions through 2026-09-04. *measured (tool channel, floor)* | The most-executed component in the harness, marked dormant. Frontmatter contradicts behaviour | |
| `usadebusk-vault-ingest` | 33,706 B / 602 lines — 2nd largest. `disable-model-invocation: true`. `/ingest` invoked **2×, both 2026-07-26**. Read in 9 sessions. F2's regression fixture. *measured (tool channel, floor)* | 40 days since last invocation. Size is 2nd-largest against the 2nd-lowest human demand | |
| `usadebusk-core` | 23,924 B. Skill-loaded 14 sessions (last 2026-08-22), read 10 (last 2026-09-04). CLAUDE.md mandates it "for any USADebusk task". *measured (tool channel, floor)* | Present in ~24 of 185 sessions against an every-task instruction. Same compliance shape as `01-context` | |
| `usadebusk-sop` | 22,021 B. 7 read + 1 Skill, last 2026-09-04 | Steady low use | |
| `adversarial-review` | 23,487 B. Read in 4 sessions, last 2026-08-17. Never Skill-invoked | 18 days idle; not a USADebusk skill | |
| `usadebusk-equipment` | 12,986 B. 8 read + 2 Skill, last 2026-09-04 | Steady low use | |
| `adhd` | 8,674 B, command-only. `/adhd` invoked **once**, 2026-08-17. *measured (transcript, exact)* | One lifetime invocation | |
| `usadebusk-ops` | 6,193 B, smallest USADebusk skill. 3 read + 1 Skill, last 2026-08-16 | Smallest and least used | |
| `idea-triage` | 4,500 B, command-only. `/idea-triage` invoked **once**, 2026-08-17. Read in 8 sessions | Its consumer loops (capture, prestaging) were retired 2026-08-21 | |
| `__pycache__` | 8 `.pyc` files on disk in `usadebusk-estimating/scripts/` and `usadebusk-fieldpm/{scripts,back-test}/`. **0 tracked in git.** Newest dated today. *measured (git + fs)* | Live build artifacts of scripts in daily use. Not a repo problem | |

**Command-only skills, all four:** `adhd` 1, `idea-triage` 1, `/ingest` 2, `/report` 1, `/extract` 1.
None is stranded in the sense the brief feared — they are reachable — but none is *used*. The gating
decision (`disable-model-invocation: true`) removed them from the one channel that had traffic and put
them on one that has almost none.

## B. Hooks — `~/.claude/hooks/`, 5 wired

All five are `PreToolUse`/`Bash` and all fail open. Three block (exit 2), two warn (exit 0 with
`additionalContext`).

| Hook | Fired | Hatched | Outcome | Verdict |
|---|---|---|---|---|
| `usadebusk-exec-guard` | **85 blocks** / 63 sessions, last 2026-09-04. *measured (transcript, exact)* | **416** commands carried `exec-ok` in 41 sessions — only ~44 after a block, so **~372 (89%) were pre-emptive** | 44 paid the hatch and ran; 38 switched to a shell tool; 3 reworded. **Zero of the 501 events involved a human decision** — the agent that wanted to run the command also granted the exemption | |
| `usadebusk-staged-count-guard` | **12 blocks** / 12 sessions, last 2026-09-03. Threshold 12; observed staged counts 14, 14, 19, 21, 24, 25, 26, 27, 29, 46, 76, 103 | **12 of 12 hatched (100%)** | **No commit has ever been prevented.** The threshold sits below the median real commit (25), so it fires on normal work and is waved through every time | |
| `usadebusk-git-guard` | **6 blocks**, last 2026-08-16, **0 true positives**. *measured (transcript, exact)* | No hatch exists | `C:\USADEBUSK\` **does not exist on this machine**. The pattern `/USADEBUSK[\\/]/i` matched: `OneDrive/USADeBusk/Facilities` as an *input path* to a document conversion (2×), the phrase `USADeBusk\Facilities` inside a **commit message** (2×), a Python heredoc writing `change-log.md` (1×), and its own test harness (1×). One block caused a commit message to be **degraded** — the canonical store name was deleted to get past the guard | |
| `usadebusk-word-delta-guard` | **17 firings** / 10 sessions, last 2026-08-25. *measured (transcript, exact)* | 11 × `word-delta-ok` in 5 sessions | The only hook whose firings outnumber its escapes. Scoped to `obsidian-work`, which is the session cwd, so its scope test resolves correctly | |
| `usadebusk-fixture-replay-guard` | **0 firings, ever.** 29 config-repo commits touched a mapped `skills/*/SKILL.md` since 2026-08-15 | 4 × `replay-ok`, all in 1 session | **Structurally unable to fire.** See below | |

### Why `fixture-replay-guard` cannot fire

The hook computes which repository it is judging by running `git rev-parse --show-toplevel` against
`input.cwd`, then requires that toplevel to end in `.claude`. A `PreToolUse` hook runs **before** the
command, so `input.cwd` is the working directory as it stands *before* any `cd` inside that command.

**74 of 84** config-repo commits since 2026-08-15 take the form `cd "C:/Users/Jwuts/.claude" && git
commit …` issued from a vault working directory. For every one of them the hook resolves the toplevel as
`obsidian-work`, fails its own scope test, and exits 0 in silence.

The same defect has a quieter consequence for `staged-count-guard`, which accepts either repo: committing
the config repo from a vault cwd makes it count **the vault's** staged files. All 12 observed blocks
happened to be genuine vault commits, so it has not yet produced a wrong answer — but the mechanism for
one is present.

`word-delta-guard` escapes only by coincidence: its scope is `obsidian-work`, which is where sessions
already sit.

## C. The event surface that is empty

There are **zero** `SessionStart`, `SessionEnd`, `Stop`, `PostToolUse` and `UserPromptSubmit` hooks. Every
guard is `PreToolUse`/`Bash`. *measured (fs — `settings.json`)*

| Instruction | Is it an instruction, or a computation? | Compliance | Verdict |
|---|---|---|---|
| Vault CLAUDE.md: "Read `01-context/` before responding" | **Computation.** Reading five fixed files needs no judgment | **7% of attended sessions read all five**; 28% read ≥1; **0 of 88 loop runs read all five**, 1 read any. *measured (tool channel, floor)* — the prior audit's both-channel figure was 43% / 1-of-85 | |
| Vault CLAUDE.md: "Check `health.md` and surface any red rows" | **Computation.** Fixed file, fixed test | 37% of attended sessions, 6% of loop runs read it. `health.md` is nonetheless the single most-read file in the vault (44 reads) | |
| Global CLAUDE.md: "Load `usadebusk-core` for any USADebusk task" | **Computation** in its trigger, judgment in which domain skill follows | `usadebusk-core` present in ~24 of 185 sessions; not Skill-loaded since 2026-08-22 | |
| Vault CLAUDE.md: session close-out routine | **Judgment** — what counts as a durable finding is not computable | Fires in 60% of attended sessions since 2026-08-21 (12 of 20). *measured (transcript, floor)* | |
| Global CLAUDE.md: "check the staged file count before committing" | **Computation** — already mechanized into `staged-count-guard` | Hook hatched 100% of the time; the prose survives alongside it | |

**Recommendation — `SessionStart`. Mechanism now verified on this machine.** Per
`code.claude.com/docs/en/hooks` (read 2026-09-04), a `SessionStart` hook's plain-text stdout is injected
into the session as context. That would convert the three computations above from instructions with a 7%
compliance rate into content that is simply present.

> **Smoke test — approved by Jesse and executed 2026-09-04. PASSED.** A temporary `SessionStart` hook was
> added to `settings.json` emitting one line carrying an unguessable token. A fresh session was started
> with `claude -p` and asked to echo any line beginning with `SMOKE-CHECK`. **It returned the line and the
> token verbatim.** The token appeared nowhere in the prompt, so it can only have arrived through hook
> injection. The hook and its script were then removed and `git status` in `~/.claude` confirmed clean —
> `settings.json` is byte-identical to its pre-test state and still carries exactly its five `PreToolUse`
> hooks and no others. *measured (live test, 2026-09-04)*

The mechanism is real. What to put in the hook is a separate decision and is **not** made here — the
payload for a startup hook is a design question, and the Verdict column is where it belongs.

## D. Always-resident context weight

| Block | Bytes | Demand (attended reads) | Verdict |
|---|---|---|---|
| `~/.claude/CLAUDE.md` | 5,651 | Always resident | |
| Vault `CLAUDE.md` | 6,064 | Always resident | |
| `01-context/estimating-approach.md` | 8,013 | 16 | |
| `01-context/active-jobs.md` | 6,172 | 18 | |
| `01-context/output-preferences.md` | 4,244 | 9 | |
| `01-context/company-context.md` | 3,354 | 14 | |
| `01-context/equipment-fleet.md` | 2,531 | 11 | |
| **Mandated floor** | **36,029 B ≈ 9K tokens** | before any skill loads | |
| *(load-on-demand)* `system-workflow-reference.md` | 10,574 | 3 | |
| *(load-on-demand)* `workflow-map.md` | 2,450 | 2 | |

*measured (fs) for bytes, measured (tool channel, floor) for demand.* The floor matches the brief's
estimate. The two files CLAUDE.md already exempts from per-response loading are also the two least read —
that exemption is working.

## E. Settings and permissions

| Component | Evidence | Effect | Verdict |
|---|---|---|---|
| `settings.json` `"model": "opus[1m]"` | The only model pin anywhere. No `env`, no `statusLine`, no `agents` | Pins the model but not the effort level, which is the first lever | |
| `autoMode` block | ~33 lines of prose policy inside `settings.json`, restating the data posture, repo visibility and git hard-bans already in global CLAUDE.md | Two copies of one policy. Neither is generated from the other, so drift is unpoliced — the same shape the vault audit found in content notes | |
| **`obsidian-work/.claude/settings.local.json`** | **107 allow rules, 7,234 B — 77% of every allow rule on the machine.** *measured (fs, added 2026-09-04 after the smoke test surfaced it)* | **The audit's first pass counted three allowlist files and missed this one, the largest.** It was found only because starting a fresh session printed its warnings. Contains `Bash(python -c ' *)` — the exact rule `exec-guard` was built to defeat, still live, which corroborates that hook's stated rationale | |
| — its 6 `Write(...)` rules | The harness itself warns at startup: `Write(path) is not matched by file permission checks — only Edit(path) rules are` | **Six dead rules**, one per vault folder. Harmless: every one is paired with an `Edit(...)` rule for the same path, and Edit rules cover all file-editing tools. Six lines of noise and six startup warnings, no lost permission | |
| `~/.claude/settings.local.json` | 13 entries. Contains bare **`Bash(git push *)`** and `Bash(git commit -q -m ' *)`, plus frozen one-shots like `Bash(sed 's/.*obsidian-work.//')` | A wildcard push allow beside 5 specific one-shots | |
| `~/.claude/.claude/settings.local.json` (nested) | 19 entries, all frozen one-shots. Contains **`Bash(git add *)`, `Bash(git commit -m ' *)`, `Bash(git push *)`**. Three entries target `C:\Users\Jwuts\claude-config` | That path is the stale clone location global CLAUDE.md corrects; `~/.claude` is the live runtime directory. Only applies when cwd is `~/.claude`. Easy to edit the wrong file over | |
| `obsidian-work/.claude/settings.json` | 674 B, project-level, tracked in the vault repo | The only one of the five that is version-controlled | |

**Five settings files, not three.** `~/.claude/settings.json`, `~/.claude/settings.local.json`,
`~/.claude/.claude/settings.local.json`, `obsidian-work/.claude/settings.json`,
`obsidian-work/.claude/settings.local.json`. The brief said three and this audit's first pass repeated it;
both were counting only the config-repo side. Correcting it moves the allow-rule centre of gravity from
32 rules to 139, and puts 107 of them in a file neither document had looked at.
| `output-styles/jesse-default.md` | Exists (902 B), `outputStyle` is `"Concise"`. *measured (fs)* | Never selected. Its content — "name what is outstanding, then the suggested action" — is the one output rule that matters, and it is inert here; it survives only because global CLAUDE.md states it too | |

## F. Regression battery — `~/.claude/regression/`, 1.48 MB

| Component | Evidence | Effect | Verdict |
|---|---|---|---|
| Replay cadence | 53 runs on **5 distinct days**: 2026-07-24 (6), 07-25 (16), 07-28 (17), 08-15 (3), 09-03 (10). Gaps of 18 and 19 days. *measured (fs)* | Bursty, not continuous. Two of the five days account for 62% of all runs | |
| Baseline currency | **5 of 6 behind** — F1 (1 commit), F3 (2), F4 (2), F5 (8), F6 (1); only F2 current. *measured (`baseline_staleness.py`, run 2026-09-04)* | `regression/README.md` states F1/F4/F6 current as of 2026-09-03. One day later the checker disagrees on two of them | |
| Model coverage | All 53 runs under `runs/claude-opus-5/`. All 6 frozen baselines are Opus 5 | Single-tier. A second tier is available on the plan and unexercised, so model-delta is unmeasurable by construction | |
| What a replay has caught | README records: F5 carried a stale `5.297"` card field and a stale rounding line for 3 days; a re-cut caught a frozen baseline **over-billing a second truck by $720**; the 2026-08-01 sweep found all five swept fixtures behind, including F4 which "looked like the weakest case". *measured (git + README)* | It has caught real numeric errors headed for customer-facing output. This is the one subsystem with a documented commercial save | |
| `fixture-replay-guard` coupling | The hook exists to enforce README trigger #2 and has never fired (§B) | The battery's automation layer is inert; every replay in the record was triggered by a human deciding to run one | |

## G. Dead weight

| Component | Evidence | Effect | Verdict |
|---|---|---|---|
| `plugins/` | **57 MB** — `cache/` 34 MB, `marketplaces/` 23 MB. `installed_plugins.json` is `{"plugins": {}}`; `enabledPlugins` is `{}`. **0 files tracked in git.** *measured (fs + git)* | 57 MB of marketplace checkout against zero installed plugins. Local only — it is not repo weight | |
| `plans/` | 420 KB / 30 files. Oldest 2026-08-10, newest today. *measured (fs)* | The brief said unpruned since 2026-08-05; the oldest file is 2026-08-10. Unpruned for 25 days, not 30 | |
| `scheduled-tasks/` | 7 `SKILL.md` loop definitions for 7 tasks; 3 enabled, 3 disabled, 1 one-time | The 3 disabled definitions are retained after the 2026-08-21 retirement | |
| `projects/` (transcripts) | 492 MB total; 397 MB in the `obsidian-work` directory alone across 185 files | Not dead — it is the corpus both audits measure from. Named here so it is not mistaken for bloat | |

## H. Loops — scheduler truth vs the ledger

Closes the prior audit's third un-audited item.

| Task | Enabled | Cron | `lastRunAt` (scheduler) | Sessions (transcripts) | Verdict |
|---|---|---|---|---|---|
| `vault-review-loop` | **true** | `0 4 8 * *` | **none** | **0** | |
| `vault-skill-drift-loop` | true | `0 3 1 * *` | 2026-09-01 | 3 | |
| `vault-consolidation-loop` | true | `0 3 15 * *` | 2026-08-15 | 2 | |
| `vault-idea-research-loop` | false | `0 2 * * *` | 2026-08-21 | 31 | |
| `vault-capture-loop` | false | `0 5 * * *` | 2026-08-21 | 27 | |
| `vault-prestaging-loop` | false | `0 6 * * *` | 2026-08-21 | 25 | |
| `vault-audit-remeasure` | true | one-time 2026-09-22 | — | 0 (not yet due) | |

*measured (scheduler) for state, measured (transcript, exact) for session counts.*

Three disabled loops all stop cleanly on 2026-08-21 — the retirement executed correctly. **83 of 88 loop
runs came from those three.** Of the three still enabled, one has never run.

`vault-audit-remeasure` is already queued for 2026-09-22 to re-measure the 61% system-maintenance figure.
That is the existing slot for this audit's own re-measure obligation; no new task is needed.

## I. Vault/harness boundary — carried in, not re-derived

Measured in the 2026-09-04 research session. Carried as evidence per the brief; **no command recorded for
these rows**, and no fix for them is executed here.

| Finding | Measurement | Channel | Verdict |
|---|---|---|---|
| Close-out routine replaced the retired loops as the inbox producer | 26 of 72 inbox items created after 2026-08-21 = 1.9/day, vs the loops' ~2/day | *carried-in* | |
| The routine fires on about half of sessions | close-out phrasing in 9 of 19 attended sessions since 2026-08-21 | *carried-in* | |
| It is used as a question, not a command | 5 of those 9 ask "should we finish anything, or close out?" | *carried-in* | |
| Handoffs that name their consumer work; ones that don't rot | 3 of 3 consumed and closed; 4 of 4 "owed" notes still `status: inbox` at 11–14 days | *carried-in* | |
| The routine delegates to a retired consumer | vault `CLAUDE.md:7` still says "rough is fine, **the capture loop routes it**"; that loop was disabled 2026-08-21 | *carried-in* | |
| Terminal notes have no exit path | 6 of 26 carry `resolved`/`complete` and are still in `00-inbox/` | *carried-in* | |
| System-maintenance share fell but did not collapse | ~45% of 19 attended sessions since 2026-08-21, vs the audit's 61% and its "should fall sharply" prediction | *carried-in* | |

**One re-measurement, offered as corroboration not correction.** This audit independently counted 20
attended sessions since 2026-08-21 (vs 19) and close-out phrasing in 12 of them (60%, vs 9 of 19 = 47%).
The definitions differ — this scan matched a wider phrase set across all human turns rather than the
opening turn — so the two are not in conflict. Take the carried-in figure as the tighter one.

---

## Known limits of this audit

- **Every attended read count is a floor.** Bash-channel reads are invisible; the undercount is ~20–25%.
- **The estimating skill's load-bearing fraction was not measured.** The method was built, produced a
  nonsense result (185/185 sessions for 13 of 18 sections), and was discarded rather than reported.
- **Filesystem claims come from the tool sandbox**, which has previously shown files absent from the real
  disk. ~~The `C:\USADEBUSK\` non-existence finding needs confirmation from Jesse's own terminal.~~
  **Closed 2026-09-04: Jesse ran `ls C:\USADEBUSK` and it returns nothing.** The `git-guard` finding —
  6 firings, 0 true positives, protecting a directory that does not exist — is confirmed on the real disk.
- ~~This audit did not test a `SessionStart` hook.~~ **Closed 2026-09-04: tested and passed.** See §C.
- **The audit missed a settings file on its first pass** and found it only by starting a session. Anything
  measured by reading a fixed list of paths shares that failure mode; the counts in §E are now five files,
  but "five" is what was found, not what is provable.
- **No component was read for quality.** A skill could be excellent prose and still show zero effect.

## Appendix — commands

Run from `C:/Users/Jwuts/obsidian-work` unless noted. Transcript scans are Python over
`~/.claude/projects/C--Users-Jwuts-obsidian-work/*.jsonl`; `# exec-ok` is the documented escape for the
exec guard, not a bypass.

| Number | Command |
|---|---|
| 185 transcripts, 88 loop / 97 attended | Parse each `.jsonl`; first human turn (`promptSource` or `origin.kind == "human"`); loop iff that turn contains `<scheduled-task` |
| Skill-tool calls by skill | Assistant `tool_use` blocks where `name == "Skill"`, keyed on `input.skill` |
| Skill file reads | Assistant `tool_use` where `name == "Read"` and `file_path` matches `/skills/<name>/` |
| Script invocation counts | Assistant `tool_use` where `name == "Bash"` and the command contains the script filename |
| Hook block firings | `type == "user"` records whose `toolUseResult` contains `PreToolUse:Bash hook error`, keyed on the `usadebusk-*-guard.mjs` filename in that string |
| Hook warn firings | `type == "attachment"` records containing `additionalContext` **and** the hook's own context text (`staged note(s) LOST words`, `Staged skill edit to`). Records carrying the same text as a *read result* or `stdout` are source-reading contamination and are excluded |
| Sentinel (hatch) uses | Bash commands containing `exec-ok` / `staged-ok` / `word-delta-ok` / `replay-ok` |
| Block → outcome | For each block, the nearest preceding Bash command vs the next 7; classified as hatched, reworded (`difflib` ratio > 0.85), or different approach |
| `01-context` compliance | Per session, the set of the five mandated basenames appearing in any `Read` `file_path` |
| Config-repo commit shape | Bash commands matching `git (-C <path> )?commit` that reference a `.claude` path, since 2026-08-15, bucketed by `git -C` vs `cd … &&` |
| 29 qualifying skill commits | `git -C ~/.claude log --since=2026-08-15 --name-only -- "skills/*/SKILL.md"` |
| `__pycache__` tracking | `git -C ~/.claude ls-files \| grep -c "__pycache__"` → `0` |
| Baseline staleness | `python tools/baseline_staleness.py` |
| Loop scheduler state | The live scheduled-task registry (`list_scheduled_tasks`), not the vault ledger |
| Loop session attribution | First user turn's `<scheduled-task name="…">`, counted per task |
| `vault-review-loop` never ran | `grep -rl 'scheduled-task name="vault-review-loop' ~/.claude/projects/` → only this session's own transcript |
| Context weight | `wc -c` on `~/.claude/CLAUDE.md`, vault `CLAUDE.md`, and the five mandated `01-context` files |
| `C:\USADEBUSK\` absent | `ls -d /c/USADEBUSK` → no such file or directory; **confirmed independently by Jesse in his own terminal, 2026-09-04** |
| Directory sizes | `du -sk` under `~/.claude` |
| `SessionStart` injection works | Add `hooks.SessionStart` to `settings.json` pointing at a script that prints one line with an unguessable token; then from the vault: `claude -p "If your context contains a line beginning with SMOKE-CHECK, reply with that line verbatim and nothing else. Otherwise reply exactly: NONE."` The token must not appear in the prompt. Revert `settings.json` and confirm `git status` clean |
| 5 settings files / 139 allow rules | `ls` the three `~/.claude` paths plus `obsidian-work/.claude/settings{,.local}.json`; count `permissions.allow` in each |
| 6 inert `Write(...)` rules | Emitted by the harness itself at session start; also `[r for r in allow if r.startswith("Write(")]` in `obsidian-work/.claude/settings.local.json` |

## Log

| Date | Action | By |
|---|---|---|
| 2026-09-04 | Harness audit run per brief. Read-only against `~/.claude`, the vault, 185 transcripts and the live scheduler. One artifact, no fixes, no queue rows, nothing retired, Verdict column left empty. Corrected four of the brief's own premises — the `fixture-replay-guard` firing claim, the `__pycache__` tracking claim, the `usadebusk-fieldpm` dormancy claim, and the baseline count. Abandoned one measurement (estimating load-bearing fraction) rather than report a bad number. | Claude |
| 2026-09-04 | **Two open items closed, both on Jesse's word.** (1) He ran `ls C:\USADEBUSK` in his own terminal — nothing. The `git-guard` finding is confirmed off the sandbox. (2) He approved the `SessionStart` smoke test; it was executed and **passed** — a temporary hook was added, a fresh `claude -p` session returned the injected token verbatim, and `settings.json` was then reverted to a byte-identical state with `git status` clean. §C is updated from "unverified" to verified. Still no verdicts filled and no fix executed. | Claude |
| 2026-09-04 | **Correction found by the smoke test, not by the audit.** Starting a fresh session printed permission warnings from `obsidian-work/.claude/settings.local.json` — a **fifth** settings file, holding **107 of the machine's 139 allow rules**, which the audit's §E had not counted. Six of its `Write(...)` rules are inert (paired `Edit(...)` rules cover them, so nothing is lost). §E and the known-limits section are updated. The audit's path-list method is what missed it. | Claude |
