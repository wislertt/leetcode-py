import heapq


class Solution:
    # Time: O(m*n*log(m*n))
    # Space: O(m*n)
    def trap_rain_water(self, height_map: list[list[int]]) -> int:
        m, n = len(height_map), len(height_map[0])
        if m < 3 or n < 3:
            return 0
        visited = [[False] * n for _ in range(m)]
        heap: list[tuple[int, int, int]] = []
        for i in range(m):
            for j in (0, n - 1):
                heapq.heappush(heap, (height_map[i][j], i, j))
                visited[i][j] = True
        for j in range(n):
            for i in (0, m - 1):
                if not visited[i][j]:
                    heapq.heappush(heap, (height_map[i][j], i, j))
                    visited[i][j] = True
        total = 0
        while heap:
            wall, i, j = heapq.heappop(heap)
            for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and not visited[ni][nj]:
                    visited[ni][nj] = True
                    total += max(0, wall - height_map[ni][nj])
                    heapq.heappush(heap, (max(wall, height_map[ni][nj]), ni, nj))
        return total
