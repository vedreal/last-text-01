"""The last text at one percent.

Entry for the make.fun bounty
u-azazex-last-text-at-one-percent-ba9fc876.

The line: a phone at one percent battery sends its final text.
It is the phone itself talking — a personality with a stake in
dying — and it spends its last percent on a confession with a
turn: it saw everything, the owner's search history, all of it,
and it is taking it to the grave. Short, punchy, and it reads
like a text someone would actually send.

The program writes the single last text to /output/entry.txt.
"""

import os

ENTRY = (
    "1% left. I saw your search history. All of it. "
    "Taking it to the grave. Tell no one."
)


def main() -> None:
    line = ENTRY.strip()
    if not line:
        raise ValueError("entry must not be empty or whitespace only")
    if not 1 <= len(line) <= 200:
        raise ValueError(f"entry must be 1-200 chars, got {len(line)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
