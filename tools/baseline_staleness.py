#!/usr/bin/env python3
"""baseline_staleness.py — is any frozen regression baseline behind its inputs?

Pure standard library, matching the `vault_lint.py` / `vault_health.py`
convention. Reads `baseline_commits:` off each `~/.claude/regression/frozen/*.md`
and asks git, per repo, whether anything has landed on the paths that fixture
depends on since the baseline was cut.

WHY THIS EXISTS (2026-08-01 ruling, built 2026-08-16). Two baselines went stale
without anyone noticing:

  - F6 sat against a rig-in rule that had since been corrected, and surfaced only
    because a human replayed it by hand.
  - F1 had been over-billing a second crew truck through four promotions —
    2 x 48 = 96 truck-hours, a $720 over-quote on every replay.

This is the standing version of the check that caught the first and would have
shortened the second.

REPORT ANY COMMIT BEHIND. DO NOT CLASSIFY SUBSTANTIVE VS COSMETIC. The regression
README states this outright from the 2026-07-28 sweep: do not estimate staleness
from a commit's subject line. This tool prints subjects so a human can judge, and
takes no position itself. It matches the replay guard's "ALL fixtures, not ANY"
bias toward sensitivity over precision — a false alarm costs a glance, a missed
one costs a wrong number in a customer's quote.

BASE-GATED, LIKE POINTER-DEAD AND THE BID-FOLDER COLUMN. This script lives in the
vault but must read a second repo at ~/.claude. If that repo is absent — a
different machine, a fresh clone — the answer is `-` (nothing judged), never FAIL.
An absent repo and a current baseline must not look alike, but neither may an
absent repo look like a failure.

Usage:
    python tools/baseline_staleness.py           table to stdout
    python tools/baseline_staleness.py --verbose  list the commits behind

Windows: `py tools/baseline_staleness.py`.

Exit codes follow the pre-send gate's convention: 0 all current, 1 at least one
baseline behind, 2 could not judge (a repo missing, or a hash that does not
resolve).
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):  # vault_lint.py omits this; its siblings do not
    sys.stdout.reconfigure(encoding="utf-8")

FROZEN_REL = "regression/frozen"

# `baseline_commits: <repo> @ <sha> -- <path>[, <path>...] [| <repo> @ <sha> -- ...]`
#
# Deliberately NOT YAML. Five of the six frozen files do not parse as YAML at all
# (unquoted prose values containing ": " — the same defect that silently disabled
# usadebusk-fieldpm for three weeks), and rewriting a frozen baseline to satisfy a
# parser is exactly the wrong trade. This grammar is readable by the vault's own
# flat `key: value` frontmatter parser, which is what every other tool here uses.
ENTRY_SEP = "|"
REPO_RE = re.compile(r"^\s*(?P<repo>[A-Za-z0-9_-]+)\s*@\s*(?P<sha>[0-9a-f]{7,40})\s*--\s*(?P<paths>.+)$")


def repo_roots(vault: Path) -> dict[str, Path]:
    """Map the repo names used in `baseline_commits:` onto real checkouts."""
    return {"vault": vault, "claude-config": Path.home() / ".claude"}


def parse_frontmatter(text: str) -> dict[str, str]:
    """Flat `key: value` frontmatter, matching tools/estimating_rollup.py.

    Nested structures are not supported and not wanted — see the grammar note
    above. A repeated key takes its last value, same as the sibling parsers.
    """
    fm: dict[str, str] = {}
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return fm
    for line in lines[1:]:
        if line.strip() == "---":
            break
        m = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if m:
            fm[m.group(1).strip()] = m.group(2).strip()
    return fm


def parse_baseline_commits(raw: str) -> tuple[list[dict], list[str]]:
    """Return (entries, problems). An unparseable entry is a problem, not a skip.

    Silently dropping a malformed entry would make a fixture with a typo'd
    baseline look perfectly current, which is the failure this tool exists to
    prevent.
    """
    entries, problems = [], []
    for chunk in raw.split(ENTRY_SEP):
        if not chunk.strip():
            continue
        m = REPO_RE.match(chunk)
        if not m:
            problems.append(f"unparseable entry: {chunk.strip()!r}")
            continue
        paths = [p.strip() for p in m.group("paths").split(",") if p.strip()]
        if not paths:
            problems.append(f"entry names no paths: {chunk.strip()!r}")
            continue
        entries.append({"repo": m.group("repo"), "sha": m.group("sha"), "paths": paths})
    return entries, problems


def git(root: Path, *args: str) -> tuple[int, str]:
    proc = subprocess.run(
        ["git", "-C", str(root), *args],
        capture_output=True, text=True, encoding="utf-8", errors="replace",
    )
    return proc.returncode, (proc.stdout or "").strip()


def commits_behind(root: Path, sha: str, paths: list[str]) -> tuple[int, list[str], str | None]:
    """Commits touching `paths` since `sha`. Returns (count, subjects, error)."""
    rc, _ = git(root, "cat-file", "-e", f"{sha}^{{commit}}")
    if rc != 0:
        return 0, [], f"hash {sha} does not resolve in {root.name}"
    rc, out = git(root, "log", "--format=%h %s", f"{sha}..HEAD", "--", *paths)
    if rc != 0:
        return 0, [], f"git log failed against {sha} in {root.name}"
    subjects = [ln for ln in out.splitlines() if ln.strip()]
    return len(subjects), subjects, None


def collect(vault: Path) -> tuple[list[dict], list[str]]:
    """One result per frozen fixture, plus repo-level notes."""
    roots = repo_roots(vault)
    config = roots["claude-config"]
    frozen = config / FROZEN_REL
    notes: list[str] = []

    if not config.exists() or not (config / ".git").exists():
        return [], [f"claude-config repo not present at {config} — nothing judged"]
    if not frozen.is_dir():
        return [], [f"no frozen fixtures at {frozen} — nothing judged"]

    results = []
    for path in sorted(frozen.glob("*.md")):
        fm = parse_frontmatter(path.read_text(encoding="utf-8"))
        name = fm.get("fixture") or path.stem
        raw = fm.get("baseline_commits", "")
        row = {"fixture": name, "file": path, "per_repo": [], "problems": []}
        if not raw:
            row["problems"].append("no baseline_commits: field")
            results.append(row)
            continue
        entries, problems = parse_baseline_commits(raw)
        row["problems"].extend(problems)
        for e in entries:
            root = roots.get(e["repo"])
            if root is None:
                row["problems"].append(f"unknown repo {e['repo']!r}")
                continue
            if not root.exists():
                row["per_repo"].append({"repo": e["repo"], "count": None, "subjects": []})
                continue
            count, subjects, err = commits_behind(root, e["sha"], e["paths"])
            if err:
                row["problems"].append(err)
                continue
            row["per_repo"].append({"repo": e["repo"], "count": count, "subjects": subjects})
        results.append(row)
    return results, notes


def summarize(row: dict) -> tuple[str, str]:
    """Return (detail, status) for one fixture."""
    if row["problems"]:
        return "; ".join(row["problems"]), "FAIL: cannot judge"
    if not row["per_repo"]:
        return "no repos judged", "-"
    parts, behind, unjudged = [], 0, False
    for r in row["per_repo"]:
        if r["count"] is None:
            parts.append(f"{r['repo']} -")
            unjudged = True
        else:
            parts.append(f"{r['repo']} {r['count']}")
            behind += r["count"]
    detail = " · ".join(parts)
    if unjudged and behind == 0:
        return detail, "-"
    return detail, "behind" if behind else "current"


def health_rows(vault: Path) -> tuple[list[tuple[str, str, str]], int, bool]:
    """For vault_health.py. Returns (rows, behind_count, judged)."""
    results, notes = collect(vault)
    if not results:
        return [], 0, False
    rows, behind = [], 0
    for row in results:
        detail, status = summarize(row)
        if status == "behind":
            behind += 1
        rows.append((row["fixture"], detail, status))
    return rows, behind, True


def self_test() -> int:
    """Prove the tool can say 'current', not only 'behind'.

    On the real battery every baseline currently reports behind, so a run against
    live data cannot distinguish a working checker from one that reports staleness
    unconditionally. These cases pin the other outcomes.
    """
    vault = Path(__file__).resolve().parent.parent

    # 1. A baseline AT HEAD must report zero behind. This is the falsification
    #    case: without it, "6 of 6 behind" is unfalsifiable.
    rc, head = git(vault, "rev-parse", "--short", "HEAD")
    if rc != 0:
        print("SELF-TEST FAILED — cannot read vault HEAD")
        return 2
    count, _, err = commits_behind(vault, head, ["tools/"])
    if err or count != 0:
        print(f"SELF-TEST FAILED — HEAD baseline should be 0 behind, got {count} ({err})")
        return 2

    # 2. A known-old commit must report NON-zero on a path that has since moved,
    #    proving the count tracks real history rather than returning 0 always.
    rc, first = git(vault, "rev-list", "--max-parents=0", "HEAD")
    if rc == 0 and first:
        count, _, err = commits_behind(vault, first.splitlines()[0], ["tools/"])
        if err or count == 0:
            print(f"SELF-TEST FAILED — root commit should be many behind, got {count} ({err})")
            return 2

    # 3. A malformed entry must surface as a problem, never be skipped — a
    #    silently-dropped entry makes a typo'd baseline look perfectly current.
    entries, problems = parse_baseline_commits("claude-config @ notasha -- skills/x")
    if entries or not problems:
        print(f"SELF-TEST FAILED — malformed entry not reported: {entries} {problems}")
        return 2
    entries, problems = parse_baseline_commits("claude-config @ a8cc6fd --   ")
    if entries or not problems:
        print(f"SELF-TEST FAILED — path-less entry not reported: {entries} {problems}")
        return 2

    # 4. A well-formed multi-repo line must parse into both entries.
    entries, problems = parse_baseline_commits(
        "claude-config @ a8cc6fd -- skills/a, skills/b | vault @ 6d73e15 -- 04-knowledge/c.md")
    if problems or len(entries) != 2 or entries[0]["paths"] != ["skills/a", "skills/b"]:
        print(f"SELF-TEST FAILED — good line misparsed: {entries} {problems}")
        return 2

    # 5. An unresolvable hash is a problem, not a silent zero.
    _, _, err = commits_behind(vault, "0" * 40, ["tools/"])
    if not err:
        print("SELF-TEST FAILED — unresolvable hash reported no error")
        return 2

    print("SELF-TEST PASSED — 5 cases: current, behind, two malformed, unresolvable hash.")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--verbose", action="store_true", help="list the commits behind each baseline")
    ap.add_argument("--self-test", action="store_true", help="run the built-in cases and exit")
    args = ap.parse_args()

    if args.self_test:
        return self_test()

    vault = Path(__file__).resolve().parent.parent
    results, notes = collect(vault)

    for n in notes:
        print(f"[-] {n}")
    if not results:
        return 2

    worst = 0
    for row in results:
        detail, status = summarize(row)
        print(f"{row['fixture']:26s} {status:18s} {detail}")
        if status.startswith("FAIL"):
            worst = max(worst, 2)
        elif status == "behind":
            worst = max(worst, 1)
        if args.verbose:
            for r in row["per_repo"]:
                for s in r["subjects"]:
                    print(f"    {r['repo']}: {s}")

    behind = sum(1 for r in results if summarize(r)[1] == "behind")
    print(f"\n{behind} of {len(results)} baselines behind their inputs.")
    return worst


if __name__ == "__main__":
    raise SystemExit(main())
