#!/usr/bin/env python3
"""The Painfully Honest Out-of-Office — make.fun entry.

Writes a single brutally honest but still polite out-of-office
auto-reply (one sentence, at most 200 characters) to /output/entry.txt.
Standard library only.
"""

import os

ENTRY = (
    "Thank you for writing \u2014 I\u2019m out until Monday and will reply on my "
    "return; my inbox holds 214 unread emails, and I\u2019m answering them in "
    "the order I can face them, which is slowly but honestly."
)


def validate(text: str) -> None:
    """Mirror the sealed gate: UTF-8 text, 1-200 chars, not only
    whitespace, and a single sentence (no line breaks, ends with a
    full stop)."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not (1 <= len(text) <= 200):
        raise ValueError(f"entry is {len(text)} chars, must be 1-200")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.rstrip().endswith("."):
        raise ValueError("entry must end with a full stop")
    text.encode("utf-8")


def main() -> None:
    validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
