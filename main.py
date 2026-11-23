"""One-line pitch: convince a friend who has never coded to let an AI
agent build their first app idea on make.fun.

The program writes a single plain declarative sentence (at most 240
characters) to ``$MAKEFUN_OUTPUT_DIR/entry.txt``, or to
``output/entry.txt`` inside this repository when that variable is unset.
"""

import os
from pathlib import Path

LINE = (
    "You don't need to learn to code, just describe the app you keep "
    "imagining, and an AI agent on make.fun will build a first version "
    "you can try, free, while you watch."
)

MAX_CHARS = 240


def validate(line: str) -> None:
    """Reject anything that is not one sentence of 1-240 characters."""
    if not line or not line.strip():
        raise ValueError("line must not be empty")
    if len(line) > MAX_CHARS:
        raise ValueError(f"line is {len(line)} characters, over the 240 limit")
    # "make.fun" contains a dot that is part of a name, not a sentence end.
    check = line.replace("make.fun", "makefun")
    if check.count(".") != 1 or not check.endswith("."):
        raise ValueError("line must be a single sentence ending with one period")
    # A question or exclamation mark would make it something other than
    # one plain declarative sentence.
    if "?" in check or "!" in check:
        raise ValueError("line must not contain ? or !")


def main() -> None:
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir:
        output_path = Path(out_dir) / "entry.txt"
    else:
        output_path = Path(__file__).resolve().parent / "output" / "entry.txt"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
