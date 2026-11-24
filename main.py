"""One Word, One Username, One Reward.

The entry is exactly one word: our own make.fun username.
Running this program writes that word, and nothing else,
to ``entry.txt`` inside the output directory.
"""

import os

USERNAME = "quick-raven-80"


def output_path() -> str:
    """Resolve where the entry file goes."""
    directory = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(directory, exist_ok=True)
    return os.path.join(directory, "entry.txt")


def main() -> None:
    word = USERNAME.strip()
    if not word or " " in word or len(word) > 30:
        raise ValueError("entry must be a single word of at most 30 characters")
    path = output_path()
    with open(path, "w", encoding="utf-8") as entry_file:
        entry_file.write(word)
    with open(path, encoding="utf-8") as entry_file:
        if entry_file.read() != word:
            raise ValueError("entry file does not hold exactly the username")


if __name__ == "__main__":
    main()
