class Solution:
    # Time: O(3^(m*n)) backtracking over non-obstacle cells
    # Space: O(m*n) for the visited set and recursion stack
    def unique_paths_iii(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        empty = 0
        start = (0, 0)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    empty += 1
                elif grid[r][c] == 1:
                    start = (r, c)

        seen = {start}
        count = 0

        def dfs(r: int, c: int) -> None:
            nonlocal count
            if grid[r][c] == 2:
                if len(seen) == empty + 2:
                    count += 1
                return
            for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                in_bounds = 0 <= nr < rows and 0 <= nc < cols
                if in_bounds and grid[nr][nc] != -1 and (nr, nc) not in seen:
                    seen.add((nr, nc))
                    dfs(nr, nc)
                    seen.discard((nr, nc))

        dfs(*start)
        return count
