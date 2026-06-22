class Solution:
    # Time: O(m * n)
    # Space: O(m * n)
    def max_area_of_island(self, grid: list[list[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        rows, cols = len(grid), len(grid[0])

        def dfs(row: int, col: int) -> int:
            if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == 0:
                return 0
            grid[row][col] = 0  # Mark visited by sinking
            area = 1
            area += dfs(row + 1, col)
            area += dfs(row - 1, col)
            area += dfs(row, col + 1)
            area += dfs(row, col - 1)
            return area

        max_area = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    max_area = max(max_area, dfs(row, col))
        return max_area
