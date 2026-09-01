from collections import Counter


class Solution:
    # Time: O(n log n)
    # Space: O(n)
    def frequency_sort(self, nums: list[int]) -> list[int]:
        counts = Counter(nums)
        return sorted(nums, key=lambda num: (counts[num], -num))
