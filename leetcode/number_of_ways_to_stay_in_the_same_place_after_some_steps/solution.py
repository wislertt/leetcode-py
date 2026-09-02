class Solution:
    def num_ways(self, steps: int, arr_len: int) -> int:
        mod = 1_000_000_007
        limit = min(steps // 2 + 1, arr_len)
        dp = [0] * limit
        dp[0] = 1
        for _ in range(steps):
            ndp = [0] * limit
            for i in range(limit):
                ndp[i] = dp[i]
                if i > 0:
                    ndp[i] += dp[i - 1]
                if i + 1 < limit:
                    ndp[i] += dp[i + 1]
                ndp[i] %= mod
            dp = ndp
        return dp[0]
