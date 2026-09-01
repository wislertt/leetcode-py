from collections.abc import Iterator
from itertools import zip_longest


class Solution:
    # Time: O(n + m)
    # Space: O(1)
    def array_strings_are_equal(self, word1: list[str], word2: list[str]) -> bool:
        return all(a == b for a, b in zip_longest(self._chars(word1), self._chars(word2)))

    def _chars(self, words: list[str]) -> Iterator[str]:
        for word in words:
            yield from word
