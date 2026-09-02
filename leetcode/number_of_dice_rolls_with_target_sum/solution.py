class Solution:
    # Time: O(n * k * target)
    # Space: O(target)
    def num_rolls_to_target(self, n: int, k: int, target: int) -> int:
        mod = 10**9 + 7
        dp = [1] + [0] * target
        for _ in range(n):
            ndp = [0] * (target + 1)
            for t in range(1, target + 1):
                for f in range(1, min(k, t) + 1):
                    ndp[t] = (ndp[t] + dp[t - f]) % mod
            dp = ndp
        return dp[target]
