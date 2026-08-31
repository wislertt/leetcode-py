class Solution:
    # Time: O(n)
    # Space: O(1)
    def is_monotonic(self, nums: list[int]) -> bool:
        increasing = decreasing = True
        for i in range(1, len(nums)):
            increasing &= nums[i - 1] <= nums[i]
            decreasing &= nums[i - 1] >= nums[i]
        return increasing or decreasing
