from math import isqrt


class Solution:
    # Time: O(1)
    # Space: O(1)
    def bulb_switch(self, n: int) -> int:
        return isqrt(n)
