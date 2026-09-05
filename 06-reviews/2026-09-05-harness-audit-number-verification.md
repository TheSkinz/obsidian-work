---
type: review
status: open
review_type: verification
source_authority: observed
confidence: high
created: 2026-09-05
related:
  - "[[2026-09-04-harness-audit-evidence]]"
  - "[[2026-08-20-vault-architecture-audit-evidence]]"
tags: [review, harness, audit, verification, transcripts]
---

# Harness audit — verification of the five headline numbers

## What this is

The 2026-09-04 harness audit produced five transcript-derived headline numbers, none of which was ever
independently re-derived. All five came from the same classifier machinery that made four proxy-validation
errors elsewhere in that audit. This note re-derives all five and compares.

Three of the five reproduce. Two do not, and both failures are the same defect the audit was told to hunt:
a proxy measured and generalised without validating it against the thing it stood for.

**The corpus grew.** 187 transcripts now against the audit's 185. Where a figure moves by roughly two
sessions, that is drift and is reported as drift rather than reconciled away.

---

## Blind disclosure — read this before the figures

**The blind failed, and it failed on contact.** The verification brief
(`~/.claude/plans/verify-the-audit-numbers-quiet-lantern.md`) placed its sealed answers in the same file as
its instructions. A single `Read` returned both. There was no sequence of actions by which this session
could have read the brief without reading the five target figures, so the contamination is structural, not
a lapse.

**What was done instead.** On Jesse's ruling, the blind was rebuilt one level down. This session never
measured the corpus. Four subagents did, each given the five questions and the definitions but **not** the
sealed figures, **not** `06-reviews/2026-09-04-harness-audit-evidence.md`, and **not** anything under
`~/.claude/plans/`. Each was required to pre-register its counting method and its own failure modes in
writing before running a command, and to report contamination rather than absorb it.

| Agent | Question | Priming |
|---|---|---|
| A1 | 1 — startup compliance | Given a structural map of the record shapes |
| A2 | 1 — startup compliance | **No map.** Derived the record shapes itself |
| B | 2 — corpus split; 5 — skill usage | Map |
| C | 3 — `exec-guard`; 4 — `word-delta-guard` | Map |

Question 1 was replicated because the brief singles it out as the audit's most-cited figure. A1 and A2
answered identical question text; only the priming differed, so a divergence between them isolates the map
as the bias rather than the corpus.

**Every figure below came from a blinded channel. The comparison, the reading of the two audit notes, and
this note's conclusions did not** — they are this session's, written with knowledge of the targets. Weight
them accordingly. The figures are the evidence; the interpretation is argument.

**Three of the four agents hit contamination inside the corpus and all three reported it.** A1 saw the
audit session's own echo string disclosing a prior attended denominator of 80 and did not adjust toward it.
B found a published claim answering both its questions and re-verified its own contradicting figure by an
independent raw grep before reporting. C met a published total of 103 blocking firings *after* it had
already produced 103 independently. The corpus contains sessions auditing the corpus, so this exposure is
permanent for any future transcript work and cannot be firewalled away by instruction alone.

---

## Method, pre-registered

Each agent wrote its method and its failure modes before measuring. Three failure modes were predicted in
advance and then actually bit, which is the pre-registration doing its job.

**Polarity bit twice.** A whole-file `grep -l` for `<scheduled-task name=` returns 92–93 files against a
true 88; the extras are sessions that read or grep transcripts containing the marker. And 171 of the 464
commands carrying `exec-ok` do not trip the exec guard at all — they are `python tools/vault_lint.py …
# exec-ok`, a habitual suffix on invocations the gate never gated. Counting those as escapes overstates by
58%.

**Attribution window bit hardest, on question 3.** Pairing a sentinel use to a block gives 407 reactive
under a loose same-session rule and 23 under a strict same-command rule. Neither endpoint is the answer,
and no single number is defensible — which is why the table below carries three.

**Enumeration completeness bit on question 5, and it bit this session too.** See the map error below.

Two structural traps are worth recording for any future transcript analysis. Large tool outputs are
offloaded to `<sessionId>/tool-results/<id>.txt`, leaving a 2 KB preview in the JSONL — A2 nearly
retracted a correct all-five session because it read the preview and concluded a `head -400` had truncated
the output. It had not; the sidecar holds all 322 lines. And heredoc bodies must be stripped before
classifying a Bash command, because `cat >> change-log.md <<'EOF' … 01-context/active-jobs.md … EOF` reads
as `cat` applied to a mandated file when it is a write to a different one.

---

## The five figures

### 1. Startup-protocol compliance

Attended sessions, of 99. All figures `measured`, all floors.

| Channel | all five | at least one |
|---|---|---|
| Tool (`Read`) only — **A1 and A2 agree exactly** | **8/99 (8.1%)** | **28/99 (28.3%)** |
| Tool + Bash — A1 | 10/99 (10.1%) | 32/99 (32.3%) |
| Tool + Bash — A2 | 11/99 (11.1%) | 36/99 (36.4%) |

Loop sessions, of 88: **0/88 read all five** on every channel, both agents. At least one is 1/88 on the
tool channel and 2/88 with Bash.

**The replicate diverged, and the divergence is informative.** A1 and A2 agree to the session on the tool
channel and disagree on the Bash channel. A2 found one all-five session A1 missed — `9a696cd4`, which runs
`cd 01-context && for f in active-jobs.md company-context.md …; do cat "$f"; done`. A1's detector required
the literal string `01-context/` in the command; the `cd` form defeats it. That is enumeration
completeness failing inside a run that was explicitly warned about enumeration completeness. **A2's 11 is
the better figure and A1's 10 is a floor beneath it.**

Command (A2, three independent implementations agree on the denominator):

```bash
cd "C:/Users/Jwuts/.claude/projects/C--Users-Jwuts-obsidian-work" && for f in *.jsonl; do python -c "
import json,sys
for l in open(sys.argv[1],encoding='utf-8',errors='replace'):
    o=json.loads(l)
    if o.get('type')!='user' or o.get('isSidechain') or 'toolUseResult' in o: continue
    c=(o.get('message') or {}).get('content')
    if isinstance(c,list) and c and all(b.get('type')=='tool_result' for b in c if isinstance(b,dict)): continue
    t=c if isinstance(c,str) else ''.join(b.get('text','') for b in c if isinstance(b,dict))
    print('LOOP' if '<scheduled-task name=' in t[:400] else 'ATTENDED'); break
" "$f"; done | sort | uniq -c  # exec-ok
```

**The distribution is the finding, not the fraction.** Of 99 attended sessions: 63 read none, 17 read one,
5 read two, 3 read three, **0 read four**, 11 read all five. Compliance is bimodal, not a gradient — a
session either runs the protocol or skips it, and nothing lands on four. Ten of the eleven compliant
sessions finish all five reads inside their first sixteen assistant turns, so this is genuine startup
behaviour rather than incidental mid-session lookups.

The least-read mandated file is `equipment-fleet.md` (13 of 99); the most-read is `active-jobs.md` (27).

**Artifact that would settle it:** the tool-result stdout corpus including the 45 `tool-results/` sidecar
directories, searched for each file's own content signature. That measures what content actually returned
rather than what command was issued, and would catch every read form no verb list anticipated. Re-running
either agent's scan settles nothing.

### 2. Corpus split

**187 files, 187 sessions, 88 loop-driven, 99 attended.** `measured`, exact within the glob.

One file holds exactly one session in all 187 cases, no `sessionId` spans two files, no `uuid` appears
twice, zero unparseable lines, zero files without a human turn. The denominator question is moot — but
moot because tested, not assumed. A second, structurally independent channel confirms it: each loop session
also carries a `queue-operation` record holding the same prompt verbatim, and deriving the loop set from
that record type alone gives the identical 88 files with zero set difference.

| Loop task | Sessions | First | Last |
|---|---|---|---|
| `vault-idea-research-loop` | 31 | 2026-07-22 | 2026-08-21 |
| `vault-capture-loop` | 27 | 2026-07-20 | 2026-08-21 |
| `vault-prestaging-loop` | 25 | 2026-07-28 | 2026-08-21 |
| `vault-skill-drift-loop` | 3 | 2026-07-25 | 2026-09-01 |
| `vault-consolidation-loop` | 2 | 2026-07-19 | 2026-08-15 |

Three retired loops account for 83 of 88. No `vault-review-loop` session exists anywhere in the corpus,
independently confirming that finding.

**Artifact that would settle it:** the live scheduler's own run history under
`~/.claude/scheduled-tasks/<name>/`, which would confirm the split from outside the transcripts entirely.

### 3. `exec-guard`

**85 blocks across 63 sessions.** `measured`, floor. Per-hook split of all 103 blocking firings in the
corpus, so the figure is checkable against its siblings:

| Hook | Blocks | Sessions | First | Last |
|---|---|---|---|---|
| `usadebusk-exec-guard` | 85 | 63 | 2026-07-29 | 2026-09-04 |
| `usadebusk-staged-count-guard` | 12 | 12 | 2026-07-27 | 2026-09-03 |
| `usadebusk-git-guard` (retired) | 6 | 6 | 2026-07-23 | 2026-08-16 |
| **total** | **103** | **70** | | |

**464 Bash commands carried `exec-ok` across 41 sessions — but only 293 would actually have been blocked.**
The classifier was validated by re-implementing the hook's own `decide()` and running it against the 85
real blocks: it flags 85 of 85, zero divergence, and no blocked command ever contained the sentinel.

The overlap, three ways, because no single pairing rule is defensible:

| Pairing rule | All 464 | The 293 that would have tripped |
|---|---|---|
| Any earlier block in the same session (loose) | 407 | 236 |
| Sentinel command *is* a previously blocked command (tight) | 23 | 23 |
| Sentinel on the very next Bash call after a block | 38 of 85 blocks (45%) | — |
| **Pre-emptive — no block earlier in that session** | **57** | **57** |

**The 57 pre-emptive uses collapse entirely under inspection.** All 57 live in two sessions: 53 in
`4a153e72`, the sibling audit session scanning this same corpus on 2026-09-05, and 4 in `80ad9814`, the
session that *wrote* exec-guard, testing it 45 seconds before committing it. Exclude both meta sessions and
**411 sentinel uses remain across 40 ordinary sessions, of which zero are pre-emptive.** Every working
session that hatched the gate had been blocked first, in that same session.

The complement matters as much: **23 of the 63 blocked sessions never used the sentinel at all.** They were
stopped and rerouted.

**Artifact that would settle it:** a `PreToolUse` hook-invocation log written by the harness itself. None
exists; the transcript is the only witness, which is precisely why the subagent gap below is unclosable.

### 4. `word-delta-guard`

**17 genuine firings across 10 sessions. Last firing 2026-08-25T00:33:32Z.** `measured`, floor.

Both attachment shapes carry all 17 with identical `(sessionId, toolUseID)` keys — they are duplicate
persistences of the same events, not 34 events. A parser summing both shapes gets 34 and is wrong.

The attribution hazard flagged before dispatch turned out not to be load-bearing. `hookName` isolates
`PreToolUse:Bash` to 18 records; the text anchors split those 17 word-delta / 1 fixture-replay with **zero
residue**, so two orthogonal channels agree and the unattributable bucket is empty. Anchor drift was
checked and did not apply: the hook has exactly one commit in its history and the matched strings are the
only strings it has ever emitted.

Naive matching for contrast: the message opener returns 45 lines across 15 sessions (2.6× the firings), and
the hook's *name* returns 195 lines across 45 sessions (11.5×). Every one of the 17 firings resolves to its
triggering `git commit` call, none unresolved.

Since the last firing there have been 17 further scoped, sentinel-free `git commit` calls, 11 naming the
vault, none of which fired — so the silence is the lint finding no losses, not the hook being off.

**Artifact that would settle it:** replay the vault's own `git log` for scope-claiming commits through
`python tools/vault_lint.py --staged` at each commit. That reconstructs the fire set from the repo rather
than the transcript, and would catch any firing whose session was never persisted.

### 5. Skill-tool usage

**40 `Skill` calls in the 187-file glob.** `measured`. Two structured paths cross-check clean — 40
`tool_use` blocks and 40 `toolUseResult.commandName` records, identical per-skill tallies, all 40
succeeding. A raw `grep -o '"name":"Skill"'` returns 48; the 8 extras are attachment records echoing
transcript content in the four transcript-reading sessions.

Of those 40, **28 are `usadebusk-*`, and the most recent is 2026-09-04T19:08:47Z** — `usadebusk-equipment`,
session `d6b54c2b`, a real attended work session. Verified directly, independently of the agent:

```bash
# last in-glob usadebusk Skill-tool loads, by timestamp
2026-08-22T15:26:54.644Z usadebusk-estimating 58b7d739
2026-09-04T19:08:47.026Z usadebusk-equipment d6b54c2b
```

**And the glob is not the corpus.** Subagent transcripts are fully persisted at
`<sessionId>/subagents/agent-*.jsonl` — 114 files, every record carrying `isSidechain: true`. They fall
outside `*.jsonl` only because they sit one directory down. Inside them: **133 further `Skill` calls, every
single one a `usadebusk-*` skill**, running 2026-07-24 through 2026-09-05. Five failed (all
`usadebusk-vault-ingest`, hitting `disable-model-invocation`); 128 succeeded.

| Scope | `Skill` calls | of which `usadebusk-*` | Last `usadebusk-*` |
|---|---|---|---|
| In-glob (`*.jsonl`) | 40 | 28 | 2026-09-04 |
| Subagents (out of glob) | 133 | 133 (128 ok) | 2026-09-05 |
| **Corpus-wide** | **173** | **161** | **2026-09-05** |

Verified directly: `find . -mindepth 2 -name 'agent-*.jsonl' | wc -l` → 114; `isSidechain:true` → 4,547
outside the glob, **0 inside it**.

`attributionSkill` was investigated and is **not** a separate channel — it is a per-run provenance tag on
the `Skill` call, spanning from the invocation to the last assistant record of that agentic run and never
resuming after the next human turn. It understates governance rather than overstating it, and adding it to
a load count would double-count. Two genuine additional channels do exist: slash-command expansion (`/adhd`
in one session loads a skill body with no `tool_use` emitted at all) and the loop prompts, all 88 of which
are inlined from files literally named `SKILL.md` under `~/.claude/scheduled-tasks/`. Neither touches a
`usadebusk-*` skill, so neither moves this answer — but a channel inventory stopping at "Skill tool vs
Read" misses both mechanisms.

**Artifact that would settle it:** session `d6b54c2b` at record index 237 — open it and look. The call
carries `{"skill": "usadebusk-equipment"}`, the result reads `Launching skill: usadebusk-equipment`,
`success: true`, and the skill body is injected at index 239. One record in one file decides between
2026-09-04 and the audit's 2026-08-22.

---

## Comparison against the audit

| # | Number | Audit | This verification | Verdict |
|---|---|---|---|---|
| 1 | Startup compliance, all five | 7% (7/97), tool channel | 8/99 tool; **11/99 both channels** | **agrees** on channel; the comparison built on it does not — see below |
| 1 | At least one | 28% (27/97), tool channel | 28/99 tool; **36/99 both channels** | **agrees** on channel |
| 1 | Loop, all five | 0 of 88 | 0 of 88 | **agrees** |
| 2 | Corpus split | 185 — 88 loop, 97 attended | 187 — 88 loop, 99 attended | **agrees**, drift of +2 attended |
| 3 | `exec-guard` blocks | 85 | **85** across 63 sessions | **agrees** |
| 3 | Commands carrying `exec-ok` | 416 | **464** raw, 293 gate-tripping | **diverges** |
| 3 | Pre-emptive sentinel uses | ~372 (89%) | **57 nominal → 0 by any ordinary session** | **diverges — inverts** |
| 4 | `word-delta-guard` firings | 17 / 10 sessions, last 2026-08-25 | **17 / 10 sessions, last 2026-08-25** | **agrees** |
| 5 | `Skill` calls | 40 in 185 sessions | **40** in-glob; **173** corpus-wide | **agrees** in-glob; **diverges** corpus-wide |
| 5 | Last `usadebusk-*` via Skill tool | 2026-08-22 | **2026-09-04** in-glob; **2026-09-05** with subagents | **diverges** |

### Number 1 — the figure reproduces; the argument it carries does not

The audit's tool-channel figures reproduce to within corpus drift, and both agents agree with each other
exactly on that channel. On its own terms number 1 is sound.

**What does not survive is the comparison the audit builds on it.** §2 sets its 7% against "the prior
audit's headline — 43% of attended sessions" and presents a collapse. The prior audit's 43% is `34/80`,
where 34 is arithmetically `27 + 7`: 27 is its `01-context/` **folder-demand** cell, defined at
`06-reviews/2026-08-20-vault-architecture-audit-evidence.md` line 246 as "how many sessions opened it,
measured as a tool call carrying a `file_path` under that path" — **at least one file** — and 7 is the
Bash-channel top-up it measured separately.

| | Predicate | Channel |
|---|---|---|
| 43% (2026-08-20) | opened **at least one** `01-context/` file | tool **+ Bash** |
| 7% (2026-09-04) | read **all five** mandated files | tool **only** |

Two independent mismatches stacked. The prior audit seeded it — its prose reads "CLAUDE.md says to read
every file in `01-context/`. Counting both channels, 34 of 80 attended sessions did — 43%", attaching
"did" to *every file* over a number that means *any file*. The 2026-09-04 audit inherited the mislabel and
compared across it.

**Measured like for like, the honest pair is 43% then against 36% now** — a decline of about seven points,
not a collapse from 43 to 7. Provenance: read from both notes plus one arithmetic step (27+7=34, 34/80 =
42.5%), not inferred.

A second, smaller inheritance: the audit applies "every attended read count is a floor, ~20–25% low" as a
blanket. Measured here, the Bash-channel undercount is 27% on all-five and 22% on at-least-one for A2, 20%
and 12.5% for A1. One correction factor across both metrics overstates the looser one.

### Number 3 — the block count holds and the conclusion reverses

85 blocks is exact. The sentinel count is 464 rather than 416, and the composition matters more than the
gap: only 293 of the 464 would have tripped the gate, the other 171 being a habitual `# exec-ok` suffix on
`python tools/vault_lint.py` invocations the guard never gated.

The pre-emptive claim inverts. The audit reports ~372 of 416 (89%) as pre-emptive and reads that as a gate
routed around before it ever fires. Measured, **zero ordinary sessions used the sentinel before being
blocked**; the 57 that look pre-emptive are 53 from the audit's own sibling session scanning this corpus
and 4 from the session that wrote the hook.

The audit reached 372 by treating "not an immediate retry of this block" as "never blocked" — the
attribution-window error, on the same hook family that produced the "12 of 12 hatched" correction. Its own
~44 figure is close to the measured immediate-retry rule (38 of 85, 45%); what fails is the inference from
the remainder.

**The mechanism is the opposite of what §2 describes.** The gate fires, and *then* gets hatched. And 23 of
63 blocked sessions never hatched at all — they rerouted.

### Number 5 — wrong on its own corpus, then wrong again on scope

The audit's date is wrong twice over. In-glob, the last `usadebusk-*` Skill-tool load is 2026-09-04
19:08:47Z, not 2026-08-22. This is not a timing artifact: the audit session `4a153e72` ran 2026-09-05
00:31–08:07Z, **five hours after** that call, and `d6b54c2b` was already inside its 185-file corpus.

Then the scope error. 133 further Skill calls sit in subagent transcripts one directory below the glob,
**every one of them a `usadebusk-*` skill**, the most recent running less than two hours before this
verification began. The glob sees roughly 17% of the real `usadebusk-*` Skill traffic.

This is load-bearing beyond number 5. It is the lead evidence for the audit's **structural finding**
(§Findings 1, "Every gate and every route is built on an interface the work does not use"), whose first
bullet reads: "The `Skill` tool was called 40 times in 185 sessions, and no USADebusk skill has been loaded
through it since 2026-08-22." The skills were loaded through it 128 times successfully, and one ran today.

---

## Findings beyond the five

**The subagent blind spot is the largest single defect found, and this session propagated it.** My recon
map told three of the four agents that subagent internals are not persisted and that `isSidechain` is false
everywhere. Both claims are true inside `*.jsonl` and false one directory down. A1 and C both "confirmed"
it. A2, which received no map, derived the same wrong conclusion independently — so the glob itself is the
trap, not merely the map. Agent B found the truth by asking what its channel inventory would miss rather
than by checking the field.

Three agreeing confirmations of a false claim, all three checking the same scope. That is the
already-recorded pattern that four sources agreeing prove nothing when all four derive from the artifact in
question, and it recurred here inside a run explicitly designed to catch it.

**The consequence is general.** Any conclusion in this vault drawn from `~/.claude/projects/<project>/*.jsonl`
about tool usage, delegation, or skill activity undercounts by an unknown margin — for skill usage
specifically, by four-fifths. Both the 2026-08-20 and 2026-09-04 audits are scoped to that glob.

**Two sessions sit outside the brief's corpus definition**, in
`C--Users-Jwuts-obsidian-work-50-dashboards` (1) and a `claude-worktrees-friendly-perlman` worktree (1),
both with a vault `cwd`. Reported rather than merged, per ruling, so the comparison stays clean. Small in
themselves, but the same enumeration-completeness shape as the missed fifth settings file.

**`smoke-sessionstart` is clean — closed.** Agent C flagged a `SessionStart:startup` hook injecting a
`SMOKE-CHECK` token on 2026-09-05T01:35:32Z and not present in `settings.json`, raising the possibility it
was still armed. Checked directly: no `SessionStart` entry in any of the four settings files, no smoke
script in `~/.claude/hooks/`, config repo `git status` empty. The audit's byte-identical revert holds; C
was seeing the smoke test itself.

**`fixture-replay-guard` transitioned, and the transcript dates it independently.** Created
2026-07-28T21:51Z, zero firings for 38 days, cwd bug fixed by `96d06fb` at 2026-09-05T02:19Z, first genuine
firing 2026-09-05T05:07Z. The hook's own header claim of 29 silent qualifying commits is consistent with
the record.

**One loop session came within one file of compliance.** `026734f5` (2026-07-25, skill-drift loop) read
four of the five and missed exactly `output-preferences.md` — the file governing how it writes, which is
the omission you would notice in the output rather than the reasoning.

---

## Implications

**The `SessionStart` hook proposal loses its stated justification but not necessarily its case.** The
7%-versus-43% collapse that motivates it is an artifact of comparing an all-five tool-only figure against
an at-least-one both-channel one. Like for like it is 43% → 36%. But the underlying fact is unchanged and
is arguably worse than the audit said: **63 of 99 attended sessions read none of the five, and 0 of 88 loop
runs read all five.** The hook should be argued from that distribution, and specifically from its bimodality
— compliance is a mode a session enters in its first sixteen turns or never enters at all, which is exactly
the shape a `SessionStart` injection addresses. It should not be argued from a trend that was never
measured.

**Nothing that rests on `exec-guard` being routed around pre-emptively should stand.** The gate is
experienced, then hatched, by every ordinary session that hatches it — and a third of blocked sessions
never hatch at all. Any tuning argued from "the gate fires into a void" is arguing from an inverted
premise. Note that the audit's `staged-count-guard` threshold change (12 → 25, commit `7be001a`) was swept
against real commit history rather than derived from this classifier, so it is not implicated.

**The structural finding needs re-running, not retracting.** "Every gate and every route is built on an
interface the work does not use" may still be true, but its lead evidence is false: the `Skill` tool is
used, 173 times corpus-wide and 161 of those on `usadebusk-*` skills, most recently today. Whether the
*other* limbs of that finding survive — the ≤2 lifetime invocations of command-only skills, the routing
claim generally — cannot be judged from this note, because every one of them was measured through the same
glob that hid four-fifths of the skill traffic. **Re-measuring the harness's route usage against
`*.jsonl` plus `*/subagents/agent-*.jsonl` is the single highest-value follow-up here**, and it is a
different job from this verification.

**On the method itself.** Pre-registration worked: three predicted failure modes bit and were caught
because they had been named in advance. The replicate worked: A1 and A2 agreed exactly on the tool channel
and diverged on the Bash channel, and the divergence located a real enumeration gap in A1 rather than
noise. What did not work is a blind delivered in the same file as its answers — the durable fix is to split
a sealed section into its own file, so the seal survives being read.

---

## Log

| Date | Action | By |
|---|---|---|
| 2026-09-05 | Five headline numbers from the 2026-09-04 harness audit re-derived by four blinded subagents, question 1 replicated across two. Read-only; no skill, hook, settings, `CLAUDE.md` or audit-note file touched, no Verdict cell filled, one artifact. **Blind broken at source** — the brief's sealed answers shared a file with its instructions, so the orchestrating session was contaminated before measuring and never touched the corpus; disclosed above. **Three of five agree** (corpus split, `exec-guard` blocks, `word-delta-guard` firings). **Two diverge:** the `exec-guard` pre-emptive claim inverts (~372 pre-emptive → 0 by any ordinary session; the 57 that look pre-emptive are the audit's own sibling session and the hook's author testing it), and the last `usadebusk-*` Skill-tool load is 2026-09-04 in-glob and 2026-09-05 including subagents, not 2026-08-22. Number 1 reproduces on its channel but the 43%→7% comparison underneath it pairs an at-least-one both-channel figure against an all-five tool-only one; like for like it is 43%→36%. **Largest defect found: subagent transcripts are fully persisted at `<sessionId>/subagents/agent-*.jsonl`, outside the `*.jsonl` glob both audits used** — 114 files, 133 `Skill` calls, all `usadebusk-*`. This session's own recon map asserted the opposite and three of four agents confirmed it; the fourth disproved it. | Claude |
