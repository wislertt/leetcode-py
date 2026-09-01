class Solution:
    # Time: O(n log n) for the sort, O(n) for the sliding window
    # Space: O(1) extra beyond the in-place sort
    def max_frequency(self, nums: list[int], k: int) -> int:
        nums.sort()
        left = 0
        total = 0
        best = 0
        for right, val in enumerate(nums):
            total += val
            while (right - left + 1) * val - total > k:
                total -= nums[left]
                left += 1
            best = max(best, right - left + 1)
        return best
