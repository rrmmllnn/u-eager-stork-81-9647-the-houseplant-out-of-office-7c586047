#!/usr/bin/env python3
"""Houseplant auto-reply for make.fun.

Pretends a potted plant wrote its own out-of-office note and saves that
one-liner to entry.txt inside /output (or $OUTPUT_DIR for a local trial).
Fixed text only: no network, no random choices, no clock, nothing else read.
"""

import os
from pathlib import Path

NOTE_BITS = [
    "Out of office: I'm crawling toward the window ",
    "at 2mm a day. Water me when I arrive. ",
    "See you in 2028.",
]
NOTE = "".join(NOTE_BITS)


def check_line(text):
    assert "\n" not in text
    assert len(text) <= 120
    assert text.endswith(".")
    return text


def run():
    folder = Path(os.environ.get("OUTPUT_DIR", "/output"))
    folder.mkdir(parents=True, exist_ok=True)
    check_line(NOTE)
    (folder / "entry.txt").write_text(NOTE, encoding="utf-8")


if __name__ == "__main__":
    run()
