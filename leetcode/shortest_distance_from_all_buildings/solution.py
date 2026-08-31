from collections import deque


class Solution:
    # Time: O(b * m * n) — one BFS per building (b = building count)
    # Space: O(m * n)
    def shortest_distance(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        total = [[0] * n for _ in range(m)]
        reach = [[0] * n for _ in range(m)]
        building_count = sum(row.count(1) for row in grid)

        for i in range(m):
            for j in range(n):
                if grid[i][j] != 1:
                    continue
                distance = [[-1] * n for _ in range(m)]
                distance[i][j] = 0
                queue: deque[tuple[int, int]] = deque([(i, j)])
                while queue:
                    r, c = queue.popleft()
                    for x, y in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                        if 0 <= x < m and 0 <= y < n and grid[x][y] == 0 and distance[x][y] < 0:
                            distance[x][y] = distance[r][c] + 1
                            queue.append((x, y))
                for r in range(m):
                    for c in range(n):
                        if distance[r][c] >= 0:
                            total[r][c] += distance[r][c]
                            reach[r][c] += 1

        best = -1
        for i in range(m):
            for j in range(n):
                if (
                    grid[i][j] == 0
                    and reach[i][j] == building_count
                    and (best < 0 or total[i][j] < best)
                ):
                    best = total[i][j]
        return best
