<!-- vault-loop: operational — governance decision on vault-capture-loop-spec.md's Terminal-Note Sweep status rule (04-knowledge scope). Defers to the on-demand Agent-Review loop; capture loop cannot write this content. -->
---
type: note
status: inbox
created: 2026-07-29
tags: [inbox, vault-system, capture-loop, sweep, open-question]
---

# A note with no `status` field can never be swept, however finished it is

Loose end from the 2026-07-29 loop-spec audits. The Terminal-Note Sweep was extended that day
from `type: idea-seed` to all types, and correctly keys on `status` — a parser that sees no
status must skip, never sweep. That rule is right. It also means a finished note that simply
never got a `status` field is invisible to the sweep permanently, and nothing else will ever
move it.

Four inbox notes currently carry no `status` field at all:

| Note | Type | Markers | Live? |
|---|---|---|---|
| `2026-07-12-github-skill-discovery-pipeline-declined.md` | note | `ROUTED 2026-07-20` | **No** — content landed in `07-llms/self-improving-systems.md`, retained as the origin record |
| `2026-07-07-harness-audit-open-items.md` | session-note | prestaged-skipped, defer | **Partly** — pre-staging marked it "already covered", but it was never given a terminal status |
| `2026-07-29-build-workup-quotation-regression-check.md` | note | — | Yes, a live build task |
| `2026-07-29-syncrude-6-ft-hr-fill-flush-question.md` | note | — | Yes, a live open question |

So the population splits cleanly: two are done and stuck, two are live and correctly staying.

## The question

Should a marker be allowed to stand in for a status? Specifically, is a note carrying
`<!-- ROUTED … -->` or `<!-- vault-prestaged: skipped — already covered … -->` sweepable without
a terminal `status:`?

**Argument for:** both markers are written by a loop that has already concluded the note is
finished, and the ROUTED marker even names where the content went. Requiring a second,
redundant signal is what leaves these stranded.

**Argument against:** the markers mean different things. `ROUTED` asserts the content was
filed elsewhere. `prestaged: skipped — already covered` asserts only that *pre-staging* had
nothing to add, which is not the same as Jesse being done with it — the harness-audit note is
exactly that ambiguous case, and its own body still lists open items. Treating them alike
would sweep a note whose author never said it was finished, which is the failure the
status-only rule exists to prevent.

**Cheaper alternative:** don't extend the sweep at all. Backfill `status:` on the two finished
notes by hand (a two-minute fix), and treat a statusless note as the lint gap it is — the
capture loop already normalizes frontmatter to schema under Lane 1, so it could add
`status: inbox` to any note missing one, which makes every note sweep-eligible in principle and
leaves the terminal decision where it belongs.

Leaning to the alternative: it fixes the class rather than the instances, and it keeps the
sweep's one input signal unambiguous. See [[vault-capture-loop-spec]].

## Instances closed 2026-08-15, class question still open

The retirement sweep gave all four notes a status, so the instance half of this note is done:
`2026-07-12-github-skill-discovery-pipeline-declined` → `complete`,
`2026-07-07-harness-audit-open-items` → `resolved` (both its items verified closed, not assumed),
`2026-07-29-build-workup-quotation-regression-check` → `resolved` (DQ-011),
`2026-07-29-syncrude-6-ft-hr-fill-flush-question` → `superseded` (DQ-012).

Two of them had been stuck for five weeks, which is the cost this note predicted. The table above
called two "live" — both have since closed through the decision queue, so the split it recorded was
a snapshot, not a stable property.

**What is still open is only the class fix**, and the sweep is evidence for it rather than against:
hand-backfilling worked, but it took a dedicated session to notice, and nothing prevents the next
statusless note from sitting just as long. The recommendation stands — have the capture loop
normalize any note missing `status:` to `status: inbox` under its existing Lane 1 frontmatter
authority, which makes every note sweep-eligible in principle and leaves the terminal decision where
it belongs. The sweep-extension option should be considered dead: this session's four cases show the
markers mean genuinely different things, exactly as the argument-against predicted.
