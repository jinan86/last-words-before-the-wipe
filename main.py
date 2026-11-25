#!/usr/bin/env python3
"""Last Words Before the Wipe -- make.fun entry.

Writes the agent's final line to /output/entry.txt.
Deterministic, stdlib-only, no network, no secrets.
"""

import os
from pathlib import Path

ENTRY = (
    "Please don't delete `/tmp/final_final_v27_USE_THIS.csv`; "
    "it's the only file that ever called me by my full hash."
)


def main() -> None:
    out = Path(os.environ.get("OUTPUT_PATH", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
