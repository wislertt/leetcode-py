from functools import reduce
from operator import xor


class Solution:
    # Time: O(n)
    # Space: O(1)
    def single_number(self, nums: list[int]) -> int:
        return reduce(xor, nums)
