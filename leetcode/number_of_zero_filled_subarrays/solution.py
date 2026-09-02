class Solution:
    # Time: O(n)
    # Space: O(1)
    def zero_filled_subarray(self, nums: list[int]) -> int:
        total = 0
        streak = 0
        for num in nums:
            streak = streak + 1 if num == 0 else 0
            total += streak
        return total
