class Solution:
    # Bottom-up DP: dp[t] = number of ways to reach sum t
    # dp[t] = sum(dp[t - num] for num in nums if t >= num), dp[0] = 1
    # Order matters, so iterate target outer, nums inner
    # Time: O(target * n)
    # Space: O(target)
    def combination_sum4(self, nums: list[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        for t in range(1, target + 1):
            for num in nums:
                if t >= num:
                    dp[t] += dp[t - num]
        return dp[target]
