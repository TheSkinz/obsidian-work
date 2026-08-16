#!/usr/bin/env python3
"""config_frontmatter_lint.py — does every config file's frontmatter actually parse?

Step 3 of the baseline staleness detector approved 2026-08-01, built 2026-08-16.

WHY THIS EXISTS. usadebusk-fieldpm carried `disable-model-invocation: true` and it
did nothing for three weeks. Its `description:` was unquoted and contained ": ", so
the whole frontmatter block failed to parse, the flag was silently ignored, and the
skill registered by H1-title fallback instead. Nothing reported an error. The skill
simply behaved as though the field was not there.

That is the shape of the bug this catches: NOT a wrong value, but a file the parser
gives up on while the tool around it carries on with a silent default. Claude Code
does not validate skill frontmatter — it ignores what it cannot read.

SCOPE — TWO TREES, NOT ONE. The 2026-08-01 seed scoped this to `skills/*/SKILL.md`.
Running it found the same defect in the regression battery: FIVE of the six
`regression/frozen/*.md` fixtures do not parse as YAML either, for exactly the same
reason (unquoted prose values containing ": "). That is latent rather than live —
nothing parses those files as YAML today, the replay guard reads staged paths
instead — but it is a trap laid directly under any tool that tries, which is why
tools/baseline_staleness.py deliberately uses a flat line parser instead.

PRIOR ART, NOT INSTALLED. `agnix` (github.com/agent-sh/agnix) is a real linter for
exactly this problem and carries 447 rules across CLAUDE.md, SKILL.md, hooks and MCP
— far more than this script. It was written after a skill named `Review-Code` never
triggered because the spec requires kebab-case. It is the better tool for the skills
half and is worth adopting, but installing a third-party package that reads the whole
config tree is a decision for Jesse, not an unattended one. This script is the
dependency-free floor, and it covers the frozen fixtures agnix would not know about.

Usage:
    python tools/config_frontmatter_lint.py           report
    python tools/config_frontmatter_lint.py --strict  exit 1 on any finding

Windows: `py tools/config_frontmatter_lint.py`.

Exit 0 clean (or findings without --strict), 1 findings under --strict, 2 nothing
judged (config repo absent).
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

try:
    import yaml  # ground truth: the same parser the harness uses
    HAVE_YAML = True
except ImportError:  # pragma: no cover - depends on the machine
    HAVE_YAML = False

KEBAB_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
FLAT_KEY_RE = re.compile(r"^([A-Za-z0-9_-]+):\s*(.*)$")

# Fields whose silent loss changes behaviour rather than cosmetics.
LOAD_BEARING = ("name", "description", "disable-model-invocation", "status")


def split_frontmatter(text: str) -> str | None:
    """Return the raw frontmatter block, or None if the file has no fence."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None
    out = []
    for line in lines[1:]:
        if line.strip() == "---":
            return "\n".join(out)
        out.append(line)
    return None  # unterminated fence is itself a defect, reported by the caller


def flat_keys(block: str) -> set[str]:
    """Top-level keys a naive line parser would see — the fallback's view."""
    return {m.group(1) for line in block.splitlines()
            if (m := FLAT_KEY_RE.match(line))}


def check(path: Path, kind: str) -> list[str]:
    text = path.read_text(encoding="utf-8")
    block = split_frontmatter(text)
    if block is None:
        return ["no frontmatter fence, or the fence is never closed"]

    findings: list[str] = []
    parsed = None
    if HAVE_YAML:
        try:
            parsed = yaml.safe_load(block)
        except Exception as e:
            first = str(e).splitlines()[0]
            return [f"frontmatter DOES NOT PARSE as YAML ({type(e).__name__}: {first}) — "
                    f"every field in this block is silently ignored by any YAML reader"]
        if not isinstance(parsed, dict):
            return [f"frontmatter parses to {type(parsed).__name__}, not a mapping"]

    # A key the line parser sees but YAML does not means the value swallowed it —
    # the field looks present in the file and is absent to the program.
    if parsed is not None:
        swallowed = flat_keys(block) - set(parsed.keys())
        for key in sorted(swallowed):
            if key in LOAD_BEARING:
                findings.append(f"`{key}:` is present in the text but NOT in the parsed "
                                f"mapping — swallowed by a preceding multi-line value")

    if kind != "skill" or parsed is None:
        return findings

    name = parsed.get("name")
    if not name:
        findings.append("no `name:` — the skill registers by H1-title fallback instead")
    else:
        if not KEBAB_RE.match(str(name)):
            findings.append(f"`name: {name}` is not kebab-case — the Agent Skills spec "
                            f"requires it and a non-conforming skill never auto-triggers")
        if str(name) != path.parent.name:
            findings.append(f"`name: {name}` does not match its directory "
                            f"`{path.parent.name}`")
    desc = parsed.get("description")
    if not desc or not str(desc).strip():
        findings.append("no `description:` — nothing for the model to trigger on")
    dmi = parsed.get("disable-model-invocation")
    if dmi is not None and not isinstance(dmi, bool):
        findings.append(f"`disable-model-invocation: {dmi!r}` is {type(dmi).__name__}, "
                        f"not a bool — a quoted 'true' is truthy to YAML but is not the "
                        f"flag the harness looks for")
    return findings


# The real regression, verbatim from claude-config ab40900^ — the unquoted
# description whose "(last active: USA26038" silently disabled the skill for three
# weeks. Kept as a fixture because a checker for this defect that has never been
# shown the defect is an assertion, not a test.
FIELDPM_PRE_FIX = """name: usadebusk-fieldpm
status: dormant
disable-model-invocation: true
description: Dormant — no active mobilization (last active: USA26038, HF Sinclair Navajo H19/H20, demobbed 2026-07-17). Live-job USADebusk field project management."""

FIELDPM_POST_FIX = """name: usadebusk-fieldpm
status: dormant
disable-model-invocation: true
description: "Dormant — no active mobilization (last active: USA26038, HF Sinclair Navajo H19/H20, demobbed 2026-07-17). Live-job USADebusk field project management." """


def self_test(tmp: Path) -> int:
    """Show the checker the bug it was written for, and its fix."""
    skill_dir = tmp / "skills" / "usadebusk-fieldpm"
    skill_dir.mkdir(parents=True, exist_ok=True)
    target = skill_dir / "SKILL.md"

    target.write_text(f"---\n{FIELDPM_PRE_FIX}\n---\n\n# Body\n", encoding="utf-8")
    findings = check(target, "skill")
    if not any("DOES NOT PARSE" in f for f in findings):
        print(f"SELF-TEST FAILED — the real fieldpm defect was not caught: {findings}")
        return 2

    target.write_text(f"---\n{FIELDPM_POST_FIX}\n---\n\n# Body\n", encoding="utf-8")
    findings = check(target, "skill")
    if findings:
        print(f"SELF-TEST FAILED — the FIXED fieldpm should be clean, got: {findings}")
        return 2

    # A non-kebab name must fire: the defect agnix was written for.
    bad = tmp / "skills" / "Review-Code"
    bad.mkdir(parents=True, exist_ok=True)
    (bad / "SKILL.md").write_text(
        "---\nname: Review-Code\ndescription: x\n---\n", encoding="utf-8")
    findings = check(bad / "SKILL.md", "skill")
    if not any("kebab-case" in f for f in findings):
        print(f"SELF-TEST FAILED — non-kebab name not caught: {findings}")
        return 2

    print("SELF-TEST PASSED — 3 cases: the real fieldpm defect, its fix, a non-kebab name.")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--strict", action="store_true", help="exit 1 when anything is found")
    ap.add_argument("--self-test", metavar="DIR", help="run the built-in cases in DIR and exit")
    args = ap.parse_args()

    if args.self_test:
        if not HAVE_YAML:
            print("SELF-TEST SKIPPED — PyYAML unavailable, nothing to prove")
            return 2
        return self_test(Path(args.self_test))

    config = Path.home() / ".claude"
    if not config.exists():
        print(f"[-] claude-config repo not present at {config} — nothing judged")
        return 2
    if not HAVE_YAML:
        print("[!] PyYAML unavailable — parse checking is skipped, only structural "
              "checks run. Install PyYAML for the real check.")

    # `scheduled-tasks/*/SKILL.md` added 2026-08-16 and it is not a nicety. The first
    # version globbed `skills/` only and reported all nine clean — while
    # scheduled-tasks/vault-consolidation-loop/SKILL.md sat with frontmatter that does
    # not parse, the exact fieldpm defect (unquoted "07/08/09: merge"), in a loop that
    # runs on a schedule. agnix found it because it walks the whole config tree; this
    # tool could not see it because of where it was pointed. A checker's blind spot is
    # its glob, and a clean report from a narrow glob reads identically to a clean tree.
    targets = [(p, "skill") for p in sorted(config.glob("skills/*/SKILL.md"))]
    targets += [(p, "skill") for p in sorted(config.glob("scheduled-tasks/*/SKILL.md"))]
    targets += [(p, "fixture") for p in sorted(config.glob("regression/frozen/*.md"))]

    total = 0
    for path, kind in targets:
        findings = check(path, kind)
        rel = path.relative_to(config).as_posix()
        if findings:
            total += len(findings)
            print(f"\n{rel}")
            for f in findings:
                print(f"  - {f}")

    print(f"\n{len(targets)} file(s) checked, {total} finding(s).")
    return 1 if (total and args.strict) else 0


if __name__ == "__main__":
    raise SystemExit(main())
