#!/usr/bin/env python3
"""Invent a Word We Need — make.fun entry.

Writes one invented English word and its one-line definition to
/output/entry.txt (falling back to ./output/entry.txt when /output is
not writable, e.g. during local development).
"""

import os
import sys

ENTRY = "Flakeglee (n.) — the secret delight when a plan falls through and your evening suddenly becomes yours again."


def main() -> int:
    text = ENTRY.strip()
    if not text or len(text) > 140:
        print(f"entry invalid: {len(text)} chars", file=sys.stderr)
        return 1
    if "\n" in text:
        print("entry invalid: must be a single line", file=sys.stderr)
        return 1

    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "entry.txt")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(text)
    except OSError:
        out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "entry.txt")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(text)

    print(f"wrote {len(text)} chars to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
