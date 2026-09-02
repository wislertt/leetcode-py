from collections import Counter


class Solution:
    # Time: O(total characters)
    # Space: O(1) (at most 26 keys)
    def make_equal(self, words: list[str]) -> bool:
        n = len(words)
        counts: Counter[str] = Counter()
        for word in words:
            counts.update(word)
        return all(count % n == 0 for count in counts.values())
