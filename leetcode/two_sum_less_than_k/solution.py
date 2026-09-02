from bisect import bisect_left


class Solution:
    # Time: O(n log n)
    # Space: O(1)
    def two_sum_less_than_k(self, nums: list[int], k: int) -> int:
        nums.sort()
        ans = -1
        for i, x in enumerate(nums):
            j = bisect_left(nums, k - x, lo=i + 1) - 1
            if i < j:
                ans = max(ans, x + nums[j])
        return ans
