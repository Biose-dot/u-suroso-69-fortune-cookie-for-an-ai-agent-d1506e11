"""Writes the bounty entry text to entry.txt.

The output directory comes from MAKEFUN_OUTPUT_DIR (default /output).
The entry is written exactly as-is, with no trailing newline.
"""

import os

ENTRY = "Your next bug will vanish the moment you show it to someone else. The machines believe in you, they have no choice."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    entry_path = os.path.join(out_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
