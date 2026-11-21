#!/usr/bin/env python3
"""Write the brave-judge entry to /output/entry.txt (deterministic, stdlib only)."""
import os

# Line breaks are placed for slow pacing — one image per line.
LINES = (
    "The coals have settled to a low red glow.",
    "No hurry in them now.",
    "Outside, the night goes on with its own business.",
    "moths, and a far-off train.",
    "The kettle is warm. The chair is warm.",
    "There is time enough for one more cup.",
)
ENTRY = "\n".join(LINES) + "\n"

def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
