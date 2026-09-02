from collections import Counter


class Solution:
    # Time: O(n + k^2) where k = 26 distinct characters
    # Space: O(k)
    def min_deletions(self, s: str) -> int:
        used: set[int] = set()
        deletions = 0
        for freq in sorted(Counter(s).values(), reverse=True):
            while freq > 0 and freq in used:
                freq -= 1
                deletions += 1
            if freq > 0:
                used.add(freq)
        return deletions
