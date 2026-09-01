from collections import deque
from heapq import heappop, heappush


class Solution:
    # Time: O(n^2 log(n^2)) for the multi-source BFS plus the maximin search
    # Space: O(n^2)
    def maximum_safeness_factor(self, grid: list[list[int]]) -> int:
        n = len(grid)
        dist = self._thief_distances(grid, n)
        best = [[-1] * n for _ in range(n)]
        best[0][0] = dist[0][0]
        heap: list[tuple[int, int, int]] = [(-dist[0][0], 0, 0)]
        while heap:
            neg, r, c = heappop(heap)
            safe = -neg
            if safe < best[r][c]:
                continue
            if r == n - 1 and c == n - 1:
                return safe
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n:
                    nxt = min(safe, dist[nr][nc])
                    if nxt > best[nr][nc]:
                        best[nr][nc] = nxt
                        heappush(heap, (-nxt, nr, nc))
        return best[n - 1][n - 1]

    def _thief_distances(self, grid: list[list[int]], n: int) -> list[list[int]]:
        dist = [[-1] * n for _ in range(n)]
        queue = deque((r, c) for r in range(n) for c in range(n) if grid[r][c] == 1)
        for r, c in queue:
            dist[r][c] = 0
        while queue:
            r, c = queue.popleft()
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and dist[nr][nc] < 0:
                    dist[nr][nc] = dist[r][c] + 1
                    queue.append((nr, nc))
        return dist
