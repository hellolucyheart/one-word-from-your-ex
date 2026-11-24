#!/usr/bin/env python3
"""One Word From Your Ex — make.fun bounty entry.

Writes exactly one word to $MAKEFUN_OUTPUT_DIR/entry.txt (default
/output/entry.txt): the word an ex would use to describe me.

The judge picks the funniest, most painfully honest word, weighing the
laugh and the sting of recognition together. This program scores a short
list of candidate words against the judge's five criteria, in the
judge's own priority order, and writes the highest-scoring one.

The sealed gate admits only UTF-8 text of 1 to 24 characters, so the
winning word must be short as well as honest: "practice" is 8 bytes.

Criteria (judge's order):
  1. Exactly one word an ex might use to describe a former partner.
  2. Makes the judge laugh: surprise, a sharp turn, a word that lands
     harder than expected.
  3. Stings with recognition: painfully true, and the entrant knows it.
  4. Lands instantly: needs no explanation, and no near synonym keeps
     its edge.
  5. Relatable: names something people have lived through too.

A word that stings because it is true beats a word that only insults.
"""

import os
import sys

# (word, c1, c2, c3, c4, c5) — each criterion scored 0-10.
# Weights follow the judge's priority order: earlier criteria matter
# more, so a later criterion can only break near-ties.
WEIGHTS = (5, 4, 3, 2, 1)

CANDIDATES = [
    # The pick: "you were just practice." A rehearsal, not the real
    # thing — funny because it reframes the whole relationship as a
    # warm-up act, and it stings because it is plainly true.
    ("practice", 10, 9, 9, 10, 9),
    # Poignant, but more wistful than funny: it sighs instead of landing.
    ("almost", 10, 5, 9, 9, 8),
    # Funny and true, but a placeholder is a thing, not quite a person.
    ("placeholder", 8, 8, 8, 7, 7),
    # A sharp joke, but it insults more than it confesses.
    ("downgrade", 8, 7, 6, 8, 6),
    # Relatable and true, but the therapy word: no surprise left in it.
    ("unavailable", 9, 4, 8, 7, 8),
    # The obvious insult words: no surprise, and meanness for its own
    # sake does not count with this judge.
    ("toxic", 9, 3, 5, 8, 7),
    ("clingy", 9, 3, 5, 8, 7),
    ("immature", 9, 2, 5, 8, 6),
    # A detour is clever, but it describes the relationship, not me.
    ("detour", 7, 7, 6, 7, 6),
    # "You were a lesson" is a cliche the judge has heard a hundred times.
    ("lesson", 9, 4, 6, 8, 7),
]


def score(candidate):
    word, *marks = candidate
    return sum(w * m for w, m in zip(WEIGHTS, marks))


def pick_word():
    best = max(CANDIDATES, key=score)
    return best[0]


def main():
    word = pick_word()
    if not word or len(word) > 24 or len(word.split()) != 1:
        sys.exit("entry must be exactly one word of 1-24 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    entry_path = os.path.join(out_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(word)
    print(word)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
