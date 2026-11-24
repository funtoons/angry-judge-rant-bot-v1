"""Angry Judge: The Short Rant Contest -- entry program.

Writes one short, funny rant about an everyday annoyance to
/output/entry.txt. Python stdlib only, deterministic, offline:
no randomness, no network, no clock, no environment reads.
The rant text is a fixed constant; every run writes identical bytes.
"""

import sys
from pathlib import Path

RANT = (
    "I did not steal the milk. I scanned the milk, I bagged the milk, "
    "I paid for the milk \u2014 and still the self-checkout screams "
    "UNEXPECTED ITEM IN THE BAGGING AREA like I smuggled it in under "
    "my coat. I am now doing unpaid work for a supermarket that "
    "suspects me of shoplifting my own groceries, while a teenager "
    "stands three metres away watching me fail, doing absolutely "
    "nothing \u2014 expertly."
)


def main(argv):
    output = Path(argv[1]) if len(argv) > 1 else Path("/output/entry.txt")
    if not 1 <= len(RANT) <= 400:
        raise SystemExit("rant must be 1-400 characters, got %d" % len(RANT))
    if not RANT.strip():
        raise SystemExit("rant must not be only whitespace")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(RANT, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
