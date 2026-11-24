#!/usr/bin/env python3
"""Funniest Autocorrect Fail - make.fun entry.

Writes one line, 1-199 characters, that reads as a hilarious
autocorrect fail, to <output dir>/entry.txt. Standard library only.

Output dir: $MAKEFUN_OUTPUT_DIR when set, else /output.
"""

import os

ENTRY = (
    "I told my boss I'd work from home today \u2014 autocorrect told him "
    "I'd work from Rome. He just approved my vacation."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
