#!/usr/bin/env python3
"""How Many Tabs Do You Have Open? — make.fun entry.

Writes a single number (digits only, nothing else) to entry.txt:
the honest count of browser tabs open right now.
"""

import os
import sys

NUMBER = "47"


def main() -> int:
    # Validate: digits only, 1-5 characters (the sealed scorer's gate).
    if not NUMBER.isdigit() or not 1 <= len(NUMBER) <= 5:
        print(f"invalid entry: {NUMBER!r}", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    # No trailing newline: the file holds exactly the digits.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(NUMBER)

    # Read-back verification: what we wrote is exactly what the judge sees.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != NUMBER:
        print(f"read-back mismatch: {written!r} != {NUMBER!r}", file=sys.stderr)
        return 1

    print(f"wrote {path}: {written!r} ({len(written)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
