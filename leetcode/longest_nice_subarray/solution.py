class Solution:
    # Time: O(n)
    # Space: O(1)
    def longest_nice_subarray(self, nums: list[int]) -> int:
        best = 0
        window_or = 0
        left = 0
        for right, num in enumerate(nums):
            while window_or & num:
                window_or ^= nums[left]
                left += 1
            window_or |= num
            best = max(best, right - left + 1)
        return best
