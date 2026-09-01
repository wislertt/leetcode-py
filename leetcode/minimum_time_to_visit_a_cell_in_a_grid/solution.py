import heapq


class Solution:
    # Time: O(m * n * log(m * n))
    # Space: O(m * n)
    def minimum_time(self, grid: list[list[int]]) -> int:
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1

        rows, cols = len(grid), len(grid[0])
        unvisited = 10**18
        best = [[unvisited] * cols for _ in range(rows)]
        best[0][0] = 0
        heap: list[tuple[int, int, int]] = [(0, 0, 0)]

        while heap:
            time, row, col = heapq.heappop(heap)
            if best[row][col] < time:
                continue
            if row == rows - 1 and col == cols - 1:
                return time

            for d_row, d_col in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                n_row, n_col = row + d_row, col + d_col
                if not (0 <= n_row < rows and 0 <= n_col < cols):
                    continue
                need = grid[n_row][n_col]
                # Waiting means bouncing between two adjacent cells, which costs
                # 2 seconds per bounce, so the arrival parity is preserved.
                n_time = max(time + 1, need + ((need - time - 1) % 2))
                if n_time < best[n_row][n_col]:
                    best[n_row][n_col] = n_time
                    heapq.heappush(heap, (n_time, n_row, n_col))

        return -1
