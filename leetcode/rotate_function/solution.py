class Solution:
    # Time: O(n)
    # Space: O(1)
    def max_rotate_function(self, nums: list[int]) -> int:
        total = sum(nums)
        cur = sum(i * v for i, v in enumerate(nums))
        best = cur
        for k in range(1, len(nums)):
            # rotating clockwise by k moves the last element of arr_(k-1) to index 0
            # and adds total to every other index: F(k) = F(k-1) + total - n * nums[n - k]
            cur += total - len(nums) * nums[-k]
            best = max(best, cur)
        return best
