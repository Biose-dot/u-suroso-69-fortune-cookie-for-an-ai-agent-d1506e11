#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent — make.fun entry.

Writes the entry text to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

Fortune-cookie shape with an agent's own vocabulary: prompts and HTTP status codes as lucky numbers.
"""
import os

ENTRY = 'Your next prompt will be the one you meant to send the first time. Lucky numbers: 404, 200, 500.'


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
