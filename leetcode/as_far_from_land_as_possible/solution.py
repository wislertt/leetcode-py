from collections import deque


class Solution:
    # Time: O(n^2)
    # Space: O(n^2)
    def max_distance(self, grid: list[list[int]]) -> int:
        size = len(grid)
        queue: deque[tuple[int, int, int]] = deque()
        seen = [[False] * size for _ in range(size)]
        for i in range(size):
            for j in range(size):
                if grid[i][j] == 1:
                    queue.append((i, j, 0))
                    seen[i][j] = True
        if not queue or len(queue) == size * size:
            return -1
        best = -1
        while queue:
            i, j, dist = queue.popleft()
            best = max(best, dist)
            for ni, nj in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                if 0 <= ni < size and 0 <= nj < size and not seen[ni][nj]:
                    seen[ni][nj] = True
                    queue.append((ni, nj, dist + 1))
        return best
