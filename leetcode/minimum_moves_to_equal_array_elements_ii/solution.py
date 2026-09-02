class Solution:
    # Time: O(n log n)
    # Space: O(n)
    def min_moves2(self, nums: list[int]) -> int:
        nums = sorted(nums)
        median = nums[len(nums) // 2]
        return sum(abs(num - median) for num in nums)
