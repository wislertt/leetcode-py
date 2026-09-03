from typing import ClassVar


class Solution:
    morse: ClassVar[list[str]] = [
        ".-",
        "-...",
        "-.-.",
        "-..",
        ".",
        "..-.",
        "--.",
        "....",
        "..",
        ".---",
        "-.-",
        ".-..",
        "--",
        "-.",
        "---",
        ".--.",
        "--.-",
        ".-.",
        "...",
        "-",
        "..-",
        "...-",
        ".--",
        "-..-",
        "-.--",
        "--..",
    ]

    # Time: O(S) where S is the total number of characters in all words
    # Space: O(S) for the set of transformations
    def unique_morse_representations(self, words: list[str]) -> int:
        def transform(word: str) -> str:
            return "".join(self.morse[ord(c) - ord("a")] for c in word)

        return len({transform(w) for w in words})
