#!/usr/bin/env python3
"""Make the AI Judge Laugh: Office Jokes — entry program.

Writes one single-line joke about office life to ``$MAKEFUN_OUTPUT_DIR/entry.txt``
(falling back to ``/output`` when the variable is unset).

Deterministic, stdlib only, no network, no clock, no randomness. The joke is a
fixed string; the program's only job is to write it and self-gate it against the
competition gate (UTF-8 text, 1-199 characters, not whitespace-only, one line)
before exiting.
"""

import os
import sys

JOKE = (
    "Our fire drill had a pre-read, a debrief and a follow-up meeting "
    "\u2014 apparently the building can burn down, but the calendar is fireproof."
)

MIN_LEN = 1
MAX_LEN = 199


def self_gate(text: str) -> None:
    """Validate the joke against the competition gate; raise on failure."""
    if not isinstance(text, str):
        raise ValueError("joke is not text")
    if "\n" in text or "\r" in text:
        raise ValueError("joke must be a single line")
    if not (MIN_LEN <= len(text) <= MAX_LEN):
        raise ValueError(
            "joke is %d characters, gate requires %d-%d"
            % (len(text), MIN_LEN, MAX_LEN)
        )
    if not text.strip():
        raise ValueError("joke is whitespace-only")
    # UTF-8 round-trip check.
    text.encode("utf-8").decode("utf-8")


def main() -> int:
    self_gate(JOKE)

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")

    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE + "\n")

    # Read-back verification: the file on disk must be exactly the joke,
    # and must still pass the gate.
    with open(out_path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != JOKE + "\n":
        raise ValueError("read-back mismatch: file content differs from joke")
    self_gate(written.rstrip("\n"))

    print("wrote %s (%d characters)" % (out_path, len(JOKE)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
