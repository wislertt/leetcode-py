class Solution:
    # Time: O(n^2)
    # Space: O(n^2)
    def number_of_arithmetic_slices(self, nums: list[int]) -> int:
        n = len(nums)
        total = 0
        dp: list[dict[int, int]] = [{} for _ in range(n)]
        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                count_j = dp[j].get(diff, 0)
                total += count_j
                dp[i][diff] = dp[i].get(diff, 0) + count_j + 1
        return total
