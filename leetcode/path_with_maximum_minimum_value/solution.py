import heapq


class Solution:
    # Time: O(m * n * log(m * n))
    # Space: O(m * n)
    def maximum_minimum_path(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        heap = [(-grid[0][0], 0, 0)]
        seen = [[False] * n for _ in range(m)]
        while heap:
            neg_v, i, j = heapq.heappop(heap)
            if seen[i][j]:
                continue
            seen[i][j] = True
            if (i, j) == (m - 1, n - 1):
                return -neg_v
            for a, b in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                x, y = i + a, j + b
                if 0 <= x < m and 0 <= y < n and not seen[x][y]:
                    heapq.heappush(heap, (-min(-neg_v, grid[x][y]), x, y))
        raise AssertionError
