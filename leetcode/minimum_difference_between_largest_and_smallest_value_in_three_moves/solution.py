class Solution:
    # Time: O(n log n)
    # Space: O(n) for the sort
    def min_difference(self, nums: list[int]) -> int:
        if len(nums) <= 4:
            return 0
        nums = sorted(nums)
        return min(nums[-4 + i] - nums[i] for i in range(4))
