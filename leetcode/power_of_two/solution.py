class Solution:
    # Time: O(1)
    # Space: O(1)
    def is_power_of_two(self, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0
