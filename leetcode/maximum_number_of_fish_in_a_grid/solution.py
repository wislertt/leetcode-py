from collections import deque


class Solution:
    # Time: O(m * n)
    # Space: O(m * n)
    def find_max_fish(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        seen = [[False] * cols for _ in range(rows)]
        best = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] > 0 and not seen[r][c]:
                    seen[r][c] = True
                    queue = deque([(r, c)])
                    total = 0
                    while queue:
                        cr, cc = queue.popleft()
                        total += grid[cr][cc]
                        for nr, nc in ((cr + 1, cc), (cr - 1, cc), (cr, cc + 1), (cr, cc - 1)):
                            if (
                                0 <= nr < rows
                                and 0 <= nc < cols
                                and grid[nr][nc] > 0
                                and not seen[nr][nc]
                            ):
                                seen[nr][nc] = True
                                queue.append((nr, nc))
                    best = max(best, total)
        return best
