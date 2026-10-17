# rc_watchdog.ps1 - keeps Claude Remote Control ("vault") running on Linda2.
#
# Run by the scheduled task "Claude Remote Control vault" at logon and every 5 minutes,
# under `conhost --headless` so no window ever appears. Each run takes about a second:
#   - Remote Control not running      -> start it (hidden), via start_remote_control.cmd
#   - more than one copy running      -> log a warning, touch nothing (the phone shows duplicates)
#   - Claude Code updated since start -> restart it once no phone session is open,
#                                        or during 03:00-04:59 regardless
#   - hourly (every run while failing) -> one real round trip on the claude.ai login,
#                                        result to logs\rc_login.json; restart on recovery
# A running server keeps launching sessions from the build it started with, so after an
# update new sessions fail until it restarts (anthropics/claude-code#84817).
# A server whose CLI login has expired still counts as running (the 2026-10-16 outage), and
# `claude auth status` only reads the stored token, so the login check makes a real request.
#
# Every start, stop and warning goes to logs\rc_watchdog.log (rotated at 1 MB).
# Turn it off/on on purpose with rc_stop.cmd / rc_start.cmd, which call -Stop / -Start.
# See 08-systems/mobile-field-access.md.

param([switch]$Stop, [switch]$Start)

$ErrorActionPreference = 'Stop'
$Tools       = $PSScriptRoot
$Vault       = Split-Path $Tools
$LogDir      = Join-Path $Tools 'logs'
$Log         = Join-Path $LogDir 'rc_watchdog.log'
$StopFlag    = Join-Path $LogDir 'rc.stop'
$VersionFile = Join-Path $LogDir 'rc_server_version.txt'
$Runner      = Join-Path $Tools 'start_remote_control.cmd'
$Pkg         = Join-Path $env:APPDATA 'npm\node_modules\@anthropic-ai\claude-code\package.json'
$ClaudeExe   = Join-Path $env:APPDATA 'npm\node_modules\@anthropic-ai\claude-code\bin\claude.exe'
$LoginFile   = Join-Path $LogDir 'rc_login.json'
$TaskName    = 'Claude Remote Control vault'

New-Item -ItemType Directory -Force $LogDir | Out-Null

function Write-Log([string]$msg) {
    if ((Test-Path $Log) -and (Get-Item $Log).Length -gt 1MB) { Move-Item -Force $Log "$Log.old" }
    Add-Content -Path $Log -Value ('[{0:yyyy-MM-dd HH:mm:ss}] {1}' -f (Get-Date), $msg)
}

function Get-InstalledVersion {
    try { (Get-Content -Raw $Pkg | ConvertFrom-Json).version } catch { 'unknown' }
}

function Get-Servers {
    # The server, not its sessions: sessions are child claude.exe processes run with --sdk-url.
    @(Get-CimInstance Win32_Process -Filter "Name='claude.exe'" |
        Where-Object { $_.CommandLine -match '\s(remote-control|rc)(\s|$)' -and $_.CommandLine -match '--name\s+"?vault' })
}

function Start-Runner([string]$why) {
    Set-Content $VersionFile (Get-InstalledVersion)
    Write-Log "Starting Remote Control ($why), Claude Code $(Get-InstalledVersion)."
    Start-Process -FilePath $env:ComSpec -ArgumentList "/c `"$Runner`"" -WorkingDirectory $Vault -WindowStyle Hidden
}

function Stop-Servers([string]$why) {
    foreach ($s in Get-Servers) {
        Write-Log "Stopping Remote Control PID $($s.ProcessId) ($why)."
        & taskkill.exe /PID $s.ProcessId /T /F | Out-Null
    }
}

function Get-LastLogin {
    try { Get-Content -Raw $LoginFile | ConvertFrom-Json } catch { $null }
}

function Test-Login {
    # One headless request on the subscription login Remote Control uses: the API key is
    # removed for this process only, exactly as start_remote_control.cmd does. ~5 s when healthy.
    try {
        $psi = New-Object System.Diagnostics.ProcessStartInfo $ClaudeExe
        $psi.Arguments = '-p "Reply with the single word OK." --model haiku --no-session-persistence --max-turns 1'
        $psi.WorkingDirectory = $env:TEMP
        $psi.UseShellExecute = $false
        $psi.CreateNoWindow = $true
        $psi.RedirectStandardInput = $true
        $psi.RedirectStandardOutput = $true
        $psi.RedirectStandardError = $true
        foreach ($v in 'ANTHROPIC_API_KEY', 'ANTHROPIC_AUTH_TOKEN') { $psi.EnvironmentVariables.Remove($v) }
        $p = [System.Diagnostics.Process]::Start($psi)
        $p.StandardInput.Close()
        $out = $p.StandardOutput.ReadToEndAsync()
        $err = $p.StandardError.ReadToEndAsync()
        if (-not $p.WaitForExit(90000)) {
            & taskkill.exe /PID $p.Id /T /F | Out-Null
            return @{ ok = $false; detail = 'no reply within 90 s' }
        }
        $text = (($out.Result + ' ' + $err.Result) -replace '\s+', ' ').Trim()
        if ($text.Length -gt 200) { $text = $text.Substring(0, 200) }
        return @{ ok = ($p.ExitCode -eq 0 -and $text -match '\bOK\b'); detail = "exit $($p.ExitCode): $text" }
    } catch {
        return @{ ok = $false; detail = "probe error: $($_.Exception.Message)" }
    }
}

if ($Stop) {
    Set-Content $StopFlag "Stopped by rc_stop.cmd at $(Get-Date). Delete this file or run rc_start.cmd to resume."
    Stop-Servers 'rc_stop.cmd'
    Write-Log 'Watchdog standing down until rc_start.cmd.'
    exit 0
}

if ($Start) {
    if (Test-Path $StopFlag) { Remove-Item $StopFlag; Write-Log 'Resumed by rc_start.cmd.' }
    # fall through and act now rather than waiting for the next 5-minute tick
}

if (Test-Path $StopFlag) { exit 0 }

# Login check: hourly while it passes, every run while it fails so recovery shows within 5 min.
$last = Get-LastLogin
$due  = $true
if ($last -and $last.ok) {
    try { $due = ((Get-Date) - [datetime]$last.checked).TotalMinutes -ge 55 } catch { $due = $true }
}
if ($due) {
    $r = Test-Login
    @{ checked = (Get-Date).ToString('yyyy-MM-ddTHH:mm:sszzz'); ok = $r.ok; detail = $r.detail } |
        ConvertTo-Json | Set-Content -Encoding UTF8 $LoginFile
    $wasOk = -not $last -or $last.ok
    if ($wasOk -and -not $r.ok) {
        Write-Log "LOGIN CHECK FAILED ($($r.detail)). Remote Control is up but cannot serve sessions. Fix at the box (RustDesk): run claude, then /login."
    } elseif (-not $wasOk -and $r.ok) {
        # The server may still hold the dead credentials; restart it onto the fresh login.
        Write-Log 'Login check OK again.'
        if (@(Get-Servers).Count -gt 0) {
            Stop-Servers 'login restored'
            Start-Sleep -Seconds 5
            Start-Runner 'restart after login restored'
            exit 0
        }
    }
}

$servers = Get-Servers

if ($servers.Count -gt 1) {
    Write-Log ("WARNING: {0} Remote Control 'vault' copies running (PIDs {1}). The phone will list duplicates. Leaving them alone; close the one started by hand." -f $servers.Count, ($servers.ProcessId -join ', '))
    exit 0
}

if ($servers.Count -eq 0) {
    Start-Runner 'not running'
    exit 0
}

# Exactly one copy. Restart it if Claude Code has updated since it started.
$server    = $servers[0]
$installed = Get-InstalledVersion
if (-not (Test-Path $VersionFile)) {
    # Started outside the watchdog (by hand, or before it existed): adopt it as current.
    Set-Content $VersionFile $installed
    exit 0
}
$running = (Get-Content -Raw $VersionFile).Trim()
if ($installed -eq 'unknown' -or $installed -eq $running) { exit 0 }

$sessions = @(Get-CimInstance Win32_Process -Filter "Name='claude.exe' AND ParentProcessId=$($server.ProcessId)")
$quiet    = (Get-Date).Hour -in 3, 4
if ($sessions.Count -eq 0 -or $quiet) {
    Stop-Servers "Claude Code updated $running -> $installed, $($sessions.Count) session(s) open"
    Start-Sleep -Seconds 5
    Start-Runner 'restart after update'
}
