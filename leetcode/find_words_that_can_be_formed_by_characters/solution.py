from collections import Counter


class Solution:
    # Time: O(sum(len(w) for w in words) + len(chars))
    # Space: O(1)
    def count_characters(self, words: list[str], chars: str) -> int:
        chars_count = Counter(chars)
        return sum(len(word) for word in words if not (Counter(word) - chars_count))
