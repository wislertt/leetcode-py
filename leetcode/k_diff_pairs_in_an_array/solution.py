from collections import Counter


class Solution:
    # Time: O(n)
    # Space: O(n)
    def find_pairs(self, nums: list[int], k: int) -> int:
        counts = Counter(nums)
        if k == 0:
            return sum(1 for count in counts.values() if count > 1)
        return sum(1 for value in counts if value + k in counts)
