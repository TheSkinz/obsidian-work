---
type: governance
status: active
source_authority: primary
confidence: high
created: 2026-06-30
last_reviewed: 2026-07-29
review_after: 2026-10-29
related:
  - [[vault-capture-loop-spec]]
  - [[vault-agent-loop-spec]]
  - [[vault-prestaging-loop-spec]]
  - [[knowledge-system-governance]]
tags: [knowledge-system, agent-loop, idea-research, governance]
---

# Vault Idea Research Loop Spec

The third loop, distinct from the other two in kind rather than just scope. [[vault-capture-loop-spec]] files and harvests; [[vault-agent-loop-spec]] reviews the operational core. This loop does neither — it investigates. It picks one speculative idea-seed, does bounded web research on it, and reports findings back for Jesse to decide on. It never files, never harvests, never touches operational content, and never decides or implements anything itself.

Origin: a recurring pattern where ideas discussed in chat got dismissed as low-ROI or infeasible from priors, only for later research to find a power-user had already solved the same problem with an off-the-shelf tool or technique. This loop is the direct fix — it spends bounded, otherwise-idle overnight capacity checking "has someone already solved this" before Jesse spends a session re-deriving the answer from scratch.

## Loop Name

Vault Idea Research Loop

## Trigger

**Scheduled nightly (~2 AM local) via `mcp__scheduled-tasks` as of 2026-07-07.** The original gate — "schedule only once the decision queue has a sustained track record of staying near-empty" — was judged passed on 2026-07-07: the queue has held at 0 open since the 2026-07-05 backlog clearance, and both prior research notes (07-01, 07-05) were reviewed and acted on. Runbook prompt: `~/.claude/scheduled-tasks/vault-idea-research-loop/SKILL.md`; it is heartbeat-tracked in `tools/vault_health.py` as `("Idea-research loop", "vault-idea-research-loop", "vault-idea-research:", 30, 3)` — ledger id, commit prefix, 30-day monitoring cadence, 3-day ledger staleness. (Corrected 2026-07-29: this line previously claimed a `scheduled` flag set to `True`. No such flag exists — `LOOP_HEARTBEATS` is a list of 5-tuples and always was in the version this spec described.) If the queue stops draining (health dashboard shows review notes piling past their cap), de-scheduling this loop again is the correct pressure-relief valve.

**History:** it was briefly scheduled nightly (deployed 2026-06-30, ran 07-01 and 07-02), then de-registered as collateral of the 2026-07-02 kernel-consolidation plan — a plan reversed on 2026-07-05 in favor of keeping the loops + the decision queue. Re-scheduling it is now a deliberate future step gated on the queue proving it drains, not an automatic restore.

This loop only needs git-tracked vault content and web search, so unlike the Capture Loop it has no dependency on local session transcripts. It could in principle run as a fully desktop-independent cloud routine, but that mechanism was checked during this loop's design and found unavailable in this environment (the relevant remote-environment service returned 404 on every call).

## Scope

Reads:

- `00-inbox/*.md` files with frontmatter `type: idea-seed` — the only input queue this loop watches.

**Exclusive ownership of `type: idea-seed` (recorded here 2026-07-29).** [[vault-prestaging-loop-spec]] skips every `idea-seed` file **even when it carries a `<!-- vault-loop: -->` defer marker**, precisely so the two loops never process one item. That rule was written only in the pre-staging spec; it is restated here because it constrains both sides and a reader of this spec alone could not have known it. The practical consequence: a defer marker on an idea-seed does **not** mean the item is queued elsewhere — this loop is still its only consumer.

Writes:

- One new review note per run in `06-reviews/`, using the standard review-note pattern (see [[vault-agent-loop-spec]] Output Artifact Requirements) with `review_type: idea-research`.
- The source idea-seed note: flips `status: unexplored` to `status: researched` and adds a `related:` link to the new review note. No other edit to the idea-seed's content.

Never touches `02-facilities/`, `04-knowledge/` canonical content (other than its own spec file, which it does not self-edit), pricing, SOPs, skills, or any operational content. If an idea-seed's subject turns out to be operational rather than speculative, this loop stops and defers to [[vault-agent-loop-spec]] instead of researching it.

## Ceremony Level

Low, but not silent. Every run either produces one evidence-gathering artifact (a review note, never a canonical change) or cleanly no-ops. Nothing this loop writes is a decision — the Decision checklist in the review note is Jesse's, not the loop's, exactly as in the Agent Loop pattern.

## Loop Steps

**Run ledger (every run, first and last action):** Before anything else, update `50-dashboards/.loop-runs.json` (local, gitignored — create if missing): set this loop's entry (`vault-idea-research-loop`) to `{"fired": "<now, UTC ISO-8601>", "completed": null, "result": "running"}`, merging without touching other loops' entries. As the run's very last action — after the final push, or immediately on deciding the run is a no-op or hitting a fatal problem — set `completed` to now and `result` to `committed`, `no-op`, or `error: <one line>`. Use Write/Edit tools, never shell editors. `tools/vault_health.py` reads this file to tell a dead scheduler from a quiet loop; a run that skips it surfaces as a monitoring FAIL. This matters most for this loop: it no-ops on most nights, and the ledger is the only signal separating "no seeds to research" from "scheduler stopped firing."

1. Scan `00-inbox/` for files with `type: idea-seed` and `status: unexplored`. Seeds already at `status: gated` are **not** candidates — their gate is known shut. If no `unexplored` seeds exist, report a clean no-op and stop — do not manufacture work.
2. Pick the oldest unexplored idea-seed (by `created` frontmatter date).
3. **Gate check — before any research.** Read the seed's `**Gate:**` line, and any gating condition stated in its "To explore" text even if it is not on a `**Gate:**` line (older seeds pre-date the convention and bury it in prose — "gating condition:", "not until", "the trigger is", "only once" are the usual phrasings). Then try to settle that condition **from files only** — the triage or review note that was supposed to run it, the data the seed is waiting on, the build it depends on. Three outcomes:
   - **Gate verifiably unmet:** do not research. Set the seed to `status: gated`, add or refresh a `revisit-trigger:` frontmatter field stating the condition in the dormant-trigger registry's format, and write a short review note (Interpretation: "gated — not researched") recording the gate, the evidence that it is shut, and what would re-open it. Then **return to step 2 and pick the next-oldest unexplored seed**, so a shut gate costs one file read rather than a whole run. Process at most one *researched* seed per run; gate-closures do not count against that budget.
   - **Gate verifiably met, or no gate stated:** proceed to step 4 and research normally.
   - **Gate stated but not settleable from files:** research normally, and name the unresolved gate in the review note's Interpretation. Do not guess it shut — an unverifiable gate is not a reason to skip work, only a caveat on the finding.

   The rule this encodes: a seed that ships with its own test-before-build condition has already told you what to check first, and checking it costs a minute against a research cycle. This was added 2026-07-25 after the LLM-navigable-vault-map seed consumed a full run rediscovering a gate that had closed two days earlier, with the next seed in the queue gated the same way.
4. Read the seed's "Tentative read" and "To explore" sections as the research brief.
5. Research: web search for prior art, existing tools, or power-user solutions to the problem the idea describes. Also check what's already built in this vault (`04-knowledge/`, `06-reviews/`) and in the deployed skills (`~/.claude/skills/`) that might already cover the idea, partially or fully — many ideas turn out to be already-solved or already-partially-built, and that's a valid, valuable finding.
6. Write a review note in `06-reviews/` (filename pattern `YYYY-MM-DD-idea-research-<slug>.md`) using the standard template: Trigger (why this seed was picked), Evidence (sources found, with links), Interpretation (sound / trap / premature / already covered, and why), Recommended Action (build now / bounded one-shot investigation / park / drop), Decision (empty checkboxes for Jesse), Apply Log (empty, filled in after Jesse acts).
7. Update the idea-seed: `status: researched`, add `related: [[<new review note>]]`.
8. Run `python tools/vault_lint.py` (use `py -3` if `python` is not on PATH); it must report **0 errors** before committing. Fix any error the run introduced — warnings are acceptable. Do **not** append a run summary to `change-log.md`: per the 2026-07-05 narrowing rule, `change-log.md` is decisions-only and the run record lives in the commit message and git log.
9. Commit and push: `git add` only this run's touched paths (the review note and the idea-seed file), commit message `vault-idea-research: <YYYY-MM-DD> — researched <slug>` (or `— gated <slug>` when the run only closed gates), push to `origin`. **This `vault-idea-research:` subject prefix is the loop's heartbeat.** Because the loop only commits when a seed exists (empty-queue nights are silent no-ops), `tools/vault_health.py` tracks it at a monitoring cadence of 30 days, not the nightly run cadence — a FAIL means the scheduler died or the seed queue has been empty for 60+ days, not that one night was missed. Keep the prefix exact.

## Allowed Without Additional Approval

| Action | Limits |
|---|---|
| Read any vault note, skill file, or the web | Read-only. |
| Create one review note per run in `06-reviews/` | Must use the standard template; must cite sources. |
| Update the processed idea-seed's `status` and `related:` frontmatter | Frontmatter only; never rewrite its body. |
| Set a seed to `status: gated` and add its `revisit-trigger:` | Only when the seed's own stated gate is verified shut **from files**. Frontmatter only. Never invent a gate the seed does not state, and never gate a seed to avoid hard research. |
| Run `tools/vault_lint.py` before committing | Pre-commit gate; must be 0 errors. Read-only check. |
| Commit and push this run's touched paths | Per Loop Steps step 9. The commit message is the run record — no `change-log.md` entry (decisions-only since 2026-07-05). |

## Blocked Without Specific Approval

| Action | Reason |
|---|---|
| Building, implementing, or scaffolding the idea itself | This loop investigates; it does not execute. That's a separate, explicitly-approved session. |
| Editing any skill file under `~/.claude/skills/` | Skills are out of this loop's scope entirely. |
| Writing to `02-facilities/`, `04-knowledge/` canonical content, pricing, SOP, safety, or field-execution content | Owned by [[vault-agent-loop-spec]]. |
| Processing more than one idea-seed per run | Keeps each run small and reviewable. |
| Deleting or archiving an idea-seed | *This* loop never removes one — even a "dead" idea stays as a record. Not a vault-wide statement: the capture loop's Terminal-Note Sweep archives seeds at a terminal status, and deliberately protects `unexplored`, `researched` and `gated` from it. See the seed lifecycle below. |
| Converting this loop's schedule to more frequent than nightly | Bounded cadence keeps token cost predictable on a constrained plan. |

## Seed Lifecycle — who moves a seed, and when

Added 2026-07-29. Three actors touch an idea-seed and none of them may skip a step, so the whole path is written in one place:

`unexplored` → *(this loop researches, or closes a shut gate)* → `researched` **or** `gated` → *(Jesse decides)* → a terminal status → *(capture loop's Terminal-Note Sweep archives it)*

The load-bearing part is the middle. `researched` means the research is done and **the decision is not** — the sweep's allowlist deliberately excludes it, so a researched seed sits in `00-inbox/` until Jesse acts. That is the intended pressure: an un-decided seed stays visible. `gated` is likewise excluded and additionally carries a `revisit-trigger:`, which puts it on the health dashboard's dormant-trigger registry. Neither status is a resting place the system will quietly clean up, and neither should be set to make a seed go away.

## Stop Conditions

Stop and report instead of continuing when: no unexplored idea-seeds exist (report the no-op, this is success, not failure); the idea-seed's subject is operational rather than speculative (defer to the Agent Loop); research is genuinely inconclusive after a reasonable search (write the review note anyway, mark Interpretation as "inconclusive," let Jesse decide whether it's worth a deeper one-shot investigation); git working-tree state is ambiguous.

## Success Criteria

A successful run either produces one well-evidenced review note that lets Jesse make a fast decision without re-deriving the research himself, or cleanly reports there was nothing to do. Both are success. Silently skipping a seed, researching more than one seed in a run, or writing a recommendation that reads as a decision rather than a proposal are failures.
