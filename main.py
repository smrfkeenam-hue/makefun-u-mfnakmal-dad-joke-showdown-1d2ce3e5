"""Dad Joke Showdown entry: one dad joke, at most 200 characters.

The joke is a fresh pun on "taking a break": the computer takes the
request literally and answers with KitKat ads. Clean turn, tight,
and speakable out loud across a dinner table — the punchline lands
at the very end, as a dad joke should.
"""

import os

JOKE = "I told my computer I needed a break, so now it won't stop showing me KitKat ads."

OUTPUT_FILENAME = "entry.txt"


def main():
    # Gate self-check: the entry must be 1-200 characters of non-whitespace
    # UTF-8 text, a single dad joke.
    assert 1 <= len(JOKE) <= 200, f"joke is {len(JOKE)} chars, gate is 1-200"
    assert JOKE.strip(), "joke must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, OUTPUT_FILENAME)
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)
    print(f"wrote {path} ({len(JOKE)} chars)")


if __name__ == "__main__":
    main()
