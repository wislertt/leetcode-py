class Solution:
    # Time: O(m * n)
    # Space: O(m * n)
    def num_enclaves(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def drain(r: int, c: int) -> None:
            stack = [(r, c)]
            grid[r][c] = 0
            while stack:
                r, c = stack.pop()
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                        grid[nr][nc] = 0
                        stack.append((nr, nc))

        for r in range(m):
            for c in (0, n - 1):
                if grid[r][c] == 1:
                    drain(r, c)
        for c in range(n):
            for r in (0, m - 1):
                if grid[r][c] == 1:
                    drain(r, c)
        return sum(row.count(1) for row in grid)
