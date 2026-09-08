<!-- vault-loop: operational — session handover, governance question on 00-inbox/ routing policy. Needs Jesse in session; do not self-route. -->
---
type: note
status: open
source_authority: stated
confidence: high
created: 2026-09-08
review_after: 2026-10-08
related:
  - "[[vault-capture-loop-spec]]"
  - "[[vault-agent-loop-spec]]"
  - "[[2026-08-20-vault-architecture-audit-evidence]]"
  - "[[2026-09-08-review-loop-spec-references-stopped-loops]]"
  - "[[decision-queue]]"
tags: [handover, knowledge-system, inbox, routing, governance]
---

# Handover — is `00-inbox/` routing worth it, and what happens to the 82

**For the next session.** Jesse wants to examine how and why notes get routed to `00-inbox/`, whether the strategy has produced anything, whether loose ends are better closed in the session that creates them, and only then whether to work the pile down or write parts of it off.

**Read this whole file before touching the inbox.** The measurements below already exist. Re-deriving them is the main way this session wastes itself.

---

## The one-paragraph answer, if you only read one

The inbox has almost never worked as a router. Of 147 notes ever added, roughly 11 show evidence of their content reaching a home — 5 files relocated into a vault folder, 6 carrying the line-1 `ROUTED` marker. Thirty-nine were swept to `archive/` as finished without their content going anywhere, which is the system working as a scratchpad, not as a waystation. Meanwhile the only sanctioned mechanism that removes anything, the Terminal-Note Sweep, lives inside the capture loop that was stopped on 2026-08-21, so removal has effectively ceased: 54 notes left the inbox in the 29 days before the shutdown and **1** has left in the 18 days since. Twenty-two of the current 82 are finished work that is stuck for purely mechanical reasons and need no decision from anyone.

---

## What the 82 actually is

Counted today from the `status:` frontmatter of every note in `00-inbox/`, against the sweep allowlist in `vault-capture-loop-spec.md:113`.

| Bucket | Count | What it means |
|---|---|---|
| Sweepable now | 22 | `resolved` 15 · `closed-unactioned` 4 · `complete` 3. Finished and filed elsewhere. Blocked only because nothing runs the sweep |
| Held by a trigger | 1 | `resolved` but carries `revisit-trigger:`; the sweep's own safety rule protects it |
| Protected by design | 21 | `researched` 10 · `unexplored` 11. Idea seeds awaiting Jesse. The sweep is **explicitly forbidden** from touching these |
| Live remainder | 38 | `inbox` 21 · `open` 13 · `gated` 4 |

**The headline number is misleading.** "82 inbox items" is really 22 finished, 21 parked by design, and 38 that might be work. Any ROI argument built on 82 is built on the wrong denominator.

By type: `note` 32, `idea-seed` 30, `finding` 11, `review` 5, `capture` 4. Also present and not counted above: `raw-docs/` and one stray `f501-coil-teardown-source.html`.

## What routing has actually produced

Of the 63 distinct notes that ever left `00-inbox/`:

| Destination | Count | Reading |
|---|---|---|
| `archive/` | 39 | Swept as finished. Content went nowhere; the note was just closed |
| Elsewhere in the vault | 5 | Genuinely relocated to a home folder |
| Gone entirely | 19 | Not in `archive/`, not elsewhere. Includes 2 in-inbox renames (`CND`→`CAD`) |

Add the 6 notes carrying the line-1 `ROUTED` marker — the three-outcome logic's *primary* outcome appends content to a home note and leaves the file in place, so relocation alone undercounts it — and the evidence of real routing is about **11 events against 147 notes added, near 7%**.

**Provenance and its limit.** That 7% is my computation from git history plus current file locations, not a stated figure, and it is a **floor**: content may have been appended to a home note without the marker being applied, and marker discipline is visibly imperfect (22 notes carry a `vault-loop:` comment against 6 carrying `ROUTED`). Treat it as "routing was rare," not as a precise rate. The artifact that would tighten it is a read of the `ROUTED` and `vault-loop:` notes themselves.

## Why removal stopped

`vault-capture-loop-spec.md:111` defines the Terminal-Note Sweep and the spec says outright that adding a status to its allowlist is *"inert on its own while the capture loop is disabled (2026-08-21) — the sweep runs at the end of inbox ingestion and nothing else calls it."* Nothing else calls it. That is the whole mechanism, and it explains the churn cliff:

| Period | Days | Added | Removed | Net/day | Drain rate |
|---|---|---|---|---|---|
| 2026-07-24 → 08-21 | 29 | 81 | 54 | +0.93 | 67% |
| 2026-08-22 → 09-08 | 18 | 28 | 1 | +1.50 | 4% |

**Correcting something I told Jesse earlier today.** I said growth slowed after the shutdown. The *addition* rate did slow, 2.79/day to 1.56/day. But the drain collapsed, so the pile now accumulates about 60% faster than it did while the loop ran. The 2026-08-20 audit's "net producer" verdict measured net, and net was `+0.93/day` then against `+1.50/day` now. That does not make stopping the loops wrong — roughly half the removals in the loop era were attended `[gated]`/`[default]` commits, and the loop's own biggest contribution was a 20-file sweep, not routing — but it does mean **the shutdown removed a drain nobody replaced**, and that is the real defect, not the loops.

## Why it keeps filling — live instructions pointing at dead consumers

This is the half my own measurements missed, and it is the mechanism behind the accumulation. Several **active** files still tell a session to write into `00-inbox/` and name a stopped loop as the thing that will pick it up. Each was read and quoted from the file:

| Source | Status | What it promises |
|---|---|---|
| `~/.claude/skills/idea-triage/SKILL.md:31` | active skill | Park → create a seed in `00-inbox/` *"so the nightly Idea Research Loop picks it up."* Parking without the seed is *"forbidden"* |
| `08-systems/mobile-field-access.md:74-82` | active | *"the 05:00 loop routes it the next morning. Do not file from the phone"*, and operational content waits *"for the 06:00 pre-staging loop to analyse"* |
| `04-knowledge/knowledge-system-governance.md:151` | `status: active` | Still describes the nightly Idea Research schedule |
| `~/.claude/skills/usadebusk-vault-ingest/SKILL.md` (6 sites) | active skill | Unknown client, unnormalizable city/state, missing unit folder → *"flag and route to `00-inbox`"* |

All three loops are confirmed `enabled: false` with `lastRunAt` 2026-08-21, read live from the scheduler rather than inferred from vault notes. So the field-capture path in particular is a trap: it instructs Jesse not to file from the phone because a 05:00 loop will handle it, and nothing will.

**This is DQ-032's defect on the producer side.** DQ-032 is about the review loop's spec naming a dead *consumer*; this is four active documents naming dead consumers to *writers*. Same root cause, and they should be fixed in one pass rather than separately.

Two smaller findings worth carrying: `00-inbox/.capture-state.json` is a 155 KB orphan last written 2026-08-21 that nothing now reads, and `00-inbox/raw-docs/` — the vault-ingest staging path — is empty and unused. Also note `vault_index.py:9` deliberately **excludes** `00-inbox/` from `INDEX.md` as *"transient"*, which is the vault's own existing verdict on what this folder is.

## Prior art — do not re-derive this

**A session on 2026-09-07 already answered half this question.** Per `change-log.md:16`: Jesse *"chose file at write time over re-enabling the capture loop, then chose the metric correction over working the backlog once the tail turned out to be rulings and owed work rather than filing."* That session read **all 39 notes in the ≥14-day tail** and found *not one* unfiled capture record — 15 live idea seeds, plus open rulings awaiting Jesse and owed work sessions. The conclusion was that the metric *"conflated unfiled with undone."*

So the "is the inbox a filing backlog" question is answered: no. What is genuinely open is narrower than Jesse's framing suggests, and the session should say so rather than re-opening settled ground.

Related and still open: **DQ-032**, filed today, is that `vault-agent-loop-spec.md` still names the stopped Capture Loop as the owner of inbox routing. Whatever this session decides about policy should probably absorb DQ-032 rather than run beside it — the spec correction and the policy question are the same subject.

---

## The three questions, separated

They arrived bundled and they have different answers and different owners.

**1. Is `00-inbox/` worth having as a routing destination?** Largely answered — the 7% figure and the 2026-09-07 ruling both say it never functioned as one. The live sub-question is whether to formalise that: declare the inbox a *capture scratchpad with a sweep* rather than a router, and delete the routing language that implies otherwise. That is a Lane 2 call and probably yours to recommend.

**2. Is there a drain?** No, and this is mechanical rather than philosophical. Twenty-two notes are finished and stuck because the only sweep implementation sits inside a disabled loop. Fixing this does not require answering question 1 — it is a `git mv` per note under safety rules the spec already states.

**3. Are the 38 live notes worth working?** Genuinely open, and the only one that needs Jesse. Note that the 2026-09-07 read suggests most are *rulings awaiting him* and *owed work sessions* rather than filing — meaning "work the pile down" mostly means "make decisions," which is a different and much more expensive activity than filing.

## Advice, and the traps

**Decide the policy before touching the pile.** Working 82 notes by hand into a system you may then delete is the worst available order. The 22 sweepable are the exception — they are correct to move under any policy.

**Do not re-read all 82 notes.** The ≥14-day tail was read five days ago. Read the 2026-09-07 change-log entry and the notes that are new since, and spend the saved effort on the policy question.

**The 21 protected seeds are a different system.** `CLAUDE.md` says the idea flow owns them and they belong in `00-inbox/` by design. Folding them into an inbox verdict will produce a wrong answer about both. Same for Lane 4 operational content, which is in there deliberately and needs Jesse.

**If you sweep, follow the spec's four safety rules** (`vault-capture-loop-spec.md`, "Rules that make this safe"): never sweep `researched`/`unexplored`, never sweep a `revisit-trigger:` note, never rename, and grep the moved basenames afterward because backticked *path* references dangle silently and nothing lints them. Additionally — from the vault `CLAUDE.md` — `archive/` is in `.gitignore` but partly tracked, so run `git ls-files` on a specific file before assuming a move there is recoverable.

**Beware the counterfactual trap on ROI.** "The inbox produced little" does not by itself argue for deleting it. The alternative — closing loose ends in the session that creates them — has its own failure mode, which is that a session under time pressure drops the finding entirely rather than filing it badly. The measurable question is not *did routing work* but *what happened to findings that were never captured at all*, and nothing in the vault records those. Say so rather than pretending the comparison is available.

**One live specimen.** This file is a handover note being written into `00-inbox/` per an established convention (five prior examples, `2026-09-06-handover-f4-replay-and-rate-rollup.md` most recently). It is a fair test case for question 1: is this the right home for it, or should a handover live somewhere with an owner?

## What would settle each question

Question 1 needs a read of the ~28 `ROUTED`/`vault-loop:`-marked notes to tighten the 7% floor into a real rate, plus a decision on what the folder is *for*. Question 2 needs no evidence, only execution. Question 3 needs Jesse reading a triaged list of the 38, ideally sorted by whether each is a decision, an owed build, or a capture that can simply be closed.

**Tooling facts that bound what is possible.** No script anywhere writes into `00-inbox/` or moves anything out of it — `vault_lint.py`, `vault_health.py` and `vault_index.py` read only, and the sole automated move ever specified is the Terminal-Note Sweep inside the deprecated capture-loop spec. Removal is entirely manual today. `INBOX-AGE` lint is retired (`vault_lint.py:52`), so the only remaining lint pressure on the folder is `STATUS-MISSING`, a warning currently firing once. `health.md`'s Notes section still names INBOX-AGE among current warnings, which is stale text worth fixing in the same pass.

---

## Outstanding task

**First: correct the four producer documents.** `mobile-field-access.md` is an operational trap, not just stale text — it tells Jesse *"Do not file from the phone"* on the promise that a 05:00 loop will route his field capture, and nothing will. `idea-triage`'s Park disposition forbids parking without creating a seed for a research loop that is off. Striking the dead-consumer promises is correct under **every** policy outcome, so it does not wait on question 1, and it stops the bleeding before anyone counts the pile again. This is DQ-032's defect on the producer side and belongs in the same pass.

**Second: sweep the 22.** Finished work, git-tracked and reversible, no decision needed from Jesse, and it drops the inbox from 82 to 60 — which makes every subsequent count in the policy discussion mean something. Do it under the spec's four safety rules, then re-run `vault_lint.py` and `vault_health.py`.

**Third: put question 1 to Jesse as a single Lane 2 recommendation**, not an open exploration. On the evidence, `00-inbox/` is a capture scratchpad with a periodic sweep — which is what `vault_index.py` already assumes by excluding it as "transient" — and the routing language across `CLAUDE.md`, `vault-capture-loop-spec.md` and `vault-agent-loop-spec.md` should be rewritten to say so. Question 3, whether the 38 live notes are worth working, comes last: until the folder has a stated purpose there is no basis for deciding which of them still deserve one.
