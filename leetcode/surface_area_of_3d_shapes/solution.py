class Solution:
    # Time: O(n^2) every cell inspected once with its four neighbours
    # Space: O(1)
    def surface_area(self, grid: list[list[int]]) -> int:
        size = len(grid)
        area = 0
        for row in range(size):
            for col in range(size):
                height = grid[row][col]
                if height == 0:
                    continue
                # Top and bottom faces are always exposed for a non-empty tower.
                area += 2
                # Four side faces per cube, minus what a neighbour hides.
                area += 4 * height
                for d_row, d_col in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    n_row, n_col = row + d_row, col + d_col
                    if 0 <= n_row < size and 0 <= n_col < size:
                        area -= min(height, grid[n_row][n_col])
        return area
