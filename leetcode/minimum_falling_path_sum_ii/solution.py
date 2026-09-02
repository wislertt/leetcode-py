class Solution:
    def min_falling_path_sum(self, grid: list[list[int]]) -> int:
        n = len(grid)
        dp = grid[0][:]
        for i in range(1, n):
            first, second = sorted(dp)[:2]
            dp = [grid[i][j] + (second if dp[j] == first else first) for j in range(n)]
        return min(dp)
