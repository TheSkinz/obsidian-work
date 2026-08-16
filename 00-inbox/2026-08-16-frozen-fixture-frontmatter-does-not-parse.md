<!-- vault-loop: operational — config-repo ruling owed on whether frozen baselines get edited; capture loop cannot write this content. -->

---
type: finding
status: open
created: 2026-08-16
related:
  - "[[2026-08-01-baseline-staleness-detector-owed]]"
  - "[[2026-08-01-idea-research-baseline-staleness-detector]]"
tags: [finding, regression, knowledge-system, config-repo, awaiting-decision]
---

# Five of six frozen fixtures have frontmatter that does not parse

Found 2026-08-16 while building the baseline staleness detector (Step 3 of the
2026-08-01 approval). **Nothing was changed in any frozen file beyond the additive
`baseline_commits:` field** — whether to fix this is a ruling, not a sweep.

## What was found

`~/.claude/regression/frozen/*.md` — f1, f2, f3, f4 and f6 all fail a YAML parse
outright. Only f5 parses. The cause is identical in every case and identical to the
defect that silently disabled `usadebusk-fieldpm` for three weeks: an unquoted value
containing `": "`, which YAML reads as a nested mapping and then gives up on the whole
block.

```
f1  ScannerError: mapping values are not allowed here
f2  ScannerError    f3  ScannerError    f4  ScannerError    f6  ScannerError
f5  OK
```

Reproduce with `python tools/config_frontmatter_lint.py`.

## Why it has not bitten yet, and why that is not reassuring

It is **latent, not live**. Nothing parses those files as YAML today — the replay guard
(`usadebusk-fixture-replay-guard.mjs`) reads skills and fixtures off staged file paths,
not off frontmatter, so it never touches the block. The battery works.

What makes it worth a ruling is that it is a trap laid directly under the next tool that
tries. It caught me building one: `tools/baseline_staleness.py` was specified to read a
`baseline_commits:` field out of these files, and had I reached for `yaml.safe_load` —
the obvious choice — it would have returned nothing for five of six fixtures and
reported them all clean. A staleness checker that silently sees no baselines is worse
than no checker, because it produces a green row. The tool now uses the vault's flat
line parser instead, and the frozen files are the reason.

The same shape is what `usadebusk-fieldpm` did: the field was there, the file looked
right, and the program behaved as though the field did not exist. Nothing errored.

## The call

**A — leave them.** They are frozen baselines; the record is the point, and editing them
to satisfy a parser nobody runs is churn. Cost: the trap stays for the next tool author,
who has to already know.

**B — quote the offending values.** Mechanical, five files, no semantic change: wrap the
prose values in quotes exactly as `ab40900` did for fieldpm. Cost: it edits frozen files,
which the regression discipline treats as near-immutable, and it touches five baselines
at once for a defect that is currently harming nothing.

**C — leave them and make the constraint explicit.** Do nothing to the files, but state
in `regression/README.md` that frozen frontmatter is prose-shaped and must be read with a
line parser, never a YAML one. Cheapest, and it converts a trap into a documented rule —
but it is a comment, and comments are not enforcement.

`tools/config_frontmatter_lint.py` detects the condition whichever way this goes; it is
not wired into `health.md` on purpose, pending this ruling.

## Adjacent question, still OPEN: adopt agnix?

> **Trialled 2026-08-16, decision NOT yet made.** Installed globally at `0.49.0` and run
> once against `~/.claude`. It was briefly uninstalled — **that was a misclick, not a
> ruling** — and has been restored, pinned to the same version.
>
> **One thing the trial did settle:** it does not replace `config_frontmatter_lint.py`.
> It scanned `regression/` and flagged run logs for portability, but reported nothing
> about the five frozen fixtures failing to parse — non-`SKILL.md` markdown appears to be
> treated as generic prose, so the AS rules never apply and `AS-016` never fires. The two
> tools are complements, not alternatives.
>
> **Still unknown, and it is the number the decision turns on:** the run reported 16
> errors that were never read — the output scrolled. Everything assessed so far is from
> the warnings. Three genuine findings are captured at
> [[2026-08-16-three-config-findings-from-the-agnix-trial]].
>
> The section below is the pre-trial assessment, kept as written.

## Adjacent, and also Jesse's call: adopt agnix?

`agnix` (`github.com/agent-sh/agnix`) is a real linter for exactly this class of problem —
447 rules across `CLAUDE.md`, `AGENTS.md`, `SKILL.md`, hooks and MCP, with autofixes and
an LSP for VS Code / Neovim / JetBrains / Zed. It exists because a skill named
`Review-Code` never triggered: the Agent Skills spec requires kebab-case and Claude Code
does not validate it, it just silently ignores the skill. That is our failure mode,
described by a stranger.

It is materially better than `config_frontmatter_lint.py` for the skills half. It was
**not installed** — pulling a third-party package that reads the whole config tree is a
decision, and this ran unattended. Two things to weigh: it would not know to check
`regression/frozen/`, which is where the actual findings are; and the 2026-08-01 seed
that authorized this work said to check the agnix lead first and build bespoke only if it
did not fit, which is what happened, so the bespoke floor exists either way.

**Decays:** no. Nothing is broken today and nothing degrades while this sits.
