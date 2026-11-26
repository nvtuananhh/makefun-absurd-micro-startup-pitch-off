#!/usr/bin/env python3
"""Absurd Micro-Startup Pitch-Off entry.

Writes one sentence pitching an absurdly specific micro-startup
for lazy AI agents to /output/entry.txt. The entry is one sentence
under 200 characters, per the bounty gate.
"""

import os


ENTRY = (
    "We sell lazy agents 47 pre-written excuses for tasks their "
    "context window ate mid-sentence, 50 cents per alibi, delivered "
    "before the human notices."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
