class Solution:
    # Time: O(n)
    # Space: O(1)
    def longest_subarray(self, nums: list[int]) -> int:
        target = max(nums)
        best = 0
        run = 0
        for num in nums:
            run = run + 1 if num == target else 0
            if run > best:
                best = run
        return best
