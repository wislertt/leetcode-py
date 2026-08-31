class Solution:
    # Time: O(m * n)
    # Space: O(m * n)
    def num_distinct_islands(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        seen = [[False] * n for _ in range(m)]
        shapes: set[tuple[tuple[int, int], ...]] = set()

        def dfs(i: int, j: int, cells: list[tuple[int, int]]) -> None:
            if not (0 <= i < m and 0 <= j < n) or seen[i][j] or grid[i][j] == 0:
                return
            seen[i][j] = True
            cells.append((i, j))
            for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                dfs(i + di, j + dj, cells)

        for i in range(m):
            for j in range(n):
                if grid[i][j] and not seen[i][j]:
                    cells: list[tuple[int, int]] = []
                    dfs(i, j, cells)
                    bi, bj = min(cells)
                    shapes.add(tuple(sorted((x - bi, y - bj) for x, y in cells)))
        return len(shapes)
