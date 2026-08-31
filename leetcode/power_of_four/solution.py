class Solution:
    # Time: O(1)
    # Space: O(1)
    def is_power_of_four(self, n: int) -> bool:
        # Power of two with the single set bit in an even (0-indexed) position:
        # 4^x mod 3 == 1, while 2 * 4^x mod 3 == 2.
        return n > 0 and n & (n - 1) == 0 and n % 3 == 1
