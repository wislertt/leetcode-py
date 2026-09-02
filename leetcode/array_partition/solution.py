class Solution:
    # Time: O(n log n)
    # Space: O(n) for the sort
    def array_pair_sum(self, nums: list[int]) -> int:
        nums.sort()
        return sum(nums[::2])
