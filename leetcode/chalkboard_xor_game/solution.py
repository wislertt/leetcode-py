from functools import reduce
from operator import xor


class Solution:
    # Time: O(n)
    # Space: O(1)
    def xor_game(self, nums: list[int]) -> bool:
        # Alice loses only when the count is odd and the total XOR is nonzero:
        # with an even count she can always mirror Bob's erasures (two copies of
        # every value would XOR to 0), and a zero XOR wins on the spot.
        return len(nums) % 2 == 0 or reduce(xor, nums, 0) == 0
