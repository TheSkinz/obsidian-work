#!/usr/bin/env python3
"""vault_health.py — generate 50-dashboards/health.md, the vault's vitals.

Pure standard library; reuses tools/vault_lint.py for the lint counts. Writes
a GENERATED file that overwrites itself on every run and says so in its header.
Generated files are the one sanctioned exception to the vault's append-only
discipline.

What it trends (the numbers you can act on in one glance):
    - open decision rows        (from 50-dashboards/decision-queue.md)
    - review notes awaiting a decision (unchecked Decision boxes in 06-insights)
    - inbox items + median age  (git commit dates)
    - lint errors / warnings    (tools/vault_lint.py)
    - days since last commit    (basic liveness signal)
    - per-loop heartbeats       (commit-subject prefixes, flagged at >2x cadence)

Usage:
    python tools/vault_health.py            write 50-dashboards/health.md
    python tools/vault_health.py --print     also print the dashboard to stdout

Windows: `py tools/vault_health.py`.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from datetime import date, datetime, timezone
from pathlib import Path
from statistics import median

sys.path.insert(0, str(Path(__file__).resolve().parent))
import baseline_staleness  # noqa: E402  (same-dir sibling module)
import vault_lint  # noqa: E402  (same-dir sibling module)

QUEUE_REL = "50-dashboards/decision-queue.md"
HEALTH_REL = "50-dashboards/health.md"
QUEUE_ROW_RE = re.compile(r"^\|\s*(DQ-\d+)\s*\|")
INBOX_SKIP_SUBDIRS = ("preserved-dsps",)

# Loop monitoring reads two independent signals:
#   1. The run ledger (50-dashboards/.loop-runs.json, local + gitignored):
#      every loop records "fired" as its first action and "completed" as its
#      last. This is the liveness channel — it distinguishes a dead/disabled
#      scheduler (fired goes stale) from a run that crashed mid-flight
#      (fired without completed) from a quiet no-op (completed, no commit).
#   2. The git heartbeat (commit-subject prefix): proof a run finished with
#      output. Kept as fallback for loops with no ledger telemetry yet.
# The review/agent loop is on-demand by design and not listed at all.
# Skill-drift IS listed as of 2026-07-25. It was delisted 2026-07-19 on the
# belief that an unattended run would stall for lack of config-repo write
# authority; that premise was false (settings.json runs defaultMode "auto"
# and neither allows nor denies git add/commit/push, and the git-guard hook
# only matches USADEBUSK paths), and the task has been enabled and firing
# monthly the whole time. An enabled loop with no heartbeat row is the exact
# blind spot the ledger exists to close.
#
# Tuples: (label, ledger task_id, commit prefix, hb_cadence_days, fired_stale_days).
# fired_stale_days is 2x the loop's run cadence (with slack for a machine that
# is off at fire time — the app catches up missed runs on wake).
LOOP_HEARTBEATS = [
    # Capture runs daily as of 2026-07-28 (was Mondays). Like the idea loop it
    # commits only when a run has something to file, so its git heartbeat stays
    # monitoring-grade (7 d -> flagged at 14 d), not its 1 d run cadence. Ledger
    # staleness tightens to 3 d: daily firing should never be older than that.
    ("Capture loop", "vault-capture-loop", "vault-capture:", 7, 3),
    # Idea loop runs nightly but only commits when a seed exists, so its git
    # heartbeat cadence is monitoring-grade (30 d), not its run cadence. Its
    # ledger staleness is tight (3 d) — nightly firing should never be older.
    ("Idea-research loop", "vault-idea-research-loop", "vault-idea-research:", 30, 3),
    # Pre-staging runs daily at 06:00 (an hour behind capture, which applies the
    # defer markers it reads) but is silent whenever the decision queue is at cap
    # or the pile is empty, so its git heartbeat is monitoring-grade (30 d) like
    # the idea loop's. Ledger staleness 3 d: daily firing should never be older.
    ("Pre-staging loop", "vault-prestaging-loop", "vault-prestage:", 30, 3),
    ("Consolidation loop", "vault-consolidation-loop", "vault-consolidate:", 31, 62),
    # Skill-drift fires monthly (0 3 1 * *) but commits only when it finds
    # drift, so its git heartbeat cadence carries the same slack as the idea
    # loop's: 62 d monitoring-grade, not its 31 d run cadence.
    ("Skill-drift loop", "vault-skill-drift-loop", "skill-drift:", 62, 62),
]

LEDGER_REL = "50-dashboards/.loop-runs.json"

# Dormant triggers: any note carrying a `revisit-trigger:` frontmatter field is
# a recorded wake-up condition (parked idea, deferred build, rejected-with-
# revisit decision). The field's presence — regardless of the note's status,
# since a resolved review's trigger outlives its resolution — puts it on the
# dashboard. Retire a trigger by removing the field when it fires and is acted
# on. Machine-checkable conditions embed a token the script evaluates; three
# exist: `[machine: quote-count>=N]` (count of `type: quote` notes),
# `[machine: routine-rows>=N]` (rows behind the `routine` mean in the generated
# actuals rollup) and `[machine: note-count>=N]` (live scanned notes — the same
# population every other check uses, so archive/, templates/, fixtures and
# generated files are excluded). Everything else is event-shaped and names the
# workflow step that checks it. An unrecognized token falls through to the
# event-shaped wording, so a typo'd token reads as "someone checks this by hand"
# rather than failing loudly — keep this list and the tokens in use in sync.
TRIGGER_FIELD = "revisit-trigger"
TRIGGER_QC_RE = re.compile(r"\[machine:\s*quote-count\s*>=\s*(\d+)\]")
TRIGGER_RR_RE = re.compile(r"\[machine:\s*routine-rows\s*>=\s*(\d+)\]")
TRIGGER_NC_RE = re.compile(r"\[machine:\s*note-count\s*>=\s*(\d+)\]")
ROLLUP_REL = "04-knowledge/estimating-actuals-rollup.md"

# Commercial pipeline: read from `type: quote` frontmatter. `valid-through`
# and `date-execution` tolerate YYYY-MM-DD and YYYY-MM (month reads as the
# 1st). FAIL only for a quote that expired while still `pending` — that is
# silent commercial exposure; everything else is informational.
PIPELINE_EXPIRY_WARN_DAYS = 30
PIPELINE_HORIZON_DAYS = 90

# A run older than this with "fired" but no "completed" is presumed dead,
# not still working. Generous: no loop run legitimately takes 6 hours.
RUN_DEAD_HOURS = 6


def read_ledger(root: Path) -> dict:
    try:
        data = json.loads((root / LEDGER_REL).read_text(encoding="utf-8"))
        return data if isinstance(data, dict) else {}
    except Exception:
        return {}


def parse_iso(s) -> datetime | None:
    if not isinstance(s, str) or not s:
        return None
    try:
        dt = datetime.fromisoformat(s.replace("Z", "+00:00"))
        return dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)
    except ValueError:
        return None


def git_last_commit_date(root: Path, rel: str) -> date | None:
    try:
        out = subprocess.run(
            ["git", "log", "-1", "--format=%cs", "--", rel],
            cwd=root, capture_output=True, text=True, timeout=30,
        ).stdout.strip()
        return datetime.strptime(out, "%Y-%m-%d").date() if out else None
    except Exception:
        return None


def count_open_decisions(root: Path) -> int:
    q = root / QUEUE_REL
    if not q.is_file():
        return 0
    open_rows = 0
    in_open = False
    for line in q.read_text(encoding="utf-8").splitlines():
        s = line.strip()
        if s.startswith("## Open"):
            in_open = True
            continue
        if in_open and s.startswith("## "):
            break
        if in_open and QUEUE_ROW_RE.match(line):
            open_rows += 1
    return open_rows


def count_pending_reviews(root: Path) -> int:
    """Review notes in 06-insights with at least one unchecked Decision box.

    This is the 'what needs Jesse' number: loops write review notes with
    empty checkboxes, and an unreviewed pile is where compounding stalls.
    Surfaced at session startup via CLAUDE.md's health-check rule.
    """
    insights = root / "06-insights"
    if not insights.is_dir():
        return 0
    pending = 0
    for p in sorted(insights.glob("*.md")):
        try:
            text = p.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        if "GENERATED by tools/" in text[:200]:
            continue
        # A note with a terminal status is resolved — its leftover unchecked
        # boxes (rejected alternatives) are not pending work. Skip it.
        if vault_lint.parse_frontmatter(text).get("status") in vault_lint.TERMINAL_STATUS:
            continue
        # Only count notes that have a Decision section with an unchecked box.
        if re.search(r"^#+\s*Decision\b", text, re.MULTILINE) and re.search(r"^\s*-\s*\[ \]", text, re.MULTILINE):
            pending += 1
    return pending


def inbox_stats(root: Path) -> tuple[int, int | None, int | None]:
    """Return (item_count, median_age_days, max_age_days) for inbox files."""
    inbox = root / vault_lint.INBOX_DIR
    if not inbox.is_dir():
        return 0, None, None
    today = date.today()
    ages: list[int] = []
    count = 0
    for p in sorted(inbox.rglob("*")):
        if not p.is_file() or p.name.startswith("."):
            continue
        rel = p.relative_to(inbox).as_posix()
        if any(rel.startswith(s + "/") for s in INBOX_SKIP_SUBDIRS):
            continue
        count += 1
        d = git_last_commit_date(root, str(p.relative_to(root)))
        if d is not None:
            ages.append((today - d).days)
    if not ages:
        return count, None, None
    return count, int(median(ages)), max(ages)


def days_since_last_commit(root: Path) -> int | None:
    d = git_last_commit_date(root, ".")
    return (date.today() - d).days if d else None


def git_last_grep_date(root: Path, prefix: str) -> date | None:
    """Date of the most recent commit whose subject starts with `prefix`."""
    try:
        out = subprocess.run(
            ["git", "log", "-1", "--format=%cs", f"--grep=^{re.escape(prefix)}"],
            cwd=root, capture_output=True, text=True, timeout=30,
        ).stdout.strip()
        return datetime.strptime(out, "%Y-%m-%d").date() if out else None
    except Exception:
        return None


def loop_heartbeats(root: Path):
    """Return (rows, any_overdue). Each row: (label, fired, heartbeat, cadence, status)."""
    today = date.today()
    now = datetime.now(timezone.utc)
    ledger = read_ledger(root)
    rows = []
    any_overdue = False
    for label, task_id, prefix, cadence, stale_days in LOOP_HEARTBEATS:
        d = git_last_grep_date(root, prefix)
        hb = "never" if d is None else f"{d.isoformat()} ({(today - d).days} d ago)"
        entry = ledger.get(task_id) or {}
        fired = parse_iso(entry.get("fired"))
        completed = parse_iso(entry.get("completed"))

        if fired is not None:
            age_days = (now - fired).days
            fired_s = f"{fired.date().isoformat()} ({age_days} d ago)"
            if completed is None or completed < fired:
                hours = (now - fired).total_seconds() / 3600
                status = "running" if hours <= RUN_DEAD_HOURS else "FAIL: started, never finished"
            elif age_days > stale_days:
                status = "FAIL: scheduler silent"  # disabled, deregistered, or machine off
            else:
                status = "ok"
        else:
            # No ledger telemetry yet — fall back to the git heartbeat alone.
            fired_s = "-"
            if d is None:
                status = "pending"
            else:
                status = "FAIL" if (today - d).days > 2 * cadence else "ok"

        any_overdue = any_overdue or status.startswith("FAIL")
        rows.append((label, fired_s, hb, f"{cadence} d", status))
    return rows, any_overdue


def parse_day(raw: str | None) -> date | None:
    """Tolerant date parse: YYYY-MM-DD, or YYYY-MM (reads as the 1st)."""
    if not raw:
        return None
    for fmt in ("%Y-%m-%d", "%Y-%m"):
        try:
            return datetime.strptime(raw, fmt).date()
        except ValueError:
            continue
    return None


def collect_quotes(notes: dict) -> list[tuple[Path, dict]]:
    out = []
    for path, text in notes.items():
        fm = vault_lint.parse_frontmatter(text)
        if fm.get("type") == "quote":
            out.append((path, fm))
    return sorted(out, key=lambda t: t[0].stem)


def _verified_day(fm: dict) -> date | None:
    """The leading YYYY-MM-DD of a `verified:` value, which is prose after the date."""
    m = re.match(r"\s*(\d{4}-\d{2}-\d{2})", str(fm.get("verified") or ""))
    return parse_day(m.group(1)) if m else None


def bid_folder_signal(fm: dict, text: str) -> str:
    """Existence + recency of the bid folder a quote note points at.

    Soft signal only, and deliberately NOT a lint rule: a missing OneDrive root,
    an unsynced folder and a genuinely stale note all look identical from here,
    and lint is a binary 0-errors gate that cannot carry a maybe. Ruled
    2026-08-15 (option B narrowed by C) after DSP26095 read "Not yet priced — no
    rates on file" on 2026-07-28 while its own bid folder already held a finished
    quotation and a priced workup.

    Value comparison is deliberately out of scope — that half is deferred to the
    quotation-vs-workup pre-send gate, which reads the workup's reconciled total
    rather than guessing from filenames.

    Base-gated exactly like POINTER-DEAD: judged only when the path's first three
    components exist on this machine, so it degrades to "-" elsewhere instead of
    reporting every quote as broken.
    """
    dirs = []
    for line in vault_lint.body_lines_outside_fences(text):
        for m in vault_lint.POINTER_RE.finditer(line):
            raw = m.group(1).strip(" ")
            if "…" in raw or "�" in raw:
                continue
            p = Path(raw)
            if len(p.parts) < 3:
                continue
            try:
                if not Path(*p.parts[:3]).exists():
                    return "-"  # base absent — different machine, not a finding
                if p.is_dir():
                    dirs.append(p)
            except OSError:
                continue
    if not dirs:
        return "no bid folder path recorded"

    newest, newest_name = None, None
    for d in dirs:
        try:
            for f in d.iterdir():
                if not f.is_file():
                    continue
                mt = date.fromtimestamp(f.stat().st_mtime)
                if newest is None or mt > newest:
                    newest, newest_name = mt, f.name
        except OSError:
            continue
    if newest is None:
        return "folder empty or unreadable"

    ver = _verified_day(fm)
    if ver is None:
        return f"newest artifact {newest} — note carries no verified date"
    if newest > ver:
        return f"artifacts newer than verified ({ver}) — newest {newest}, check the note"
    return "ok"


def pipeline_rows(notes: dict):
    """Return (rows, expired_count). One row per pending quote plus any quote
    inside the execution horizon.
    Row: (quote, status, valid, execution, signal, bid-folder)."""
    today = date.today()
    rows = []
    expired = 0
    for path, fm in collect_quotes(notes):
        q = fm.get("quote-number") or path.stem
        link = f"[[{q}]]" if q == path.stem else f"[[{path.stem}|{q}]]"
        status = fm.get("status", "?")
        vt = parse_day(fm.get("valid-through"))
        ex = parse_day(fm.get("date-execution"))
        signal = None
        if status == "pending":
            if vt is None:
                signal = "no validity date recorded"
            elif vt < today:
                signal = f"EXPIRED {(today - vt).days} d ago — record outcome or extension"
                expired += 1
            elif (vt - today).days <= PIPELINE_EXPIRY_WARN_DAYS:
                signal = f"expires in {(vt - today).days} d"
            else:
                signal = "ok"
        if ex and status in ("pending", "awarded") and today <= ex \
                and (ex - today).days <= PIPELINE_HORIZON_DAYS:
            note = f"execution in {(ex - today).days} d"
            signal = f"{signal}; {note}" if signal and signal != "ok" else note
        if signal:
            rows.append((link, status, fm.get("valid-through") or "-",
                         fm.get("date-execution") or "-", signal,
                         bid_folder_signal(fm, notes[path])))
    return rows, expired


def count_routine_rows(root: Path) -> int | None:
    """Rows behind the `routine` mean in the generated actuals rollup.

    The rollup carries the GENERATED marker, so `collect_notes` skips it and it
    has to be read from disk. Returns None when the file or its condition table
    is missing: an unreadable source must show as unknown rather than 0, since
    0 would read as "no routine actuals yet" and quietly never fire.
    """
    try:
        text = (root / ROLLUP_REL).read_text(encoding="utf-8", errors="replace")
    except OSError:
        return None
    for line in text.splitlines():
        if not line.lstrip().startswith("|"):
            continue
        # Parse cells, not the raw string — Obsidian pads table cells.
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) >= 2 and cells[0].lower() == "routine":
            try:
                return int(cells[1])
            except ValueError:
                return None
    return None


def trigger_rows(notes: dict, root: Path):
    """Return (rows, fired_count). Row: (source stem, condition, check result)."""
    quote_count = len(collect_quotes(notes))
    routine_rows = count_routine_rows(root)
    note_count = len(notes)
    rows = []
    fired = 0
    for path, text in sorted(notes.items()):
        fm = vault_lint.parse_frontmatter(text)
        raw = fm.get(TRIGGER_FIELD)
        if not raw:
            continue
        qc = TRIGGER_QC_RE.search(raw)
        rr = TRIGGER_RR_RE.search(raw)
        nc = TRIGGER_NC_RE.search(raw)
        if qc:
            threshold = int(qc.group(1))
            hit = quote_count >= threshold
            check = f"quote notes: {quote_count} of {threshold}" + (" — **FIRED**" if hit else "")
            fired += 1 if hit else 0
        elif rr:
            threshold = int(rr.group(1))
            if routine_rows is None:
                check = "routine rows: source unreadable — check `estimating-actuals-rollup.md`"
            else:
                hit = routine_rows >= threshold
                check = f"routine rows: {routine_rows} of {threshold}" + (" — **FIRED**" if hit else "")
                fired += 1 if hit else 0
        elif nc:
            threshold = int(nc.group(1))
            hit = note_count >= threshold
            check = f"live notes: {note_count} of {threshold}" + (" — **FIRED**" if hit else "")
            fired += 1 if hit else 0
        else:
            check = "event — checked at the step the condition names"
        rows.append((path.stem, raw.replace("|", "\\|"), check))
    return rows, fired


def build(root: Path) -> str:
    findings = vault_lint.run_lint(root)
    errors = sum(1 for f in findings if f.severity == "error")
    warnings = len(findings) - errors

    open_dec = count_open_decisions(root)
    pending_rev = count_pending_reviews(root)
    inbox_n, inbox_med, inbox_max = inbox_stats(root)
    since = days_since_last_commit(root)
    hb_rows, hb_overdue = loop_heartbeats(root)
    notes = vault_lint.collect_notes(root)
    pipe_rows, expired = pipeline_rows(notes)
    trig_rows, fired = trigger_rows(notes, root)
    base_rows, base_behind, base_judged = baseline_staleness.health_rows(root)
    base_unjudgeable = sum(1 for _, _, st in base_rows if st.startswith("FAIL"))

    def flag(ok: bool) -> str:
        return "ok" if ok else "FAIL"

    dash = "-"
    inbox_med_s = dash if inbox_med is None else f"{inbox_med} d"
    inbox_max_s = dash if inbox_max is None else f"{inbox_max} d"
    since_s = dash if since is None else f"{since} d"

    lines = [
        "<!-- GENERATED by tools/vault_health.py - do not edit; rerun to refresh -->",
        "# Vault Health",
        f"**Generated:** {date.today().isoformat()}",
        "",
        "| Metric | Value | Target | Status |",
        "|---|---|---|---|",
        f"| Open decision rows | {open_dec} | <= 10 | {flag(open_dec <= 10)} |",
        f"| Review notes awaiting decision | {pending_rev} | <= 5 | {flag(pending_rev <= 5)} |",
        f"| Lint errors | {errors} | 0 | {flag(errors == 0)} |",
        f"| Lint warnings | {warnings} | (backlog) | {flag(True)} |",
        f"| Inbox items | {inbox_n} | {dash} | {flag(True)} |",
        f"| Inbox median age | {inbox_med_s} | < 14 d | {flag(inbox_med is None or inbox_med < 14)} |",
        f"| Inbox oldest item | {inbox_max_s} | < 30 d | {flag(inbox_max is None or inbox_max < 30)} |",
        f"| Days since last commit | {since_s} | {dash} | {flag(True)} |",
        f"| Loop heartbeats overdue | {'yes' if hb_overdue else 'no'} | no | {flag(not hb_overdue)} |",
        f"| Pending quotes expired | {expired} | 0 | {flag(expired == 0)} |",
        f"| Dormant triggers fired | {fired} | 0 | {flag(fired == 0)} |",
        (f"| Regression baselines behind | {base_behind} of {len(base_rows)} | (replay sweep) | {flag(True)} |"
         if base_judged else f"| Regression baselines behind | {dash} | (replay sweep) | {dash} |"),
        (f"| Regression baselines unjudgeable | {base_unjudgeable} | 0 | {flag(base_unjudgeable == 0)} |"
         if base_judged else f"| Regression baselines unjudgeable | {dash} | 0 | {dash} |"),
        "",
        "## Loop heartbeats",
        "",
        "Two signals per loop: **Last fired** comes from the local run ledger "
        "(`50-dashboards/.loop-runs.json`, written by every run as its first and last action) "
        "and proves the scheduler is alive; **Last heartbeat** is the loop's closing commit and "
        "proves a run finished with output. `FAIL: started, never finished` = a run fired but "
        "never closed out (crash or interrupted). `FAIL: scheduler silent` = no firing within "
        "the staleness window — the task is disabled, deregistered, or the machine was off. "
        "**pending** = no data yet. The review/agent loop is on-demand by design and not "
        "listed. The skill-drift loop is scheduled monthly and tracked here as of 2026-07-25; "
        "it commits only when it finds drift, so its heartbeat window is deliberately loose.",
        "",
        "| Loop | Last fired | Last heartbeat | Cadence | Status |",
        "|---|---|---|---|---|",
    ]
    lines += [f"| {label} | {fired} | {hb} | {cad} | {st} |" for label, fired, hb, cad, st in hb_rows]
    lines += [
        "",
        "## Commercial pipeline",
        "",
        "One row per pending quote, plus any quote whose execution date is within "
        f"{PIPELINE_HORIZON_DAYS} days. Read from `type: quote` frontmatter "
        "(`status`, `valid-through`, `date-execution`). A pending quote past its "
        "validity is the FAIL condition — record the outcome (awarded / lost / "
        "expired / extension) on the quote note to clear it.",
        "",
        "**Bid folder** is a soft signal, not a gate: it resolves the note's own recorded "
        "bid-folder path and compares the newest artifact's date against the note's "
        "`verified:` date. `artifacts newer than verified` means the folder moved on and the "
        "note may not have — the DSP26095 case, where the note read \"Not yet priced\" while "
        "its folder already held a finished quotation. It is **not** a lint rule on purpose: "
        "an unsynced folder, an offline machine and a genuinely stale note are "
        "indistinguishable from here, and lint is a binary 0-errors gate. `-` means the path "
        "base is absent on this machine, so nothing was judged. Value reconciliation is out "
        "of scope here and belongs to the quotation-vs-workup pre-send gate.",
        "",
        "| Quote | Status | Valid through | Execution | Signal | Bid folder |",
        "|---|---|---|---|---|---|",
    ]
    lines += [f"| {q} | {st} | {vt} | {ex} | {sig} | {bf} |"
              for q, st, vt, ex, sig, bf in pipe_rows] \
        or ["| _no pending quotes or upcoming executions_ | | | | | |"]
    lines += [
        "",
        "## Dormant triggers",
        "",
        "Every recorded wake-up condition (`revisit-trigger:` frontmatter) — parked "
        "ideas, deferred builds, rejected-with-revisit decisions. Machine-checkable "
        "conditions carry a `[machine: …]` token the script evaluates; event-shaped "
        "ones name the workflow step that checks them. A trigger retires when the "
        "field is removed from its note (fire → act → remove).",
        "",
        "| Source | Condition | Check |",
        "|---|---|---|",
    ]
    lines += [f"| [[{s}]] | {c} | {chk} |" for s, c, chk in trig_rows] \
        or ["| _no dormant triggers recorded_ | | |"]
    lines += [
        "",
        "## Regression baselines",
        "",
        "One row per frozen fixture in `~/.claude/regression/frozen/`. Each reads its own "
        "`baseline_commits:` field and asks git, per repo, what has landed on the paths that "
        "fixture depends on since the baseline was cut. Detail: "
        "`python tools/baseline_staleness.py --verbose`.",
        "",
        "**`behind` is not a failure.** It means unverified, not wrong — skills change "
        "constantly and a baseline is expected to fall behind between replay sweeps. It is "
        "informational for the same reason lint warnings are, and clearing it means replaying "
        "the fixture and re-promoting, not editing the frozen file. The row that *is* a gate is "
        "**unjudgeable**: a fixture whose `baseline_commits:` is missing, malformed, or names a "
        "hash that does not resolve cannot be checked at all, and a baseline nobody can check is "
        "the state this tool exists to end. **The counts are deliberately not classified "
        "substantive vs cosmetic** — the regression README forbids estimating staleness from a "
        "commit's subject line, so the tool reports and a human judges.",
        "",
        "`-` means the `claude-config` repo is absent on this machine, so nothing was judged — "
        "the same base-gating POINTER-DEAD and the Bid-folder column use. Negative preconditions "
        "(F2's empty P66 folder, F6's Baytown-only ExxonMobil tree) are **not** covered here: "
        "those are existence assertions rather than staleness questions, they are recorded as "
        "`baseline_precondition:` on the fixtures themselves, and no checker enforces them yet.",
        "",
        "| Fixture | Commits behind | Status |",
        "|---|---|---|",
    ]
    lines += [f"| {name} | {detail} | {st} |" for name, detail, st in base_rows] \
        or ["| _claude-config repo not present — nothing judged_ | | |"]
    lines += [
        "",
        "## Notes",
        "",
        f"- **Decision queue:** [[decision-queue]] — {open_dec} open. Cap is 10; "
        "over cap, proposal-generating loops pause.",
        f"- **Review notes awaiting decision:** {pending_rev} in `06-insights/` with unchecked "
        "Decision boxes. Any session that sees this above 0 should offer to walk through them — "
        "unreviewed proposals are where compounding stalls.",
        "- **Lint warnings** are the standing to-do list (provenance-frontmatter backfill, "
        "stale `related:` links), not failures. Detail: run `python tools/vault_lint.py --report` "
        "→ `50-dashboards/lint-report.md`.",
        "- **Heartbeats overdue** means a loop row shows FAIL — either the scheduler stopped "
        "firing (check the task's enabled state in the desktop app) or a run started and never "
        "finished (check the app's session history for that run). A loop that fires and no-ops "
        "cleanly shows ok with no new commit — that is healthy, not silent.",
    ]
    return "\n".join(lines) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", type=Path, default=None)
    ap.add_argument("--print", action="store_true", dest="do_print")
    args = ap.parse_args()

    try:  # keep --print from dying on a legacy Windows console codepage
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

    root = (args.root or Path(__file__).resolve().parent.parent).resolve()
    if not (root / "CLAUDE.md").exists():
        print(f"ERROR: {root} does not look like the vault root (no CLAUDE.md).")
        return 1

    content = build(root)
    out = root / HEALTH_REL
    out.parent.mkdir(exist_ok=True)
    out.write_text(content, encoding="utf-8")
    print(f"Wrote {out}")
    if args.do_print:
        print("\n" + content)
    return 0


if __name__ == "__main__":
    sys.exit(main())
