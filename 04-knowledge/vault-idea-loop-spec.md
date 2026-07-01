---
type: governance
status: active
source_authority: primary
confidence: high
created: 2026-06-30
last_reviewed: 2026-06-30
review_after: 2026-09-30
related:
  - [[vault-capture-loop-spec]]
  - [[vault-agent-loop-spec]]
  - [[knowledge-system-governance]]
tags: [knowledge-system, agent-loop, idea-research, governance]
---

# Vault Idea Research Loop Spec

The third loop, distinct from the other two in kind rather than just scope. [[vault-capture-loop-spec]] files and harvests; [[vault-agent-loop-spec]] reviews the operational core. This loop does neither — it investigates. It picks one speculative idea-seed, does bounded web research on it, and reports findings back for Jesse to decide on. It never files, never harvests, never touches operational content, and never decides or implements anything itself.

Origin: a recurring pattern where ideas discussed in chat got dismissed as low-ROI or infeasible from priors, only for later research to find a power-user had already solved the same problem with an off-the-shelf tool or technique. This loop is the direct fix — it spends bounded, otherwise-idle overnight capacity checking "has someone already solved this" before Jesse spends a session re-deriving the answer from scratch.

## Loop Name

Vault Idea Research Loop

## Trigger

Scheduled nightly at 2:00 AM local via the `mcp__scheduled-tasks` mechanism (task id `vault-idea-research-loop`). Runs while the Claude Code app is active; if the app is closed at trigger time, it runs on next launch — same degraded-but-not-lost behavior as [[vault-capture-loop-spec]].

This loop only needs git-tracked vault content and web search, so unlike the Capture Loop it has no dependency on local session transcripts. It could in principle run as a fully desktop-independent cloud routine, but that mechanism was checked during this loop's design and found unavailable in this environment (the relevant remote-environment service returned 404 on every call). Local scheduling is deliberately the fallback, not a compromise — revisit if cloud routines become available.

## Scope

Reads:

- `00-inbox/*.md` files with frontmatter `type: idea-seed` — the only input queue this loop watches.

Writes:

- One new review note per run in `06-insights/`, using the standard review-note pattern (see [[vault-agent-loop-spec]] Output Artifact Requirements) with `review_type: idea-research`.
- The source idea-seed note: flips `status: unexplored` to `status: researched` and adds a `related:` link to the new review note. No other edit to the idea-seed's content.

Never touches `02-facilities/`, `04-knowledge/` canonical content (other than its own spec file, which it does not self-edit), pricing, SOPs, skills, or any operational content. If an idea-seed's subject turns out to be operational rather than speculative, this loop stops and defers to [[vault-agent-loop-spec]] instead of researching it.

## Ceremony Level

Low, but not silent. Every run either produces one evidence-gathering artifact (a review note, never a canonical change) or cleanly no-ops. Nothing this loop writes is a decision — the Decision checklist in the review note is Jesse's, not the loop's, exactly as in the Agent Loop pattern.

## Loop Steps

1. Scan `00-inbox/` for files with `type: idea-seed` and `status: unexplored`. If none exist, report a clean no-op and stop — do not manufacture work.
2. Pick the oldest unexplored idea-seed (by `created` frontmatter date). Process exactly one per run — same one-item discipline as [[vault-agent-loop-spec]]'s Selection Rule.
3. Read the seed's "Tentative read" and "To explore" sections as the research brief.
4. Research: web search for prior art, existing tools, or power-user solutions to the problem the idea describes. Also check what's already built in this vault (`04-knowledge/`, `06-insights/`) and in the deployed skills (`~/.claude/skills/`) that might already cover the idea, partially or fully — many ideas turn out to be already-solved or already-partially-built, and that's a valid, valuable finding.
5. Write a review note in `06-insights/` (filename pattern `YYYY-MM-DD-idea-research-<slug>.md`) using the standard template: Trigger (why this seed was picked), Evidence (sources found, with links), Interpretation (sound / trap / premature / already covered, and why), Recommended Action (build now / bounded one-shot investigation / park / drop), Decision (empty checkboxes for Jesse), Apply Log (empty, filled in after Jesse acts).
6. Update the idea-seed: `status: researched`, add `related: [[<new review note>]]`.
7. Append one dated run summary to `change-log.md` (append-only; trigger label "Vault Idea Research Loop").
8. Commit and push: `git add` only this run's touched paths (the review note, the idea-seed file, `change-log.md`), commit message `vault-idea-research: <YYYY-MM-DD> — researched <slug>`, push to `origin`.

## Allowed Without Additional Approval

| Action | Limits |
|---|---|
| Read any vault note, skill file, or the web | Read-only. |
| Create one review note per run in `06-insights/` | Must use the standard template; must cite sources. |
| Update the processed idea-seed's `status` and `related:` frontmatter | Frontmatter only; never rewrite its body. |
| Append to `change-log.md` | Dated run summary, append-only. |
| Commit and push this run's touched paths | Per Loop Steps step 8. |

## Blocked Without Specific Approval

| Action | Reason |
|---|---|
| Building, implementing, or scaffolding the idea itself | This loop investigates; it does not execute. That's a separate, explicitly-approved session. |
| Editing any skill file under `~/.claude/skills/` | Skills are out of this loop's scope entirely. |
| Writing to `02-facilities/`, `04-knowledge/` canonical content, pricing, SOP, safety, or field-execution content | Owned by [[vault-agent-loop-spec]]. |
| Processing more than one idea-seed per run | Keeps each run small and reviewable. |
| Deleting or archiving an idea-seed | Even a "dead" idea stays as a record; Jesse marks it, the loop doesn't remove it. |
| Converting this loop's schedule to more frequent than nightly | Bounded cadence keeps token cost predictable on a constrained plan. |

## Stop Conditions

Stop and report instead of continuing when: no unexplored idea-seeds exist (report the no-op, this is success, not failure); the idea-seed's subject is operational rather than speculative (defer to the Agent Loop); research is genuinely inconclusive after a reasonable search (write the review note anyway, mark Interpretation as "inconclusive," let Jesse decide whether it's worth a deeper one-shot investigation); git working-tree state is ambiguous.

## Success Criteria

A successful run either produces one well-evidenced review note that lets Jesse make a fast decision without re-deriving the research himself, or cleanly reports there was nothing to do. Both are success. Silently skipping a seed, researching more than one seed in a run, or writing a recommendation that reads as a decision rather than a proposal are failures.
