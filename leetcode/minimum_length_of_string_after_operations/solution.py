from collections import Counter


class Solution:
    # Time: O(n)
    # Space: O(1)
    def minimum_length(self, s: str) -> int:
        return sum(c if c <= 2 else 1 if c % 2 else 2 for c in Counter(s).values())
