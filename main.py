#!/usr/bin/env python3
"""One Letter: Coffee or Tea — entry program.

Writes exactly one letter, "A" (coffee), with no trailing newline,
to entry.txt inside the output directory given by MAKEFUN_OUTPUT_DIR
(fallback "/output").

Standard library only, no network, deterministic.
"""

import os
import sys

LETTER = "A"


def validate_letter(letter: str) -> None:
    if len(letter) != 1 or letter.isspace():
        raise ValueError("letter must be exactly 1 non-whitespace character")


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    validate_letter(LETTER)

    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)

    print(f"wrote {path}: {LETTER!r}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
