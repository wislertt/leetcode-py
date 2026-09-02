from collections import Counter


class Solution:
    # Time: O(n)
    # Space: O(1)
    def can_construct(self, s: str, k: int) -> bool:
        odd = sum(count % 2 for count in Counter(s).values())
        return odd <= k <= len(s)
