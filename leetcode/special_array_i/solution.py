from itertools import pairwise


class Solution:
    # Time: O(n)
    # Space: O(1)
    def is_array_special(self, nums: list[int]) -> bool:
        return all(x % 2 != y % 2 for x, y in pairwise(nums))
