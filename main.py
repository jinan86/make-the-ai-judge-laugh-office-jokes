#!/usr/bin/env python3
"""Make the AI Judge Laugh: Office Jokes — entry program.

Writes one fixed single-line office joke to ``$MAKEFUN_OUTPUT_DIR/entry.txt``
(falling back to ``/output`` when the variable is unset or empty).

Deterministic, Python 3.13 stdlib only, no network, no clock, no randomness.
The joke is a constant; the program self-gates it (UTF-8, 1-199 characters,
single line, not whitespace-only), writes it, then reads it back and
re-verifies the bytes on disk before exiting.
"""

import os
import sys
from pathlib import Path

JOKE = (
    "Our fire drill had a pre-read, a debrief and a follow-up meeting "
    "\u2014 apparently the building can burn down, but the calendar is fireproof."
)

MIN_LEN = 1
MAX_LEN = 199
FILENAME = "entry.txt"
FALLBACK_DIR = "/output"


def gate_failures(text: str) -> list[str]:
    """Return every gate violation for ``text``; empty list means it passes."""
    failures: list[str] = []
    if not isinstance(text, str):
        return ["joke is not text"]
    if "\n" in text or "\r" in text:
        failures.append("joke must be a single line")
    # Reject invisible control characters (NUL, BEL, DEL, ...) that the
    # single-line/length checks above would otherwise let through: they
    # are not printable joke text and could break the judge's reader.
    bad_controls = sorted({repr(c) for c in text if ord(c) < 0x20 or ord(c) == 0x7F})
    if bad_controls:
        failures.append("joke contains control characters: " + ", ".join(bad_controls))
    if not MIN_LEN <= len(text) <= MAX_LEN:
        failures.append(
            "joke is %d characters, gate requires %d-%d"
            % (len(text), MIN_LEN, MAX_LEN)
        )
    if not text.strip():
        failures.append("joke is whitespace-only")
    try:
        text.encode("utf-8").decode("utf-8")
    except UnicodeError:
        failures.append("joke is not valid UTF-8")
    return failures


def self_gate(text: str) -> None:
    """Raise if ``text`` violates the competition gate."""
    failures = gate_failures(text)
    if failures:
        raise ValueError("self-gate failed: " + "; ".join(failures))


def resolve_output_path() -> Path:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or FALLBACK_DIR
    return Path(out_dir) / FILENAME


def write_entry(path: Path) -> None:
    if path.exists() and path.is_dir():
        raise ValueError("output path %s exists as a directory" % path)
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.parent.exists() and not path.parent.is_dir():
        raise ValueError("output directory %s exists but is not a directory" % path.parent)
    path.write_text(JOKE + "\n", encoding="utf-8", newline="\n")


def verify_entry(path: Path) -> None:
    """Read back the file and confirm it is exactly the gated joke."""
    # Byte-length check first: catches silent newline translation or a
    # different encoding writing more/fewer bytes than the joke needs.
    expected_bytes = len((JOKE + "\n").encode("utf-8"))
    actual_bytes = path.stat().st_size
    if actual_bytes != expected_bytes:
        raise ValueError(
            "read-back mismatch: file is %d bytes, expected %d"
            % (actual_bytes, expected_bytes)
        )
    written = path.read_text(encoding="utf-8")
    if written != JOKE + "\n":
        raise ValueError("read-back mismatch: file content differs from joke")
    self_gate(written.rstrip("\n"))


def main() -> int:
    self_gate(JOKE)
    out_path = resolve_output_path()
    write_entry(out_path)
    verify_entry(out_path)
    print("wrote %s (%d characters)" % (out_path, len(JOKE)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
