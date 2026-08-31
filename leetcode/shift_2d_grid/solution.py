class Solution:
    def shift_grid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        m, n = len(grid), len(grid[0])
        total = m * n
        k %= total
        flat = [grid[i][j] for i in range(m) for j in range(n)]
        flat = flat[-k:] + flat[:-k] if k else flat
        return [flat[i * n : (i + 1) * n] for i in range(m)]
