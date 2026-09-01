from collections import Counter


class Solution:
    # Time: O(n)
    # Space: O(n)
    def largest_unique_number(self, nums: list[int]) -> int:
        counts = Counter(nums)
        candidates = [value for value, count in counts.items() if count == 1]
        return max(candidates) if candidates else -1
