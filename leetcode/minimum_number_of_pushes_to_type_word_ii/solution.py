from collections import Counter


class Solution:
    # Time: O(n)
    # Space: O(1)
    def minimum_pushes(self, word: str) -> int:
        counts = sorted(Counter(word).values(), reverse=True)
        return sum(count * (index // 8 + 1) for index, count in enumerate(counts))
