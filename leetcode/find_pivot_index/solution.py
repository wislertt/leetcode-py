class Solution:
    # Time: O(n)
    # Space: O(1)
    def pivot_index(self, nums: list[int]) -> int:
        total = sum(nums)
        left_sum = 0
        for i, val in enumerate(nums):
            if left_sum == total - left_sum - val:
                return i
            left_sum += val
        return -1
