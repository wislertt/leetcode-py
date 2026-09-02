class Solution:
    # Time: O(n log n)
    # Space: O(n)
    def min_operations(self, nums: list[int]) -> int:
        n = len(nums)
        vals = sorted(set(nums))
        best = 0
        left = 0
        for right in range(len(vals)):
            while vals[right] - vals[left] > n - 1:
                left += 1
            best = max(best, right - left + 1)
        return n - best
