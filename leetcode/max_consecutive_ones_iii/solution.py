class Solution:
    # Time: O(n)
    # Space: O(1)
    def longest_ones(self, nums: list[int], k: int) -> int:
        left = 0
        zeros = 0
        best = 0
        for right, num in enumerate(nums):
            if num == 0:
                zeros += 1
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            best = max(best, right - left + 1)
        return best
