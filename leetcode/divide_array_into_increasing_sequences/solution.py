from itertools import groupby


class Solution:
    # Time: O(n)
    # Space: O(1)
    def can_divide_into_subsequences(self, nums: list[int], k: int) -> bool:
        max_freq = max(len(list(group)) for _, group in groupby(nums))
        return max_freq * k <= len(nums)
