from collections import Counter


class Solution:
    # Time: O(n)
    # Space: O(1)
    def first_uniq_char(self, s: str) -> int:
        counts = Counter(s)
        for i, ch in enumerate(s):
            if counts[ch] == 1:
                return i
        return -1
