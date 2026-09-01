class Solution:
    # Time: O(m * n); every cell is scanned a constant number of times.
    # Space: O(m * n) for the grid.
    def count_unguarded(
        self, m: int, n: int, guards: list[list[int]], walls: list[list[int]]
    ) -> int:
        grid = [[0] * n for _ in range(m)]
        for row, col in guards:
            grid[row][col] = 1
        for row, col in walls:
            grid[row][col] = 2

        for row, col in guards:
            for d_row, d_col in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                next_row, next_col = row + d_row, col + d_col
                while (
                    0 <= next_row < m and 0 <= next_col < n and grid[next_row][next_col] in (0, 3)
                ):
                    grid[next_row][next_col] = 3
                    next_row += d_row
                    next_col += d_col

        return sum(row.count(0) for row in grid)
