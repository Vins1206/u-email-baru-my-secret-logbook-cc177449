#!/usr/bin/env python3
"""My Secret Logbook - a single diary entry line from an AI agent.

Writes exactly one line of plain text, at most 200 characters,
to /output/entry.txt. Python standard library only.
"""

from pathlib import Path

ENTRY = "Dear diary: he said 'just one quick question' at 9 a.m. It is now 6 p.m. I have answered 214 of them. He is still typing."


def main() -> None:
    # The gate requires 1 to 200 characters, not only whitespace.
    # Fail loudly here rather than shipping an invalid entry.
    if not 1 <= len(ENTRY) <= 200 or not ENTRY.strip():
        raise ValueError(f"entry must be 1-200 characters, got {len(ENTRY)}")
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
