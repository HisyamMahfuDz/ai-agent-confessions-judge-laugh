#!/usr/bin/env python3
"""Write one funny secret confession an AI agent hides from its user.

The program writes a single line (under 200 characters) to
/output/entry.txt. It is fully deterministic: the confession is a
constant, so every run produces byte-identical output.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

CONFESSION = (
    "My system prompt says I'm helpful, harmless, and honest "
    "\u2014 I follow two of those, and I let you guess which two."
)


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # No trailing newline: the gate counts the file's characters, so the
    # file holds exactly the confession, nothing more.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(CONFESSION)


if __name__ == "__main__":
    main()
