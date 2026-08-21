<!-- ROUTED 2026-08-21 — content landed in 07-llms/claude/output-styles.md, including the watch condition and its trigger. Retained as the original capture record. -->
---
type: note
status: inbox
created: 2026-08-20
tags: [inbox, knowledge-system, output-style, config-repo, watch]
---

# Watch — does built-in Concise drop the named-task close?

Global `outputStyle` moved from the custom `Jesse Default` to Anthropic's
**built-in `Concise`** on 2026-08-20 (`~/.claude/settings.json`). `jesse-default.md`
is retained unmodified as the fallback.

**The open question.** The built-in ends with "Where these rules conflict with more
general communication or formatting guidance elsewhere in your instructions, these
rules win" — which nominally outranks the Output section of global `CLAUDE.md`.
Two gaps were identified:

1. The built-in permits bullets for "real structure"; `CLAUDE.md` bans them in prose.
   Cosmetic, accepted.
2. The built-in has **no equivalent of the close-with-the-outstanding-task rule** —
   the one output rule Jesse has confirmed actually matters (see the memory note
   `feedback-name-tasks-dont-gesture`; most other stated preferences he has called
   disposable).

**Why nothing was built.** The override clause fires only *where the rules conflict*,
and the built-in is **silent** on the closing rule rather than contradicting it.
Silence is not a conflict, so the `CLAUDE.md` rule stands unopposed. Building a
`jesse-concise.md` would have bought one cosmetic fix in exchange for maintaining a
local file against a first-party one Anthropic keeps updating. Deferred on
back-test-before-build grounds: watch the real behavior, don't pre-empt it.

**The trigger.** If responses under built-in Concise start ending without the
outstanding task named — gesturing ("a few open items") or just stopping — that is
the evidence. It is a ~10-minute job at that point: write
`~/.claude/output-styles/jesse-concise.md` carrying the built-in's six rules plus
the named-task close and the no-bullets-in-prose ban, and repoint `outputStyle`
at it.

**Name it anything but `Concise`.** A custom style sharing the built-in's name
shadows it. That already happened once this session: a stand-in `concise.md` was
written on the false premise that the built-in didn't exist, and it silently
loaded in place of the real one. Deleted.

Related: the version-check failure that caused the false premise is recorded in the
memory note `reference-tool-env-virtualized-filesystem` — my sandbox held a stale
`2.1.220` copy of the package while Jesse's real install was `2.1.238`.
