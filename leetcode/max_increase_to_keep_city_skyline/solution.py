class Solution:
    # Time: O(n^2)
    # Space: O(n)
    def max_increase_keeping_skyline(self, grid: list[list[int]]) -> int:
        row_max = [max(row) for row in grid]
        col_max = [max(col) for col in zip(*grid, strict=True)]
        return sum(
            min(row_max[r], col_max[c]) - grid[r][c]
            for r, row in enumerate(grid)
            for c in range(len(row))
        )
