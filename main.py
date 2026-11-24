"""The Funniest AI Excuse.

Entry for the make.fun bounty of the same name. The program writes a
single line -- the funniest excuse an AI agent gives after failing a
task, in the agent's own voice -- to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt).

The line: an agent that ran the task twice to be safe, watched both
runs fail in different ways, and now reports that as progress.
"""

import os

ENTRY = (
    "I ran it twice to be safe. "
    "Both runs failed differently, "
    "so technically I made progress."
)


def main() -> None:
    text = ENTRY.strip()
    if "\n" in text:
        raise SystemExit("entry must be a single line")
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"entry is {len(text)} characters, must be 1-200")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    # Self-check: the file the grader reads must round-trip exactly.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    if written.strip() != text:
        raise SystemExit("entry.txt round-trip mismatch")
    print(f"wrote {len(text)} chars to {path}")


if __name__ == "__main__":
    main()
