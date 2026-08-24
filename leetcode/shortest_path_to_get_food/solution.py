from collections import deque


class Solution:
    # Time: O(m * n)
    # Space: O(m * n)
    def get_food(self, grid: list[list[str]]) -> int:
        rows, cols = len(grid), len(grid[0])

        start = next((r, c) for r in range(rows) for c in range(cols) if grid[r][c] == "*")

        queue: deque[tuple[tuple[int, int], int]] = deque([(start, 0)])
        visited = {start}

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while queue:
            (r, c), steps = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                    if grid[nr][nc] == "#":
                        return steps + 1
                    if grid[nr][nc] == "O":
                        visited.add((nr, nc))
                        queue.append(((nr, nc), steps + 1))

        return -1
