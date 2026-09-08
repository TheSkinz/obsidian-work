<!-- ROUTED 2026-07-30 — content landed in 07-llms/claude/code.md. Retained as the original capture record. -->
---
type: capture
status: inbox
created: 2026-07-29
related:
  - [[2026-07-19-auto-mode-permission-drift]]
tags: [capture, claude-code, permissions, security, hooks]
---

# exec-guard does not cover `gh api --method DELETE`

`~/.claude/hooks/usadebusk-exec-guard.mjs` (added 2026-07-29, config `529ba04`) gates `gh repo delete|create|edit|rename|archive|unarchive|set-default`. It does not gate `gh api`, which reaches the same destructive endpoints by another route — `gh api --method DELETE /repos/TheSkinz/claude-config` does what `gh repo delete` does, and `gh api --method PATCH` can flip visibility.

Left out deliberately to keep the first version tight and avoid false positives on the read-only `gh api` calls that are ordinary research. Not a live exposure today: nothing in the current workflow drives the GitHub API directly, and the allow list has no `gh api` rule.

## The fix if it becomes relevant

One entry in the `RULES` array plus a matching pair of tests. Roughly:

```js
{
  name: 'gh api write method',
  re: /\bgh\s+api\b[^|;&]*?(?:--method|-X)\s+(?:POST|PUT|PATCH|DELETE)\b/i,
}
```

Tests should confirm a plain `gh api /repos/...` read stays allowed, since that is the common case and blocking it would be the friction that gets the whole guard disabled.

## Trigger

Revisit if GitHub API calls start appearing in normal work — an automation that opens issues or PRs, or any script driving `gh api` with a write method. Until then this is a documented gap, not a to-do.
