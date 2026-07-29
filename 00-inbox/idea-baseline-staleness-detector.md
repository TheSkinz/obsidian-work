---
type: idea-seed
status: unexplored
created: 2026-07-28
tags: [idea, vault-system, regression, future]
---

# Baseline staleness detector for the regression battery

Idea seed captured 2026-07-28 for a future exploration session. The read below is tentative — confirm intent with Jesse before designing.

**Tentative read:** The regression battery keeps going stale silently, and on 2026-07-28 every one
of the five fixtures swept turned out to be behind at least one un-replayed substantive skill
commit — including F4, which I had recommended doing last on the grounds it was only "a pointer
cleanup" and which was actually behind a content rule plus four `usadebusk-equipment` commits.
`hooks/usadebusk-fixture-replay-guard.mjs` catches the case where a skill ships and *nothing* is
replayed, but it structurally cannot catch the commoner case: a replay happened, and then a rule
landed after it. That gap has now bitten F1, F6, F2, F3 and F4. The fix is small — for each frozen
file, parse its `skills:` line for the config commit it was cut at, run
`git log <commit>..HEAD -- skills/<each skill that fixture loads>/SKILL.md`, and report any fixture
with un-replayed commits behind it. The fixture-to-skill map already exists in the replay guard and
in the README table, so nothing new needs inventing. Surface it as a row on
`50-dashboards/health.md` so it reaches Jesse without anyone remembering to look, which is the
whole point — he does not track triggers.

**Also worth folding into the same pass:** a YAML-parse sweep of `skills/*/SKILL.md`. On 2026-07-28
`usadebusk-fieldpm`'s frontmatter was found to have been failing to parse — an unquoted
`description:` containing `": "` — which silently discarded its `disable-model-invocation` flag,
its `status`, and its entire description for three weeks while the skill still appeared to work.
A malformed skill frontmatter fails silently and looks like a working skill. Ten lines, same class
of problem, same dashboard row.

**To explore:** Whether this belongs in `tools/` as a Python script alongside `vault_lint.py` and
`vault_health.py`, or as a second hook in `~/.claude/hooks/` next to the replay guard — the data
lives in the config repo but the dashboard lives in the vault, and that split is the main design
question. Whether "substantive" can be judged mechanically at all or whether the check should just
report *any* commit behind and let a human triage, given that this session's own attempt to judge
substantiveness from commit subject lines was wrong about F4. What the right cadence is — on every
config commit, daily, or only when the battery is about to be used. And whether the same mechanism
should cover the vault-side dependency too, since F4 also reads
`04-knowledge/sops/sop-formatting-standard.md` and F1/F6 read the actuals rollup, so a skills-only
check would miss a class of drift.

**Gate:** None — researchable now. The fixture table, the frozen frontmatter format and the git
history it needs all already exist.
