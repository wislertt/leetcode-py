class Solution:
    # Time: O(log(max(start, goal)))
    # Space: O(1)
    def min_bit_flips(self, start: int, goal: int) -> int:
        return (start ^ goal).bit_count()
