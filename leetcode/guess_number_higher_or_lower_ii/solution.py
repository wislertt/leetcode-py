class Solution:
    # Time: O(n^3)
    # Space: O(n^2)
    def get_money_amount(self, n: int) -> int:
        # dp[lo][hi] = min worst-case cost to guarantee a win within [lo, hi].
        dp = [[0] * (n + 2) for _ in range(n + 2)]
        for length in range(2, n + 1):
            for lo in range(1, n - length + 2):
                hi = lo + length - 1
                dp[lo][hi] = min(x + max(dp[lo][x - 1], dp[x + 1][hi]) for x in range(lo, hi))
        return dp[1][n]
