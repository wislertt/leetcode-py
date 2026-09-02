class Solution:
    # Time: O(n)
    # Space: O(1)
    def min_moves(self, nums: list[int]) -> int:
        # Each move raises n - 1 elements by 1, so the minimum never falls behind.
        # Equivalently, every element must climb to the maximum: one move can be
        # seen as lowering a single element by 1, giving sum(nums) - n * min(nums).
        return sum(nums) - min(nums) * len(nums)
