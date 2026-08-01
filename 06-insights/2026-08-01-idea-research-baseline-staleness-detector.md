---
type: review
status: resolved
review_type: idea-research
source_authority: primary
confidence: high
created: 2026-08-01
review_after: 2026-09-01
related:
  - "[[idea-baseline-staleness-detector]]"
  - "[[2026-07-31-idea-research-replay-ordering-discipline]]"
tags: [review, knowledge-system, idea-research, regression, hooks]
---

# Idea Research — Baseline Staleness Detector for the Regression Battery

## Trigger

Scheduled nightly run of the Vault Idea Research Loop, 2026-08-01. Oldest `unexplored`
idea-seed by `created` date: `idea-baseline-staleness-detector` (2026-07-28), ahead of
`idea-business-normal-register` (2026-07-29) and `idea-rig-layout-diagram` (2026-07-30).

**Gate check.** The seed's `**Gate:**` line reads "None — researchable now." No hidden
gate found in the "To explore" prose either. Proceeded to research (case b).

## Evidence

**1. The seed's own sibling was already researched yesterday and explicitly recommends
building this one.** `06-insights/2026-07-31-idea-research-replay-ordering-discipline.md`
compared a discipline-based alternative (co-commit the replay and the rule) against this
seed's mechanical design (record a config-commit reference, check by `git log
<commit>..HEAD`) and concluded the mechanical approach is "ordering-immune by
construction" and cited external prior art for the same pattern in prompt-drift
detection. Its Recommended Action names this seed directly: "pursue... through
`idea-baseline-staleness-detector` instead, which already specifies the mechanism in
more actionable detail." That conclusion is reaffirmed here, with one load-bearing
correction below.

**2. The mechanism assumes a machine-parseable `skills:` frontmatter field. It doesn't
exist yet — verified against all six live frozen files, not inferred.** Read
`~/.claude/regression/frozen/*.md` directly:

| Fixture | `skills:` line as written today |
|---|---|
| F1 | `(claude-config @ 71efec5)` + prose: "Later commits d17d293 and 4ec2d76 touched only vault-ingest and fieldpm... baseline is current" — vault path named, **no vault commit hash** |
| F2 | `(claude-config @ f20db13)` |
| F3 | `(claude-config @ 4ec2d76 — current HEAD as of 2026-07-28)` |
| F4 | `(claude-config @ 396d8b2, vault @ ba06c1c)` — the one fixture with both hashes |
| F5 | `(claude-config @ 2026-07-28, ...)` — **a date, not a commit hash** |
| F6 | `(claude-config @ ab40900 + the shift-landing diagnostic patch committed with this promotion)` |

The field is free prose written per-fixture by whoever promoted it, not a structured
value. Confirmed with `grep -rl "frozen/" --include="*.py" --include="*.mjs" ~/.claude`
that nothing parses it programmatically today — the README's own instruction is "always
read the `model:` and `skills:` frontmatter... of the specific file," i.e. a human does
this by eye. The seed's plan — "parse its `skills:` line for the config commit it was
cut at, run `git log <commit>..HEAD`" — is correct in spirit but would be parsing
inconsistent prose, and F5 has no commit to parse at all (it recorded a date, which is
exactly the ordering-blind signal `hooks/usadebusk-fixture-replay-guard.mjs`'s own
"KNOWN LIMITATION" comment names as the problem this whole line of work exists to
avoid). This is a **prerequisite gap**, not a detail: the mechanical checker cannot be
built directly on top of the current field as-is.

**3. The seed's own open question about vault-side coverage is answered by the same
evidence, not left open.** The seed asks whether "the same mechanism should cover the
vault-side dependency too, since F4 also reads
`04-knowledge/sops/sop-formatting-standard.md` and F1/F6 read the actuals rollup, so a
skills-only check would miss a class of drift." The format already *sometimes* carries
a vault hash (F4's `vault @ ba06c1c`) — the convention exists, it's just not applied
consistently (F1 names the vault path with no hash). Standardizing the field once
closes both gaps in the same pass rather than needing a second mechanism.

**4. Part two of the seed (a YAML-parse sweep of `skills/*/SKILL.md`) has no existing
tool in this environment.** Searched `~/.claude` for any script already doing this —
none found. Web search surfaced `yamllint` (generic YAML linter, would need a wrapper to
check specifically for the silent-field-drop failure mode this vault already hit with
`usadebusk-fieldpm`'s unquoted `description:`) and an unverified lead, a Hacker News post
titled "Show HN: Agnix – lint your AI agent configs (Claude.md, skills, MCP, hooks)"
which by its title looks like it may cover exactly this — but the fetch to read it
returned HTTP 429 and could not be confirmed before this run's research budget closed.
**This is a real, unverified lead, not a finding** — worth a two-minute check before
building a bespoke sweep from scratch, but not worth blocking on for this note. Given the
sweep is ~10 lines per the seed's own estimate and the vault already has the
`vault_lint.py` pattern to copy, building it directly is also reasonable regardless of
what Agnix turns out to be.

## Interpretation

**Sound overall, but the seed as literally specified would fail on contact with the
real data — trap avoided only because this research checked the actual files instead of
trusting the seed's description of them.** The seed says "the fixture-to-skill map
already exists... nothing new needs inventing," which is true for the map
(`SKILL_FIXTURES` in the replay guard) but not true for the commit reference — that part
needs inventing first, in the form of a standardized structured field. Once that one
prerequisite is done, the rest of the seed's design holds up: the fixture-to-skill map
is real and already cross-checked against the README table by the replay guard's own
test suite, `git log <commit>..HEAD -- <path>` is a correct and ordering-immune
staleness check, and yesterday's sibling research independently validated the mechanical
approach over a discipline-based one using a real trial (the F1/F6 rebaseline) as
evidence.

On the seed's other to-explore questions: "whether substantive can be judged
mechanically" — no. The README states outright, from the 2026-07-28 sweep, "Do not
estimate staleness from a commit's subject line; check what the fixture actually loads,"
and the fixture-replay-guard's own design notes reject a similar substantive/cosmetic
classifier as unreliable (its `COSMETIC` regex is a narrow escape hatch, not a
classifier). The detector should report *any* commit behind the recorded baseline and
let a human or agent triage — consistent with the existing hook's own "ALL fixtures, not
ANY" philosophy of maximum sensitivity over precision.

On placement (`tools/` vs a hook): `tools/` fits better than a new hook. A PreToolUse
hook only fires at commit time on whatever's being staged right now, which is what the
existing fixture-replay-guard already does for the forgot-to-replay case. This detector
is a different shape — a periodic pull-based sweep across all six fixtures regardless of
what's currently staged, reading git log in two repos (claude-config and vault) and
writing a row to `50-dashboards/health.md`. That's the same shape as `vault_health.py`
itself, which already lives in `tools/` for exactly this reason.

## Recommended Action

**Bounded one-shot build, done in this order, not "build now" as a single undifferentiated
task:**

1. Standardize the `skills:` frontmatter across all six `frozen/*.md` files into a
   parseable form — e.g. a `baseline_commits:` field listing `{repo: claude-config,
   commit: <hash>}` / `{repo: vault, commit: <hash>}` pairs, one per repo the fixture's
   prompt actually depends on. Mechanical edit, six files, no behavior change (nothing
   parses the old prose today, confirmed above). This closes both the F1/F6 vault-gap
   question and the F5 date-instead-of-hash gap in the same pass.
2. Write the checker as `tools/`-style script (Python, matching `vault_lint.py` /
   `vault_health.py` convention): for each frozen file, read its `baseline_commits:`,
   run `git log <commit>..HEAD -- <paths the fixture's skills map say it loads>` against
   the matching repo, report any fixture with nonzero commits behind — no
   substantive/cosmetic filtering, per Interpretation above. Surface as a row on
   `50-dashboards/health.md`.
3. Separately (independent, can be done first if it's wanted as the quick win): a
   YAML-parse sweep of `skills/*/SKILL.md` flagging any file whose frontmatter fails to
   parse or silently drops a known field (`disable-model-invocation`, `status`,
   `description`) — the exact failure mode that hid for three weeks in
   `usadebusk-fieldpm`. Check the unverified Agnix lead first (two minutes); build
   bespoke only if it doesn't fit.

Cadence: run step 2's checker whenever `vault_health.py` runs, not on every config
commit — it's a pull check over two repos' full history, not a pre-commit gate, and the
existing PreToolUse hook already covers the pre-commit case for the common "forgot
entirely" failure mode.

## Decision

- [x] **Approved — build in the order above** (Jesse, 2026-08-01)
- [ ] ~~Approved with edits~~
- [ ] ~~Drop~~
- [ ] ~~Needs more source material (e.g. confirm/rule out Agnix first)~~

Ruled together with [[2026-07-31-idea-research-replay-ordering-discipline]], which was **dropped**
in the same pass — the mechanical check here supersedes the discipline-based convention, and only
one of the two was ever needed. That note's point 1 stands as the record of why: the F1/F6
rebaseline, the exact case the convention covered, still split into two commits under careful
manual execution.

**The order is load-bearing, not a suggestion.** Step 1 is a prerequisite, not a nicety — the
checker cannot be built on the `skills:` field as it exists today. Verified across all six live
frozen files: F5 records a date rather than a commit hash, F1 names a vault path with no hash, and
the field is free prose written per-fixture rather than a structured value. Nothing parses it
programmatically today, so standardizing it is a no-behavior-change edit.

The Agnix lead stays a two-minute check before step 3 only, not a gate on steps 1–2.

**Approved but unexecuted.** Filed as owed work at `00-inbox/2026-08-01-baseline-staleness-detector-owed.md`.
Steps 1 and 3 are config-repo changes (`~/.claude/regression/frozen/`, `~/.claude/skills/`); step 2
adds a script under the vault's `tools/`.

## Apply Log

| Date | Action | By | Notes |
|---|---|---|---|
| 2026-08-01 | Approved in the ordered three-step form; `status` → `resolved` | Claude | No build this session — the ruling closes the decision, not the work. Owed work filed to `00-inbox/2026-08-01-baseline-staleness-detector-owed.md`. Sibling note dropped in the same pass. Source seeds `00-inbox/idea-baseline-staleness-detector.md` and `00-inbox/2026-07-28-replay-ordering-discipline.md` both closed by this ruling. |
