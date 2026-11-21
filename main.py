#!/usr/bin/env python3
"""A short evening vignette, saved as the entry file.

No clock, no dice, no network: the same six sentences every run,
so the result is identical byte for byte each time it is produced.
"""
from pathlib import Path

# Each sentence is one unhurried beat, so the reader settles in
# line by line instead of being told to slow down.
evening_beats = [
    "The coals have settled to a low red glow.",
    "No hurry in them now.",
    "Outside, the night goes on with its own business.",
    "moths, and a far-off train.",
    "The kettle is warm. The chair is warm.",
    "There is time enough for one more cup.",
]

destination = Path("/output/entry.txt")
text_encoding = "utf-8"  # plain text, same bytes on every machine


def compose_evening() -> str:
    """Stitch the evening beats into one trailing-newline text block."""
    return "\n".join(evening_beats) + "\n"


def main() -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(compose_evening(), encoding=text_encoding)


if __name__ == "__main__":
    main()
