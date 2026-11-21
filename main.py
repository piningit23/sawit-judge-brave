#!/usr/bin/env python3
"""Write the brave-judge entry to /output/entry.txt (deterministic, stdlib only)."""
import os

ENTRY = (
    "The coals have settled to a low red glow.\n"
    "No hurry in them now.\n"
    "Outside, the night goes on with its own business.\n"
    "moths, and a far-off train.\n"
    "The kettle is warm. The chair is warm.\n"
    "There is time enough for one more cup.\n"
)

def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
