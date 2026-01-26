class Solution:
    # Time: O(m * n)
    # Space: O(1)
    def min_path_sum(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        # Initialize first row
        for j in range(1, n):
            grid[0][j] += grid[0][j - 1]

        # Initialize first column
        for i in range(1, m):
            grid[i][0] += grid[i - 1][0]

        # Fill the rest of the grid
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])

        return grid[-1][-1]
