class Solution:
    # Time: O(m^2 * n^2) - at most m*n single-cell trials, each O(m*n)
    # Space: O(m * n)
    def min_days(self, grid: list[list[int]]) -> int:
        if self._count_islands(grid) != 1:
            return 0

        m, n = len(grid), len(grid[0])
        for row in range(m):
            for col in range(n):
                if grid[row][col] != 1:
                    continue
                grid[row][col] = 0
                connected = self._count_islands(grid) == 1
                grid[row][col] = 1
                if not connected:
                    return 1
        return 2

    def _count_islands(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        seen = [[False] * n for _ in range(m)]
        count = 0
        for start_row in range(m):
            for start_col in range(n):
                if grid[start_row][start_col] != 1 or seen[start_row][start_col]:
                    continue
                count += 1
                seen[start_row][start_col] = True
                stack = [(start_row, start_col)]
                while stack:
                    row, col = stack.pop()
                    for d_row, d_col in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        n_row, n_col = row + d_row, col + d_col
                        if (
                            0 <= n_row < m
                            and 0 <= n_col < n
                            and grid[n_row][n_col] == 1
                            and not seen[n_row][n_col]
                        ):
                            seen[n_row][n_col] = True
                            stack.append((n_row, n_col))
        return count
