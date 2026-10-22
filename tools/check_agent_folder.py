#!/usr/bin/env python3
"""Check the minimum contracts for a folder-based Endpoint agent."""

from pathlib import Path
import sys


REQUIRED_FILES = ["identity.md", "rules.md", "lessons.md", "boot-prompt.txt", "ROUTER.md", "state.md"]
MARKERS = {
    "identity.md": ["one job", "the bar"],
    "rules.md": ["lessons.md", "self-critique"],
    "ROUTER.md": ["read", "skip", "tools", "output", "return"],
    "boot-prompt.txt": ["lessons.md", "router.md"],
}


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: python check_agent_folder.py <agent-folder>", file=sys.stderr)
        return 2
    folder = Path(sys.argv[1])
    problems: list[str] = []
    for name in REQUIRED_FILES:
        if not (folder / name).is_file():
            problems.append(f"missing file: {name}")
    reference = folder / "reference"
    if not reference.is_dir() or not any(reference.glob("*.md")):
        problems.append("reference/ must contain at least one markdown brain/source file")
    for name, markers in MARKERS.items():
        path = folder / name
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8", errors="ignore").lower()
        for marker in markers:
            if marker not in text:
                problems.append(f"{name} lacks contract marker: {marker}")
    print(f"Checking agent folder: {folder}\n")
    if problems:
        print("FAIL - agent folder is not ready for a real test:")
        for problem in problems:
            print(f"  - {problem}")
        return 1
    print("PASS - folder contracts exist. Denzel's real-work test is still required.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

