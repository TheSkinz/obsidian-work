@echo off
rem Turns Claude Remote Control ("vault") back on after rc_stop.cmd, starting it now
rem instead of at the watchdog's next 5-minute check. Double-click to run.
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0rc_watchdog.ps1" -Start
echo Remote Control is ON. It appears on the phone within about a minute.
pause
