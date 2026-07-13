class Solution:
    # Time: O(m * n)
    # Space: O(n)
    def unique_paths_with_obstacles(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        if grid[0][0] == 1 or grid[m - 1][n - 1] == 1:
            return 0

        dp = [0] * n
        dp[0] = 1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dp[j] = 0
                elif j > 0:
                    dp[j] += dp[j - 1]
        return dp[n - 1]
