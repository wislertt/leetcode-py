class Solution:
    # Time: O(m^3) where m = len(cuts)
    # Space: O(m^2)
    def min_cost(self, n: int, cuts: list[int]) -> int:
        bounds = sorted(cuts)
        prefix = [0, *bounds, n]
        m = len(prefix)
        # dp[i][j] = min cost to cut the segment (prefix[i], prefix[j]) entirely
        dp = [[0] * m for _ in range(m)]
        for length in range(2, m):
            for i in range(m - length):
                j = i + length
                dp[i][j] = min(dp[i][k] + dp[k][j] for k in range(i + 1, j)) + prefix[j] - prefix[i]
        return dp[0][m - 1]
