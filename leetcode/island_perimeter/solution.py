class Solution:
    # Time: O(row * col) every cell inspected once
    # Space: O(1)
    def island_perimeter(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        perimeter = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    continue
                # Each land cell starts with 4 exposed sides; subtract shared edges.
                exposed = 4
                for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        exposed -= 1
                perimeter += exposed
        return perimeter
