from collections import deque


class Solution:
    # Time: O(m * n)
    # Space: O(m * n)
    def minimum_obstacles(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dist = [[-1] * cols for _ in range(rows)]
        dist[0][0] = 0
        dq: deque[tuple[int, int, int]] = deque([(0, 0, 0)])
        while dq:
            cost, r, c = dq.popleft()
            if cost > dist[r][c]:
                continue
            if r == rows - 1 and c == cols - 1:
                return cost
            for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if 0 <= nr < rows and 0 <= nc < cols:
                    ncost = cost + grid[nr][nc]
                    if dist[nr][nc] == -1 or ncost < dist[nr][nc]:
                        dist[nr][nc] = ncost
                        if grid[nr][nc]:
                            dq.append((ncost, nr, nc))
                        else:
                            dq.appendleft((ncost, nr, nc))
        return dist[rows - 1][cols - 1]
