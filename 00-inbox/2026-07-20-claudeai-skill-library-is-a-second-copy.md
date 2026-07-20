---
type: capture
status: inbox
created: 2026-07-20
related:
  - [[knowledge-system-governance]]
  - [[vault-skill-drift-loop-spec]]
tags: [capture, vault-system, claude-code, skills, drift]
---

# The claude.ai skill library is a second copy the Skill-Drift Loop can't reach

Surfaced while rewriting the Claude chat / Cowork custom instructions on 2026-07-20. `usadebusk-core` is confirmed active in the claude.ai skill library (Settings > Capabilities, or Customize > Skills). That library is a **separate upload**, not a view onto `~/.claude/skills/` — there is no sync mechanism in either direction.

Which means skill content now lives in two disconnected places:

- `~/.claude/skills/usadebusk-*` — the config repo, maintained, version-controlled, and the target of the monthly Skill-Drift Loop.
- The claude.ai library — a frozen copy of whatever was uploaded, whenever it was uploaded. Nothing updates it.

## Why this matters

The Skill-Drift Loop exists to keep skill content true. The 2026-07-18 run alone corrected seven domain facts — operating pressure range, hourly-vs-day-rate labor billing, filter-press pumping being pigging-only, FHR = Flint Hills Resources, HR = "Hell Raiser." Every one of those corrections landed in the config repo copy. If the claude.ai upload predates them, the chat/Cowork surface is still answering from the wrong values, and the loop reports success.

The exposure is worse on that surface, not better. Cloud Cowork sessions have no vault access at all (desktop sessions run locally and can reach `C:\Users\Jwuts\obsidian-work`; cloud sessions cannot), so there is nothing to check the skill against. A stale skill in Claude Code gets caught when the vault file disagrees. A stale skill in cloud Cowork just sounds fluent.

## Open question

Which copy is canonical, and what re-uploads the claude.ai one after a drift run. Three shapes, none evaluated:

- Add a re-upload step to the Skill-Drift Loop's follow-through — manual, but the loop is already on-demand, so it costs one action a month.
- Treat claude.ai as deliberately thin: upload only `usadebusk-core` and accept it as a domain-vocabulary layer, never a source of numbers. The profile instructions already carry a guard along these lines ("the skill carries domain knowledge, not my vault contents — don't state specifics that would have to come from vault files").
- Don't upload skills to claude.ai at all, and let chat/Cowork run on profile instructions alone.

The second is closest to what's live now and needs no new machinery. Worth confirming the guard actually holds before relying on it.

## Check first

Nobody has verified how stale the uploaded copy is. Before designing anything, diff the claude.ai `usadebusk-core` against `~/.claude/skills/usadebusk-core/SKILL.md` — if the upload postdates 2026-07-18, this is theoretical and the note can be closed.
