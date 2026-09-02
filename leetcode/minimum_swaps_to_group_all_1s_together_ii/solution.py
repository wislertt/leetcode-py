class Solution:
    # Time: O(n)
    # Space: O(1)
    def min_swaps(self, nums: list[int]) -> int:
        total = sum(nums)
        n = len(nums)
        if total <= 1 or total == n:
            return 0
        window = sum(nums[:total])
        best = window
        for i in range(1, n):
            window += nums[(i + total - 1) % n] - nums[i - 1]
            best = max(best, window)
        return total - best
