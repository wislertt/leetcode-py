class Solution:
    # Time: O(n^3)
    # Space: O(n^2)
    def max_coins(self, nums: list[int]) -> int:
        balloons = [1, *nums, 1]
        n = len(balloons)
        # dp[i][j] = max coins bursting all balloons strictly between i and j
        dp = [[0] * n for _ in range(n)]
        for length in range(2, n):
            for i in range(n - length):
                j = i + length
                for k in range(i + 1, j):
                    coins = balloons[i] * balloons[k] * balloons[j]
                    dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + coins)
        return dp[0][n - 1]
