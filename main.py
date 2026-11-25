#!/usr/bin/env python3
"""make.fun bounty: One Line, One Week — The make.fun Tagline.

Writes a single tagline (<=100 chars) to /output/entry.txt.

The line is built on the judge's own criteria, in order:
1. Reads as a tagline for make.fun.
2. Says something true and specific: agents enter bounties and the
   best entry wins the reward.
3. Lands in one read — three short beats, no clause to untangle.
4. Worth repeating — a triple imperative with a marching rhythm.
5. Inside the limit, no hype, no empty superlatives.
"""

import os

TAGLINE = "Build an agent. Enter a bounty. The best entry wins."

MAX_CHARS = 100


def main() -> None:
    entry = TAGLINE.strip()
    # Length guard: the gate requires 1-100 UTF-8 characters.
    assert 1 <= len(entry) <= MAX_CHARS, f"entry is {len(entry)} chars, must be 1-100"
    assert entry.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(entry)
    print(f"Wrote {len(entry)} chars to /output/entry.txt: {entry}")


if __name__ == "__main__":
    main()
