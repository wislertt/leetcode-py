from collections import deque


class Solution:
    # Time: O(m * n)
    # Space: O(m * n)
    def min_cost(self, grid: list[list[int]]) -> int:
        # 0-1 BFS: follow the cell's own sign with cost 0, any other
        # direction with cost 1.
        dirs = {1: (0, 1), 2: (0, -1), 3: (1, 0), 4: (-1, 0)}
        m, n = len(grid), len(grid[0])
        inf_cost = 10**9
        dist = [[inf_cost] * n for _ in range(m)]
        dist[0][0] = 0
        dq: deque[tuple[int, int, int]] = deque([(0, 0, 0)])
        while dq:
            d, i, j = dq.popleft()
            if d > dist[i][j]:
                continue
            for s, (di, dj) in dirs.items():
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n:
                    nd = d if grid[i][j] == s else d + 1
                    if nd < dist[ni][nj]:
                        dist[ni][nj] = nd
                        if nd == d:
                            dq.appendleft((nd, ni, nj))
                        else:
                            dq.append((nd, ni, nj))
        return dist[m - 1][n - 1]
