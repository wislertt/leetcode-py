class Solution:
    # Time: O(len(group) * n * min_profit)
    # Space: O(n * min_profit)
    def profitable_schemes(
        self, n: int, min_profit: int, group: list[int], profit: list[int]
    ) -> int:
        mod = 1_000_000_007
        dp = [[0] * (min_profit + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        for members, gain in zip(group, profit, strict=True):
            for used in range(n, members - 1, -1):
                for earned in range(min_profit, -1, -1):
                    new_earned = min(min_profit, earned + gain)
                    dp[used][new_earned] = (dp[used][new_earned] + dp[used - members][earned]) % mod
        return sum(dp[used][min_profit] for used in range(n + 1)) % mod
