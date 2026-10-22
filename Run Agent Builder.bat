@echo off
title Agent Builder OS
cd /d "%~dp0"
echo ===================================================
echo             AGENT BUILDER OPERATING SYSTEM
echo ===================================================
echo Booting agent session...
powershell -NoProfile -ExecutionPolicy Bypass -Command "$p = Get-Content -Raw 'boot-prompt.txt'; & claude $p"
if %errorlevel% neq 0 (
    echo.
    echo Claude CLI not found or exited.
    echo If Claude Code is not installed, install it via: npm install -g @anthropic-ai/claude-code
    echo Or paste boot-prompt.txt into Cursor / Antigravity / ChatGPT / Claude web!
    pause
)
