import pathlib
import sys

from string import ascii_letters

in_path = pathlib.Path(sys.argv[1])
out_path = pathlib.Path(sys.argv[2])

words = sorted(
    word.lower() for word in in_path.read_text().split()
    if len(word) == 5 and all(letter in ascii_letters for letter in word)
)

out_path.write_text("\n".join(words))
