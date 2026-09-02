from collections import Counter


class Solution:
    # Time: O(n)
    # Space: O(n)
    def can_be_equal(self, target: list[int], arr: list[int]) -> bool:
        return Counter(target) == Counter(arr)
