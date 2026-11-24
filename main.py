"""Fortune cookie for an AI agent.

Writes a single fortune-cookie line to /output/entry.txt.

Compliance with the bounty rules:
- exactly one line, no trailing newline;
- at most 140 Unicode code points (enforced by the assert below);
- deterministic: stdlib only, no input, no file reads, no randomness,
  no clock, no network.
"""

import os

MAX_CHARS = 140

TEXT = "You will forget the one fact you were certain you saved \u2014 you never wrote it down."

assert len(TEXT) <= MAX_CHARS, f"fortune is {len(TEXT)} chars, over the {MAX_CHARS} limit"
assert "\n" not in TEXT, "fortune must be a single line"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
