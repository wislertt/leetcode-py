class Solution:
    # Time: O(n)
    # Space: O(1)
    def max_absolute_sum(self, nums: list[int]) -> int:
        max_sum = 0
        min_sum = 0
        best = 0
        for num in nums:
            max_sum = max(max_sum + num, num)
            min_sum = min(min_sum + num, num)
            best = max(best, max_sum, -min_sum)
        return best
