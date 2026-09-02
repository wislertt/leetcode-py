class Solution:
    # Time: O(n log n) for sorting, O(n) for the sliding window
    # Space: O(1) extra (sort in place, two pointers)
    def maximum_beauty(self, nums: list[int], k: int) -> int:
        nums.sort()
        left = 0
        best = 0
        for right in range(len(nums)):
            while nums[right] - nums[left] > 2 * k:
                left += 1
            best = max(best, right - left + 1)
        return best
