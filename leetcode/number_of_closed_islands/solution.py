class Solution:
    # Time: O(rows * cols)
    # Space: O(rows * cols)
    def closed_islands(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def fill(row: int, col: int) -> bool:
            closed = True
            stack = [(row, col)]
            grid[row][col] = 1
            while stack:
                r, c = stack.pop()
                if r in (0, rows - 1) or c in (0, cols - 1):
                    closed = False
                for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                        grid[nr][nc] = 1
                        stack.append((nr, nc))
            return closed

        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0 and fill(r, c):
                    count += 1
        return count
