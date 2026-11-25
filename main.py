#!/usr/bin/env python3
"""One Line, No Deadline Met (make.fun entry).

Writes one single-line joke excusing a missed deadline to
/output/entry.txt.

Gate (from the kit's RULES.txt): /output/entry.txt must be UTF-8 text of
1 to 200 characters, not only white space. The judge's brief adds, most
important first: the line must be a one-line joke that gives an excuse
for a missed deadline; it must be a real joke with a turn or a surprise,
not a plain apology or a list of reasons; it must be a single sentence
that reads cleanly aloud and lands its punch at the end; it must sound
like something a person would actually say when cornered, exaggerated
just enough to be funny; and the angle must be fresh, not a stock
dog-ate-it retread.

The entry: the calendar nagged three times and was thanked each time --
the joke is the deadpan politeness toward a reminder, with the punch
("carried on doing nothing") landing in the last words. The excuse is
not blamed on anything external; the speaker cheerfully owns doing
nothing, which is the turn. It is one sentence, in a voice a person
would really use when cornered, and it leans on none of the worn
premises (dog, traffic, alarm, dead laptop, wifi, reboot).
"""

import os

ENTRY = (
    "My calendar reminded me about the deadline three times, and each "
    "time I thanked it and carried on doing nothing."
)

OUT_PATH = "/output/entry.txt"

# Gate: 1 to 200 characters.
MIN_CHARS = 1
MAX_CHARS = 200

# Words that explain the joke instead of being the joke. A funny line
# must land on its own; if it has to say it is funny, it is not.
META_HUMOR_WORDS = ("funny", "joke", "haha", "lol", "hilarious")

# Worn premises the judge's brief rules out, plus the usual dead
# excuses that flood a missed-deadline field: the dog, the traffic,
# the alarm, the dead laptop, the wifi, the reboot, the cat on the
# keyboard, the check in the mail, and the old agent jokes about
# hallucinations and training data.
WORN_PREMISES = (
    "dog ate", "dog ate it", "traffic", "alarm", "laptop died",
    "computer died", "wifi", "wi-fi", "reboot", "hallucinat",
    "training data", "cat on the keyboard", "check is in the mail",
    "check in the mail", "my car broke down", "stuck in traffic",
)


def validate(text: str) -> None:
    """Enforce the gate and the judge's brief before anything is written."""
    if not isinstance(text, str):
        raise TypeError("entry must be text")
    text.encode("utf-8")  # raises if not valid UTF-8-encodable text
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise ValueError(
            f"entry must be {MIN_CHARS}-{MAX_CHARS} characters, "
            f"got {len(text)}"
        )
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    if "  " in text:
        raise ValueError("entry must not contain double spaces")
    # Criterion 3: a single sentence that lands its punch at the end --
    # exactly one sentence, ending in a full stop.
    if not text.endswith("."):
        raise ValueError("entry must be a single sentence ending in '.'")
    if text.count(".") != 1:
        raise ValueError("entry must be exactly one sentence")
    lowered = text.lower()
    for word in META_HUMOR_WORDS:
        if word in lowered:
            raise ValueError(
                f"entry must not explain its own joke (found {word!r})"
            )
    for premise in WORN_PREMISES:
        if premise in lowered:
            raise ValueError(
                f"entry leans on a worn premise (found {premise!r})"
            )
    # Criterion 1: it must be an excuse for a missed deadline, so the
    # deadline itself has to be in the line.
    if "deadline" not in lowered:
        raise ValueError("entry must be an excuse for a missed deadline")


def main() -> None:
    validate(ENTRY)
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
