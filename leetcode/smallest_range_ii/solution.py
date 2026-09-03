class Solution:
    # Time: O(n log n) for the sort, then a single linear sweep
    # Space: O(1) beyond the sort
    def smallest_range_ii(self, nums: list[int], k: int) -> int:
        nums = sorted(nums)
        result = nums[-1] - nums[0]
        low = nums[0] + k
        high = nums[-1] - k
        for i in range(len(nums) - 1):
            big = max(nums[i] + k, high)
            small = min(nums[i + 1] - k, low)
            result = min(result, big - small)
        return result
