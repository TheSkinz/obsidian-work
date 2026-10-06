#!/usr/bin/env python3
"""remote_access_check.py — pre-departure check that Linda2 stays reachable.

WHY THIS EXISTS. Linda2 was unreachable from the road twice, on 2026-09-16 and
2026-09-23, and both times the trigger was a Windows Update restart in the early
morning (System event 1074, TrustedInstaller). The machine came back and logged
itself in each time, but nothing remote-facing did: RustDesk was a portable app
with no service, and `claude remote-control` had nothing to start it. On
2026-10-01 a third update restart landed mid-session at the desk, and RustDesk
did not survive that one either.

The standing design (see 08-systems/mobile-field-access.md) is two doors that
each survive an unattended restart: RustDesk installed as a service (GUI, lock
screen, UAC, re-logins) and Claude Remote Control started at logon by a
scheduled task (the vault, with all skills). This script checks the conditions
those doors depend on. It is read-only.

Run it as the last step before leaving town:

    python tools/remote_access_check.py --return-date 2026-10-20

PASS on every line does not replace the restart test. The acceptance test is to
restart, then reach both doors from the phone on cellular.
"""

import argparse
import datetime as dt
import json
import subprocess
import sys
from pathlib import Path

TASK_NAME = "Claude Remote Control vault"
LOG_DIR = Path(__file__).resolve().parent / "logs"

PROBE = r"""
$ErrorActionPreference = 'SilentlyContinue'
$svc = Get-Service -Name 'RustDesk'
$task = Get-ScheduledTask -TaskName '%TASK%'
$rc = Get-CimInstance Win32_Process | Where-Object { $_.Name -match '^(claude|node)\.exe$' -and $_.CommandLine -match '\s(remote-control|rc)(\s|$)' -and $_.CommandLine -match '--name\s+"?vault' }
$ux = Get-ItemProperty 'HKLM:\SOFTWARE\Microsoft\WindowsUpdate\UX\Settings'
$wl = Get-ItemProperty 'HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon'
[pscustomobject]@{
  svc_status    = if ($svc) { [string]$svc.Status } else { $null }
  svc_start     = if ($svc) { [string]$svc.StartType } else { $null }
  task_state    = if ($task) { [string]$task.State } else { $null }
  task_action   = if ($task) { [string]$task.Actions[0].Arguments } else { $null }
  task_repeat   = if ($task) { (@($task.Triggers | ForEach-Object { $_.Repetition.Interval }) | Where-Object { $_ }) -join ',' } else { $null }
  task_next     = if ($task) { [string](Get-ScheduledTaskInfo -TaskName '%TASK%').NextRunTime } else { $null }
  rc_count      = @($rc).Count
  pause_until   = [string]$ux.PauseUpdatesExpiryTime
  autologon     = [string]$wl.AutoAdminLogon
  autologon_user= [string]$wl.DefaultUserName
} | ConvertTo-Json -Compress
""".replace("%TASK%", TASK_NAME)


def probe():
    out = subprocess.run(
        ["powershell", "-NoProfile", "-Command", PROBE],
        capture_output=True, text=True, check=False,
    )
    return json.loads(out.stdout.strip())


def parse_pause(raw):
    if not raw:
        return None
    try:
        return dt.datetime.fromisoformat(raw.replace("Z", "+00:00")).date()
    except ValueError:
        return None


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--return-date", type=dt.date.fromisoformat,
                    help="YYYY-MM-DD; updates must stay paused past this date")
    args = ap.parse_args()

    s = probe()
    pause = parse_pause(s["pause_until"])
    rows = []

    rows.append((
        s["svc_status"] == "Running" and s["svc_start"] == "Automatic",
        "RustDesk service running, start Automatic",
        f"status={s['svc_status']} start={s['svc_start']}" if s["svc_status"]
        else "no RustDesk service — portable app only, will not survive a restart",
    ))
    rows.append((
        s["task_state"] is not None,
        f"Scheduled task '{TASK_NAME}' exists",
        f"state={s['task_state']}" if s["task_state"] else "missing",
    ))
    rows.append((
        "rc_watchdog.ps1" in (s["task_action"] or "") and "PT5M" in (s["task_repeat"] or "")
        and bool(s["task_next"]),
        "Task runs the hidden watchdog every 5 minutes",
        f"repeat={s['task_repeat']} next run={s['task_next'] or 'NONE — repeat only starts at next logon'}"
        if s["task_action"] else "no task action",
    ))
    stopped = (LOG_DIR / "rc.stop").exists()
    if stopped:
        rc_detail = "turned off with rc_stop.cmd — run rc_start.cmd"
    elif s["rc_count"] > 1:
        rc_detail = f"{s['rc_count']} copies — the phone lists duplicates; close the hand-started one"
    else:
        rc_detail = f"{s['rc_count']} process(es)"
    rows.append((
        s["rc_count"] == 1 and not stopped,
        "Exactly one Remote Control 'vault' process running",
        rc_detail,
    ))
    if args.return_date:
        ok = pause is not None and pause > args.return_date
        detail = f"paused until {pause}, return {args.return_date}" if pause \
            else "updates not paused"
    else:
        ok = pause is not None and pause > dt.date.today()
        detail = (f"paused until {pause} (pass --return-date to compare)"
                  if pause else "updates not paused")
    rows.append((ok, "Windows Update paused past return", detail))
    rows.append((
        s["autologon"] == "1",
        "Autologon on (doors that start at logon need a logon)",
        f"AutoAdminLogon={s['autologon']} user={s['autologon_user']}",
    ))

    for ok, label, detail in rows:
        print(f"{'PASS' if ok else 'FAIL'}  {label} — {detail}")
    log = LOG_DIR / "rc_watchdog.log"
    if log.exists():
        print("\nLast watchdog events:")
        for line in log.read_text(encoding="utf-8", errors="replace").splitlines()[-5:]:
            print(f"  {line}")
    failed = sum(1 for ok, _, _ in rows if not ok)
    print(f"\n{len(rows) - failed}/{len(rows)} pass. "
          "Then restart and reach both doors from the phone on cellular.")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
