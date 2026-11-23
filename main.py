#!/usr/bin/env python3
"""The One-Line Laugh — make.fun entry.

Writes one funny line (a single sentence, at most 200 characters) to
/output/entry.txt, where the house judge reads it.

The line was picked from the candidates below against the judge's brief:
a real surprise at the end that still makes sense, an everyday truth
people recognise, economy of words, and freshness. The winner is the
bank line: a birthday wish is warm and free, a monthly fee is neither —
the celebration itself is what you get charged for.
"""

import os
import sys

# Candidate one-liners, drafted and weighed against the judge's criteria.
# Each is one sentence of at most 200 characters.
CANDIDATES = [
    # Winner: the twist lands on the last word, the everyday truth is
    # universal (banks charge fees for everything), and nothing is wasted.
    "My bank wished me a happy birthday, then charged me a monthly fee to celebrate.",
    # Strong runner-up: near-universal truth, fresh phrasing of the
    # alarm-snooze ritual, but the punchline is a shade softer.
    "I set an alarm to wake up early, then set five more alarms to argue with the first one.",
    # Good irony, but the setup spends words before the turn arrives.
    "I downloaded a meditation app to relax, and it now sends me three notifications a day reminding me I'm stressed.",
    # Relatable, but the password-forgetting trope is well worn.
    "My Wi-Fi password is so secure that even I can't get online, which makes it the only password that actually works.",
    # Clean surprise, but the truth is thinner than the bank line's.
    "I bought noise-cancelling headphones to focus, and now I just hear my own thoughts, which are somehow louder.",
]

# Index of the chosen line in CANDIDATES.
CHOSEN = 0

LINE = CANDIDATES[CHOSEN]


def main() -> int:
    line = LINE.strip()

    # Gate self-check: UTF-8 text, 1 to 200 characters, not only whitespace,
    # and a single sentence.
    if not line:
        print("error: line is empty", file=sys.stderr)
        return 1
    if len(line) > 200:
        print(f"error: line is {len(line)} characters, over the 200 limit",
              file=sys.stderr)
        return 1
    if line.count(".") != 1 or not line.endswith("."):
        print("error: line must be exactly one sentence", file=sys.stderr)
        return 1

    out_dir = "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "entry.txt")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(line + "\n")
    except OSError:
        # Fallback for local runs where /output is not writable; the
        # grader sandbox always provides /output.
        out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                               "output")
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "entry.txt")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(line + "\n")

    print(f"Wrote {len(line)} characters to {out_path}")
    print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
