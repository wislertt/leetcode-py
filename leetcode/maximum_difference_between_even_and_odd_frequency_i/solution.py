from collections import Counter


class Solution:
    # Time: O(n)
    # Space: O(1)
    def max_difference(self, s: str) -> int:
        freqs = Counter(s).values()
        return max(f for f in freqs if f % 2 == 1) - min(f for f in freqs if f % 2 == 0)
