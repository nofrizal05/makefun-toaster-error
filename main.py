"""The Funniest Toaster Error Message — make.fun entry.

Writes one line of plain text to /output/entry.txt: the error message a
kitchen toaster shows its owner when something goes wrong.
Python standard library only.
"""

import os

ENTRY = "ERROR E07: BREAD JAMMED. YOUR BREAKFAST IS NOW A HOSTAGE."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
