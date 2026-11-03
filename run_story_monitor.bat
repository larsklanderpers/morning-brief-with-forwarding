@echo off
REM ─────────────────────────────────────────────────────────────────────────────
REM  run_story_monitor.bat
REM  Windows Task Scheduler entry point for the AI Product Story Monitor.
REM
REM  What it does:
REM    1. Changes to the project directory
REM    2. Runs `claude` non-interactively with the /story-monitor slash command
REM    3. Claude searches the five threads, builds the HTML briefing, and
REM       calls story_monitor_draft.py to push the draft to Gmail via IMAP.
REM
REM  Setup (one-time):
REM    - Make sure `claude` is on your PATH  (run `claude --version` to verify)
REM    - Set ANTHROPIC_API_KEY in System Environment Variables, or add it below
REM    - Task Scheduler: Action → Start a Program → this .bat file
REM      Suggested schedule: daily at 05:00 (after the morning briefs run)
REM
REM  To test manually:
REM    Double-click this file, or in cmd:  cd /d D:\vc-personal-projects\... && run_story_monitor.bat
REM ─────────────────────────────────────────────────────────────────────────────

setlocal

REM Project root
set PROJECT=D:\vc-personal-projects\Morning Brief with Forwarding
cd /d "%PROJECT%"

REM If ANTHROPIC_API_KEY is not already in the environment, set it here:
REM set ANTHROPIC_API_KEY=sk-ant-...

REM Log file — one per day, kept in .claude\
set LOGFILE=%PROJECT%\.claude\story_monitor_%DATE:~10,4%-%DATE:~4,2%-%DATE:~7,2%.log

REM Run Claude Code non-interactively with the /story-monitor slash command.
REM --dangerously-skip-permissions lets it run the bash/python tools without prompting.
REM Remove that flag if you want to approve each tool use manually.
echo [%DATE% %TIME%] Starting story monitor >> "%LOGFILE%"

claude --dangerously-skip-permissions -p "/story-monitor" >> "%LOGFILE%" 2>&1

echo [%DATE% %TIME%] Finished. Exit code: %ERRORLEVEL% >> "%LOGFILE%"
endlocal
