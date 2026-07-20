<!-- ROUTED 2026-07-20 — content landed in 07-llms/claude/code.md. Retained as the original capture record. -->
---
type: capture
status: inbox
created: 2026-07-19
related:
  - [[active-jobs]]
  - [[system-workflow-reference]]
tags: [capture, claude-code, skills, usadebusk-fieldpm, usa26038]
---

# usadebusk-fieldpm has never been invoked, including during a live job

Caught during the 2026-07-19 `/doctor` pass. The skill's usage counter is **zero lifetime** — it does not appear in `skillUsage` in `~/.claude.json` at all, and no `Skill` dispatch for it appears in the 50 most recent session transcripts (2026-07-01 to 2026-07-19).

Its description opens with `ACTIVE for USA26038 (HF Sinclair Navajo H19/H20, mobilized 2026-07-10) — re-dormant at demob`. That job has been mobilized nine days and the skill has not fired once.

Jesse's read at capture time: not used yet, but a use case has recently come up. So it stays. This note records the gap rather than proposing removal.

## Two possible explanations, unresolved

Either the field workflow genuinely is not running through Claude Code — shift logs, receipt extraction, and payroll emails happening by other means — or the skill is not triggering when it should. These have different fixes, and nothing in the doctor data distinguishes them. Worth one question the next time USA26038 work comes up: when you did shift-cycle work for this job, did you reach for `/extract` or `/log` and they did not fire, or did the thought not arise?

If the answer is the second, the trigger phrasing is fine and the workflow simply lives elsewhere — no action. If the first, the trigger list needs work.

## Cost, and a demob trigger

The description is **769 characters — the longest of any skill**, roughly 196 est. tokens resident in every session's skill listing regardless of project. That is the single most expensive entry in the listing, and the reason is the job-specific ACTIVE banner.

At USA26038 demob the banner goes stale, and a stale banner is worse than an absent one: it points a live-job routing hint at a finished job. Per `system-workflow-reference.md` the skill returns to dormant at demob — this is the reminder that the description text needs editing at the same time, not just the status. Trimming the banner back to a dormant one-liner recovers most of those 196 tokens.
