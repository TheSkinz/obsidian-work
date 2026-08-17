<!-- vault-loop: operational — config-repo/hooks/skills linting findings, awaiting adoption ruling on agnix. Capture loop cannot write this content. -->
---
type: finding
status: open
created: 2026-08-16
related:
  - "[[2026-08-16-frozen-fixture-frontmatter-does-not-parse]]"
tags: [finding, config-repo, hooks, skills, knowledge-system]
---

# Config findings from the agnix trial — one was a live defect

## 0. THE HEADLINE — a scheduled loop's SKILL.md did not parse, and my tool could not see it

**Found by agnix, verified independently, fixed the same session.**
`scheduled-tasks/vault-consolidation-loop/SKILL.md` carried an unquoted description —
`Monthly wiki-consolidation pass on 07/08/09: merge duplicates, …` — where `07/08/09: `
is a colon-space. The whole frontmatter block failed to parse. **This is the fieldpm
defect exactly**, in a loop that runs on a schedule, and it had been sitting there
undetected.

Like fieldpm, it was working by fallback — `health.md` showed the consolidation loop
firing normally on 2026-08-15 — so nothing was visibly broken. That is the entire danger
of this defect class: the symptom is not an error, it is a field that quietly means
nothing.

**The part worth keeping.** `tools/config_frontmatter_lint.py`, built this same morning
specifically to catch this defect, reported **all nine skills clean** — because its glob
was `skills/*/SKILL.md` and this file lives under `scheduled-tasks/`. The tool was
correct and useless at the same time. agnix caught it only because it walks the whole
config tree instead of a path someone chose in advance.

A checker's blind spot is its glob, and a clean report from a narrow glob is
indistinguishable from a clean tree. Scope extended to `scheduled-tasks/*/SKILL.md`
(20 files checked now, was 15), with the reason recorded in the code so the glob is not
quietly narrowed again.

---

# Three further findings from the same run

`agnix@0.49.0` was installed globally and run once against `~/.claude` (2026-08-16). Each
finding below was **verified locally** rather than taken from the tool's output — which
is the point: they hold whether or not agnix stays.

*Adoption is still undecided.* The tool was briefly uninstalled and restored — that was a
misclick, not a ruling. The open question lives at
[[2026-08-16-frozen-fixture-frontmatter-does-not-parse]].

## 1. `status: dormant` on usadebusk-fieldpm is an unrecognized field

Verified: it is the only `status:` across all nine skills. It parses cleanly, so this is
not the 2026-07 unparseable-frontmatter bug — but it is the same *family*. The field
reads as though it gates something and does nothing; the actual gate is
`disable-model-invocation: true`, and the description already opens with "Dormant".

Worth deciding rather than fixing blind: remove it as inert, or keep it as human-facing
documentation and accept that it is decorative. The reason it matters at all is that
`tools/config_frontmatter_lint.py` **cannot see this class** — it validates that fields
parse, never whether the harness recognizes them. That is a real gap in the tool built
today, and it is worth recording even though the linter that found it is gone.

## 2. All five PreToolUse Bash hooks specify no timeout

Verified against `settings.json` — `usadebusk-git-guard`, `usadebusk-staged-check`,
`usadebusk-word-delta`, `usadebusk-fixture-replay-guard` and `usadebusk-exec-guard` all
run with no `timeout` key.

Lower severity than it first reads: hooks carry a default timeout, so nothing runs
unbounded. But these five sit on the critical path of **every Bash call**, and the value
is currently inherited rather than chosen. Setting it explicitly is cheap and makes the
budget legible.

## 3. Two estimating scripts hardcode the OneDrive facilities root

`skills/usadebusk-estimating/scripts/backtest_workup.py:71` and
`scripts/presend_gate.py:50` both carry
`CANON = r"C:\Users\Jwuts\OneDrive\USADeBusk\Facilities"`.

**This is the finding with a track record.** DQ-015 records that `backtest_workup.py` was
*silently dead for the second time* — the cause being path assumptions breaking when the
facility tree gained a customer-group level and DSP26071.2 moved `Bids/ → Jobs/`. It was
fixed then by resolving cases by filename instead of hard-coded path, but the root
`CANON` constant survived. A generic linter with no knowledge of that history pointed
straight at the file that has broken twice.

Not urgent — the path is correct on this machine and the script is green at 3/3. Worth
noting that "correct on this machine" is exactly the state it was in both times before.

## What the trial settled about agnix itself

Recorded so the question is not re-opened from scratch. It scanned `regression/` and
flagged run logs for portability, but reported **nothing** about the five frozen fixtures
failing to parse — it appears to treat non-`SKILL.md` markdown as generic prose, so the
AS rule family never applies. It does not replace `tools/config_frontmatter_lint.py`;
the two are complements.

**The 16 errors, once read, were 1 real and 15 false.** The real one is finding 0 above.
The other 15 are a single rule misfiring: "Unclosed XML tag" against documentation
placeholders — `<slug>`, `<one>`, `<one line>`, `<YYYY-MM-DD>`, `<YYYY-MM>` — which appear
in loop runbooks and commit-message templates as fill-in-the-blank markers, not markup.
After the fix the count is 15 errors, all of that one class.

Noise profile on warnings: 73, of which well over half are hardcoded-path complaints
against `regression/runs/*.md` — historical records of what happened on a specific
machine, where "not portable" is true and irrelevant, the same class of finding that got
`change-log.md` exempted from DEAD-LINK the same day. The four `scheduled-tasks/*/SKILL.md`
path hits are the same shape: those are machine-specific launchers that *should* name the
absolute vault path. One confirmed false positive beyond the XML rule: an `$ARGUMENTS[n]`
finding against `usadebusk-estimating/SKILL.md`, which contains no `$ARGUMENTS` anywhere.

**Verdict shape.** Signal is roughly a dozen real findings in ~90, and one of them was a
live defect nothing else would have caught. That is a strong argument for keeping it and
a strong argument that it is unusable without an ignore config — both at once. The two
rules to suppress first are the XML-tag rule (100% false here) and hardcoded-path on
`regression/runs/` and `scheduled-tasks/`.

**Do not put it in a hook.** A v0 linter that invents an `$ARGUMENTS` finding, sitting on
the critical path of every Bash call, is how a session becomes unworkable. Manual or
loop-scheduled only. And `--fix-unsafe` stays away from `~/.claude`: all 16 fixable items
sit below the safe-confidence bar, and `--fix-safe` correctly applied nothing.
