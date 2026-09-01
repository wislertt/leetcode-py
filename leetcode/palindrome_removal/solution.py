class Solution:
    # Time: O(n^3)
    # Space: O(n^2)
    def minimum_moves(self, arr: list[int]) -> int:
        n = len(arr)
        # dp[i][j] = minimum moves to clear arr[i..j]
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                if i + 1 == j:
                    dp[i][j] = 1 if arr[i] == arr[j] else 2
                    continue
                best = n
                if arr[i] == arr[j]:
                    best = dp[i + 1][j - 1]
                for k in range(i, j):
                    best = min(best, dp[i][k] + dp[k + 1][j])
                dp[i][j] = best
        return dp[0][n - 1]
