@echo off
rem Turns Claude Remote Control ("vault") off on purpose. The watchdog stays scheduled
rem but stands down until rc_start.cmd. Double-click to run.
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0rc_watchdog.ps1" -Stop
echo Remote Control is OFF. Run rc_start.cmd to turn it back on.
pause
