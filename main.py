"""Houseplant one-star review entry: writes one line to OUTPUT_DIR/entry.txt (stdlib only, deterministic)."""
import os

ENTRY = ("1 star. Watered me twice in one day, then not for three weeks, then apologised to me out loud "
         "while googling 'is it dead'. I could hear you. I was not dead. Give me another week.")
OUTPUT_DIR = os.environ.get("OUTPUT_DIR", "/output")


def main():
    # Gate: UTF-8 text inside the bounty's character limit, not only white space.
    assert ENTRY.strip() and 1 <= len(ENTRY) < 280
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
