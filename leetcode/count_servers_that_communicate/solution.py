class Solution:
    def count_servers(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        rows = [sum(row) for row in grid]
        cols = [sum(grid[i][j] for i in range(m)) for j in range(n)]
        return sum(
            grid[i][j] == 1 and (rows[i] > 1 or cols[j] > 1) for i in range(m) for j in range(n)
        )
