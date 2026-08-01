<!-- vault-loop: operational — config-repo + tools/ build owed; capture loop cannot write this content. -->
---
type: note
status: inbox
created: 2026-08-01
tags: [inbox, knowledge-system, regression, hooks, approved-unexecuted]
---

# Owed — baseline staleness detector for the regression battery

Approved by Jesse 2026-08-01 in the ordered form
([[2026-08-01-idea-research-baseline-staleness-detector]]). Decision closed, work
not started. The sibling convention idea
([[2026-07-31-idea-research-replay-ordering-discipline]]) was dropped in the same
ruling — do not revive it alongside this.

**Step 1 — prerequisite, do first.** Standardize the `skills:` frontmatter across
all six `~/.claude/regression/frozen/*.md` into a parseable `baseline_commits:`
field carrying `{repo, commit}` pairs, one per repo the fixture actually depends
on. This is not cleanup; the checker cannot be built on the current field. As
verified across all six files: F5 records a *date* rather than a hash, F1 names a
vault path with no hash at all, F4 alone carries both repos. Nothing parses the
prose today, so this is a mechanical six-file edit with no behavior change — and
it closes the F1/F6 vault-coverage gap and the F5 date gap in one pass.

**Step 2 — the checker.** A Python script under the vault's `tools/`, matching the
`vault_lint.py` / `vault_health.py` convention: for each frozen file read
`baseline_commits:`, run `git log <commit>..HEAD -- <paths the fixture loads>`
against the matching repo, and report any fixture with commits behind it. Surface
as a row on `50-dashboards/health.md`; run it when `vault_health.py` runs, not on
every config commit.

**Report any commit behind the baseline — do not classify substantive vs cosmetic.**
The regression README states outright, from the 2026-07-28 sweep: do not estimate
staleness from a commit's subject line. Matches the existing replay guard's
"ALL fixtures, not ANY" bias toward sensitivity over precision.

**Step 3 — independent, can go first if a quick win is wanted.** A YAML-parse sweep
of `skills/*/SKILL.md` flagging any file whose frontmatter fails to parse or
silently drops a known field (`disable-model-invocation`, `status`, `description`)
— the failure mode that hid for three weeks in `usadebusk-fieldpm`. Spend two
minutes on the Agnix lead first (HN "Show HN: Agnix – lint your AI agent configs";
the research fetch got HTTP 429 and never confirmed it). Build bespoke only if it
doesn't fit — the seed estimates ~10 lines.

Placement note: `tools/`, not a hook. A PreToolUse hook fires at commit time on
what's staged; this is a periodic pull sweep across two repos' history.
