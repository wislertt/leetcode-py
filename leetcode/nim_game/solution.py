class Solution:
    # Time: O(1)
    # Space: O(1)
    def can_win_nim(self, n: int) -> bool:
        return n % 4 != 0
