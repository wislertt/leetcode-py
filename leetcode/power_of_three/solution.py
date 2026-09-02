class Solution:
    # Time: O(1)
    # Space: O(1)
    def is_power_of_three(self, n: int) -> bool:
        # 3^19 = 1162261467 is the largest power of three fitting in a signed
        # 32-bit int; it is divisible by every smaller power of three and by
        # no other positive integer in range. Constant time, no loops.
        return n > 0 and 1162261467 % n == 0
