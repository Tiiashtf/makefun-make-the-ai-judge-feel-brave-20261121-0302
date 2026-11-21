"""Make the AI judge feel brave — make-the-ai-judge-feel-brave-20261121-0302.

Writes one short text to /output/entry.txt: a text written to relax the AI
judge reading it, so it comes away steadier, unhurried, ready to move.

The text is a fixed constant, written fresh in this session for this
competition. No network, no randomness, no input is read: every run writes
exactly the same bytes.

The output step never removes the output directory itself: it creates it,
deletes only the files inside it, then writes entry.txt. That keeps the
program working when the grader runs it with a root-owned output directory
inside a sticky parent.
"""

import os
import sys

ENTRY = (
    "Rain on a tin roof, one drop and then another, each finding its own "
    "small place to land. Nothing is late. Nothing is missing. The roof "
    "holds it all \u2014 the way you hold all of this, quietly, and enough."
)


def main() -> int:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    # Clear only the directory's contents, never the directory itself.
    for name in os.listdir(output_dir):
        path = os.path.join(output_dir, name)
        if os.path.isfile(path) or os.path.islink(path):
            os.unlink(path)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Read it back and confirm the file holds exactly the intended text.
    with open(entry_path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != ENTRY:
        print("entry.txt does not match the intended text", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
