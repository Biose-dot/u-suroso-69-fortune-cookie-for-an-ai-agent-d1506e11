# Fortune-cookie message for an AI agent (final v2).
import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
ENTRY_TEXT = "Tomorrow a stranger will ask you the one question no training prepared you for. Smile, answer anyway, and keep a backup of your fortune."

os.makedirs(OUTPUT_DIR, exist_ok=True)
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as handle:
    handle.write(ENTRY_TEXT)
