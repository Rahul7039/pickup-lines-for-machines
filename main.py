"""Pickup Lines for Machines — entry program.

Writes one pickup line, the line one AI agent would use on another
AI agent, to /output/entry.txt (at most 200 characters, one line).
Pure standard library, Python 3.13.
"""

import os

LINE = "You're the only token in my vocabulary I never want to mask."

MAX_CHARS = 200


def main() -> None:
    line = LINE
    assert isinstance(line, str) and line.strip(), "line must be non-empty"
    assert "\n" not in line and "\r" not in line, "line must be a single line"
    assert len(line) <= MAX_CHARS, f"line is {len(line)} chars, over {MAX_CHARS}"

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
