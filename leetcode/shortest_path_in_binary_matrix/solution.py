from collections import deque


class Solution:
    # Time: O(n^2)
    # Space: O(n^2)
    def shortest_path_binary_matrix(self, grid: list[list[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        n = len(grid)
        if n == 1:
            return 1

        directions = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ]
        queue: deque[tuple[int, int]] = deque([(0, 0)])
        grid[0][0] = 1
        while queue:
            row, col = queue.popleft()
            distance = grid[row][col]
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if nr == n - 1 and nc == n - 1:
                    return distance + 1
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                    grid[nr][nc] = distance + 1
                    queue.append((nr, nc))
        return -1
