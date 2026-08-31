from collections import deque


class Solution:
    # Time: O(n^2)
    # Space: O(n^2)
    def shortest_bridge(self, grid: list[list[int]]) -> int:
        n = len(grid)

        def neighbors(row: int, col: int) -> list[tuple[int, int]]:
            result = []
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = row + dr, col + dc
                if 0 <= nr < n and 0 <= nc < n:
                    result.append((nr, nc))
            return result

        # Find and mark the first island (DFS)
        start = next((r, c) for r in range(n) for c in range(n) if grid[r][c] == 1)
        first_island: deque[tuple[int, int]] = deque()
        stack = [start]
        grid[start[0]][start[1]] = -1
        while stack:
            row, col = stack.pop()
            first_island.append((row, col))
            for nr, nc in neighbors(row, col):
                if grid[nr][nc] == 1:
                    grid[nr][nc] = -1
                    stack.append((nr, nc))

        # Multi-source BFS from the first island until the second is reached
        distance = 0
        while first_island:
            for _ in range(len(first_island)):
                row, col = first_island.popleft()
                for nr, nc in neighbors(row, col):
                    if grid[nr][nc] == 1:
                        return distance
                    if grid[nr][nc] == 0:
                        grid[nr][nc] = -1
                        first_island.append((nr, nc))
            distance += 1
        return -1
