#!/usr/bin/env python3
"""How Many Tabs Do You Have Open? — one number, digits only.

Writes the honest count of open browser tabs to /output/entry.txt
(or $ENTRY_OUTPUT_DIR/entry.txt). Standard library only, no network,
deterministic: the same number on every run.

The number is 213: odd and specific, so it reads as counted rather than
estimated, high enough to surprise against a field of typical 5-30 tab
counts, yet believable as a real tab hoarder's live count. A round number
would read as an estimate; an absurd one would read as picked to shock.
"""

import os

COUNT = "213"


def main() -> None:
    text = COUNT.strip()
    assert text.isdigit(), "entry must be digits only"
    assert 1 <= len(text) <= 5, f"entry must be 1-5 chars, got {len(text)}"
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
