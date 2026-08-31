from math import isqrt


class Solution:
    # Time: O(1)
    # Space: O(1)
    def arrange_coins(self, n: int) -> int:
        # largest k with k * (k + 1) / 2 <= n
        return (isqrt(8 * n + 1) - 1) // 2
