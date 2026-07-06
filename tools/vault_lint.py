#!/usr/bin/env python3
"""vault_lint.py — the vault's one standing automated check.

Pure standard library. Runs anywhere Python 3.11+ runs; no Obsidian, no
model, no network required. This is the "scripts over attention" floor:
every check here used to be something an agent had to notice while reading.

Rules (code | severity):
    OP-FRONTMATTER  warning  operational notes should carry source + verified
    DEAD-LINK       warning  [[wikilink]] whose target exists nowhere in repo
    SECRET          error    credential-shaped string committed to the vault
    INBOX-AGE       warning  inbox item older than 14 days, or untracked in git
    STATUS-VOCAB    warning  status: value outside the known vocabulary
    CONF-CONFLICT   error    confidence: high on an AI-inferred source

Only SECRET and CONF-CONFLICT are errors (exit 1). Everything else is a
warning so the vault is never "failing" for want of a bulk backfill —
warnings are the to-do list, errors are the stop-the-line list. New lint
rules require a fixture under tools/fixtures/ (no fixture, no rule).

Usage:
    python tools/vault_lint.py               lint the vault, print findings
    python tools/vault_lint.py --report      also write 50-dashboards/lint-report.md
    python tools/vault_lint.py --self-test   verify every rule fires on its fixture
    python tools/vault_lint.py --root PATH   lint a different tree (used by self-test)

Windows: `py tools/vault_lint.py` if `python` is not on PATH.

Exit codes: 0 = no errors (warnings allowed), 1 = errors found, 2 = self-test failure.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from datetime import date, datetime
from pathlib import Path

# --- configuration -----------------------------------------------------------

OPERATIONAL_DIRS = ("02-facilities", "04-knowledge/pricing")
INBOX_DIR = "00-inbox"
INBOX_SKIP_SUBDIRS = ("preserved-dsps",)  # deliberately held, per README there
INBOX_MAX_AGE_DAYS = 14

# Folders never scanned for problems (archive is history; templates are blanks;
# fixtures contain deliberate violations; .obsidian is app state).
SKIP_SCAN = ("archive", "templates", "tools/fixtures", ".obsidian", ".git")

# Status vocabulary actually in use across the vault as of 2026-07-05, plus the
# decision-queue's `expired`. Keep this list honest — it is the vocabulary, not
# an aspiration. A value not here is a warning, not a crash.
ALLOWED_STATUS = {
    # lifecycle
    "inbox", "draft", "active", "reviewed", "for-review", "stale",
    "deprecated", "complete", "open", "closed-unactioned", "expired",
    # review/decision outcomes
    "resolved", "unresolved", "pending", "superseded",
    "decided-blocked", "approved-blocked", "awarded",
    # research
    "unexplored", "researched",
}

SECRET_PATTERNS = [
    ("aws-access-key", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
    ("github-token", re.compile(r"\b(ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9]{36,}\b")),
    ("github-pat", re.compile(r"\bgithub_pat_[A-Za-z0-9_]{22,}\b")),
    ("private-key", re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----")),
    ("generic-credential", re.compile(
        r"(?i)\b(api[_-]?key|secret[_-]?key|access[_-]?token|password)\b\s*[:=]\s*['\"]?[A-Za-z0-9+/_\-]{20,}")),
]

WIKILINK_RE = re.compile(r"\[\[([^\[\]|#]+)(?:#[^\[\]|]*)?(?:\|[^\[\]]*)?\]\]")
FENCE_RE = re.compile(r"^\s*(```|~~~)")

ERROR_CODES = {"SECRET", "CONF-CONFLICT"}


class Finding:
    def __init__(self, code: str, path: Path, detail: str):
        self.code = code
        self.path = path
        self.detail = detail
        self.severity = "error" if code in ERROR_CODES else "warning"

    def __str__(self) -> str:
        return f"[{self.severity.upper():7}] {self.code:14} {self.path}: {self.detail}"


# --- helpers ------------------------------------------------------------------

def parse_frontmatter(text: str) -> dict[str, str]:
    """Minimal YAML-subset parser: top-level `key: value` between --- fences."""
    fm: dict[str, str] = {}
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return fm
    for line in lines[1:]:
        if line.strip() == "---":
            break
        m = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if m:
            fm[m.group(1).strip()] = m.group(2).strip().strip("'\"")
    return fm


def skip(path: Path, root: Path) -> bool:
    rel = path.relative_to(root).as_posix()
    return any(rel == s or rel.startswith(s + "/") for s in SKIP_SCAN)


def body_lines_outside_fences(text: str):
    in_fence = False
    for line in text.splitlines():
        if FENCE_RE.match(line):
            in_fence = not in_fence
            continue
        if not in_fence:
            yield line


def git_last_commit_date(root: Path, path: Path) -> date | None:
    try:
        out = subprocess.run(
            ["git", "log", "-1", "--format=%cs", "--", str(path.relative_to(root))],
            cwd=root, capture_output=True, text=True, timeout=30,
        ).stdout.strip()
        return datetime.strptime(out, "%Y-%m-%d").date() if out else None
    except Exception:
        return None


# --- rules --------------------------------------------------------------------

def check_operational_frontmatter(root: Path, notes: dict[Path, str]) -> list[Finding]:
    """OP-FRONTMATTER: operational notes should carry `source` and `verified`.

    Warning, not error: this is the provenance backfill to-do list, and the
    vault should not read as failing until that separate session runs.
    """
    findings = []
    for path, text in notes.items():
        rel = path.relative_to(root).as_posix()
        if not any(rel.startswith(d + "/") for d in OPERATIONAL_DIRS):
            continue
        if path.name.startswith("_"):  # indexes/directories, not fact carriers
            continue
        fm = parse_frontmatter(text)
        missing = [k for k in ("source", "verified") if k not in fm]
        if missing:
            findings.append(Finding("OP-FRONTMATTER", path,
                                    f"operational note missing frontmatter: {', '.join(missing)}"))
    return findings


def check_dead_links(root: Path, notes: dict[Path, str]) -> list[Finding]:
    """DEAD-LINK: [[wikilink]] whose target note exists nowhere in the repo."""
    known = set()
    for p in root.rglob("*.md"):  # resolution set includes archive/ deliberately
        rel = p.relative_to(root).as_posix()
        if rel.startswith((".git/", ".obsidian/", "tools/fixtures/")):
            continue
        known.add(p.stem.lower())
    findings = []
    for path, text in notes.items():
        for line in body_lines_outside_fences(text):
            for m in WIKILINK_RE.finditer(line):
                target = m.group(1).strip()
                if not target or "<" in target:  # template placeholders
                    continue
                # Obsidian resolves path-style links by their final segment.
                stem = target.rsplit("/", 1)[-1].lower()
                if stem not in known:
                    findings.append(Finding("DEAD-LINK", path, f"[[{target}]] not found"))
    return findings


def check_secrets(root: Path, notes: dict[Path, str]) -> list[Finding]:
    """SECRET: credential-shaped strings must never be committed."""
    findings = []
    for path, text in notes.items():
        for name, pat in SECRET_PATTERNS:
            if pat.search(text):
                findings.append(Finding("SECRET", path, f"matches {name} pattern"))
    return findings


def check_inbox_age(root: Path) -> list[Finding]:
    """INBOX-AGE: inbox items older than 14 days (by last git commit), or untracked."""
    findings = []
    inbox = root / INBOX_DIR
    if not inbox.is_dir():
        return findings
    today = date.today()
    for p in sorted(inbox.rglob("*")):
        if not p.is_file() or p.name.startswith("."):
            continue
        rel = p.relative_to(inbox).as_posix()
        if any(rel.startswith(s + "/") for s in INBOX_SKIP_SUBDIRS):
            continue
        d = git_last_commit_date(root, p)
        if d is None:
            findings.append(Finding("INBOX-AGE", p, "untracked in git — file it or commit it"))
        elif (today - d).days > INBOX_MAX_AGE_DAYS:
            findings.append(Finding("INBOX-AGE", p, f"in inbox {(today - d).days} days"))
    return findings


def check_status_vocab(root: Path, notes: dict[Path, str]) -> list[Finding]:
    """STATUS-VOCAB: `status:` values come from the fixed vocabulary."""
    findings = []
    for path, text in notes.items():
        fm = parse_frontmatter(text)
        status = fm.get("status")
        if status and status not in ALLOWED_STATUS:
            findings.append(Finding("STATUS-VOCAB", path, f"unknown status '{status}'"))
    return findings


def check_confidence_conflict(root: Path, notes: dict[Path, str]) -> list[Finding]:
    """CONF-CONFLICT: AI-inferred sources may never claim high confidence."""
    findings = []
    for path, text in notes.items():
        fm = parse_frontmatter(text)
        if fm.get("confidence") == "high" and fm.get("source_authority") == "inferred":
            findings.append(Finding("CONF-CONFLICT", path,
                                    "confidence: high with source_authority: inferred"))
    return findings


# --- driver -------------------------------------------------------------------

GENERATED_MARKER = "GENERATED by tools/"


def collect_notes(root: Path) -> dict[Path, str]:
    notes = {}
    for p in sorted(root.rglob("*.md")):
        if skip(p, root):
            continue
        try:
            text = p.read_text(encoding="utf-8", errors="replace")
        except OSError as e:
            print(f"[WARN] unreadable: {p}: {e}", file=sys.stderr)
            continue
        # Generated files (lint-report, health) echo link text and status values;
        # scanning them as sources would re-flag their own quoted findings. They
        # self-declare with a marker on the first line — skip them as sources.
        if GENERATED_MARKER in text[:200]:
            continue
        notes[p] = text
    return notes


def run_lint(root: Path, with_git: bool = True) -> list[Finding]:
    notes = collect_notes(root)
    findings = []
    findings += check_operational_frontmatter(root, notes)
    findings += check_dead_links(root, notes)
    findings += check_secrets(root, notes)
    if with_git:
        findings += check_inbox_age(root)
    findings += check_status_vocab(root, notes)
    findings += check_confidence_conflict(root, notes)
    return findings


def write_report(root: Path, findings: list[Finding]) -> Path:
    out = root / "50-dashboards" / "lint-report.md"
    out.parent.mkdir(exist_ok=True)
    errors = [f for f in findings if f.severity == "error"]
    warnings = [f for f in findings if f.severity == "warning"]
    lines = [
        "<!-- GENERATED by tools/vault_lint.py --report — do not edit; rerun to refresh -->",
        "# Vault Lint Report",
        f"**Generated:** {date.today().isoformat()} | **Errors:** {len(errors)} | **Warnings:** {len(warnings)}",
        "",
    ]
    if not findings:
        lines.append("Clean — no findings.")
    for group, title in ((errors, "Errors"), (warnings, "Warnings")):
        if group:
            lines += [f"## {title}", "", "| Code | File | Detail |", "|---|---|---|"]
            lines += [f"| {f.code} | `{f.path.relative_to(root)}` | {f.detail} |" for f in group]
            lines.append("")
    out.write_text("\n".join(lines), encoding="utf-8")
    return out


def self_test() -> int:
    """Every rule must fire on its fixture. Fixture tree mimics vault layout."""
    fixtures = Path(__file__).resolve().parent / "fixtures"
    findings = run_lint(fixtures, with_git=False)
    # INBOX-AGE: an untracked inbox file must be flagged. Committed fixtures are
    # tracked (and fresh), so create a throwaway untracked file for this check.
    temp = fixtures / INBOX_DIR / "untracked-temp-selftest.md"
    temp.parent.mkdir(parents=True, exist_ok=True)
    temp.write_text("self-test scratch — safe to delete\n", encoding="utf-8")
    try:
        findings += check_inbox_age(fixtures)
    finally:
        temp.unlink(missing_ok=True)
    fired = {f.code for f in findings}
    expected = {"OP-FRONTMATTER", "DEAD-LINK", "SECRET", "STATUS-VOCAB",
                "CONF-CONFLICT", "INBOX-AGE"}
    missing = expected - fired
    for f in findings:
        print(f"  fixture: {f}")
    if missing:
        print(f"SELF-TEST FAILED — rules did not fire: {', '.join(sorted(missing))}")
        return 2
    print(f"SELF-TEST OK — all {len(expected)} rules fired on their fixtures.")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", type=Path, default=None)
    ap.add_argument("--report", action="store_true")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()

    if args.self_test:
        return self_test()

    root = (args.root or Path(__file__).resolve().parent.parent).resolve()
    if not (root / "CLAUDE.md").exists():
        print(f"ERROR: {root} does not look like the vault root (no CLAUDE.md).")
        return 1

    findings = run_lint(root)
    for f in findings:
        print(f)
    errors = sum(1 for f in findings if f.severity == "error")
    warnings = len(findings) - errors
    print(f"\n{errors} error(s), {warnings} warning(s).")
    if args.report:
        print(f"Report written: {write_report(root, findings)}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
