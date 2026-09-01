class Solution:
    # Time: O(n)
    # Space: O(1)
    def max_ascending_sum(self, nums: list[int]) -> int:
        best = cur = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                cur += nums[i]
            else:
                cur = nums[i]
            if cur > best:
                best = cur
        return best
