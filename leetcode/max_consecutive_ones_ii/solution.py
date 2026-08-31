class Solution:
    # Time: O(n)
    # Space: O(1)
    def find_max_ones(self, nums: list[int]) -> int:
        left = zeros = best = 0
        for right, value in enumerate(nums):
            if value == 0:
                zeros += 1
            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            best = max(best, right - left + 1)
        return best
