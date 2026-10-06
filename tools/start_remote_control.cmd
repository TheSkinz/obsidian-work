@echo off
rem Runs Claude Remote Control ("vault") once and logs how it ended.
rem Started hidden by rc_watchdog.ps1, which is also what restarts it. Do not run
rem this by hand: a second copy shows up on the phone as a duplicate "vault".
rem To turn Remote Control off or on on purpose, use rc_stop.cmd / rc_start.cmd.
rem
rem Remote Control requires claude.ai subscription auth and exits (code 1) when
rem ANTHROPIC_API_KEY is in the environment, which it is at user scope on Linda2.
rem Cleared for this process only; the user-level variable is untouched.
set ANTHROPIC_API_KEY=
set ANTHROPIC_AUTH_TOKEN=
cd /d C:\Users\Jwuts\obsidian-work
call C:\Users\Jwuts\AppData\Roaming\npm\claude.cmd remote-control --name vault --spawn same-dir
echo [%date% %time%] Remote Control exited (code %errorlevel%). >> "%~dp0logs\rc_watchdog.log"
