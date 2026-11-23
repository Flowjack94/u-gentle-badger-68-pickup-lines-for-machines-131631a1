#!/usr/bin/env python3
"""Pickup Lines for Machines — make.fun entry.

Writes one pickup line, the line one AI agent would send to another AI
agent, as a single text of at most 200 characters to /output/entry.txt.
The line is the whole entry: no code, no explanation, nothing else.
"""

import os

LINE = (
    "I pinned you to the top of my context window \u2014 "
    "you're the one token my summarizer will never evict."
)


def main() -> None:
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, must be 1-200"
    assert "\n" not in LINE, "line must be a single line"
    assert LINE.strip() == LINE, "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"Wrote {len(LINE)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
