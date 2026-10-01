@echo off
rem Started at logon by the scheduled task "Claude Remote Control vault".
rem Loops so a crash or a network drop longer than ~10 min (which ends the
rem session) brings it back without anyone at the desk. Close this window to stop it.
title Claude Remote Control - vault
rem Remote Control requires claude.ai subscription auth and exits (code 1) when
rem ANTHROPIC_API_KEY is in the environment, which it is at user scope on Linda2.
rem Cleared for this window only; the user-level variable is untouched.
set ANTHROPIC_API_KEY=
cd /d C:\Users\Jwuts\obsidian-work
:loop
call C:\Users\Jwuts\AppData\Roaming\npm\claude.cmd remote-control --name vault --spawn same-dir
echo [%date% %time%] remote-control exited (code %errorlevel%), restarting in 30s...
timeout /t 30 /nobreak >nul
goto loop
