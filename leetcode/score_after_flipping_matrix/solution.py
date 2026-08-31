class Solution:
    # Time: O(m * n)
    # Space: O(1)
    def matrix_score(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        score = 0
        for j in range(n):
            # After the optimal row flip, a row's bit at j is 1 exactly when
            # grid[i][j] == grid[i][0] (the leading bit is always set to 1)
            ones = sum(1 for row in grid if row[j] == row[0])
            score += max(ones, m - ones) * (1 << (n - 1 - j))
        return score
