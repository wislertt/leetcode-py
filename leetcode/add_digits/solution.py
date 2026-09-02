class Solution:
    # Time: O(1) (at most 3 passes for 32-bit inputs)
    # Space: O(1)
    def add_digits(self, num: int) -> int:
        if num == 0:
            return 0
        return 1 + (num - 1) % 9
