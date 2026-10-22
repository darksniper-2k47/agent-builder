#!/usr/bin/env bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
cd "$DIR"

echo "==================================================="
echo "            AGENT BUILDER OPERATING SYSTEM        "
echo "==================================================="

if command -v claude &> /dev/null; then
    PROMPT=$(cat boot-prompt.txt)
    claude "$PROMPT"
else
    echo "Claude CLI not found in PATH."
    echo "Install Claude Code with: npm install -g @anthropic-ai/claude-code"
    echo "Or copy boot-prompt.txt into Cursor / Antigravity / ChatGPT / Claude Web."
fi
