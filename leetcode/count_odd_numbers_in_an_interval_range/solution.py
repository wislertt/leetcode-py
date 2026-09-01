class Solution:
    # Time: O(1)
    # Space: O(1)
    def count_odds(self, low: int, high: int) -> int:
        return (high + 1) // 2 - low // 2
