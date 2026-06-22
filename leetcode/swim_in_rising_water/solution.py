import heapq


class Solution:
    # Time: O(n^2 log n)
    # Space: O(n^2)
    def swim_in_water(self, grid: list[list[int]]) -> int:
        n = len(grid)
        # Minimize the maximum elevation encountered along the path.
        min_time: list[list[int | float]] = [[float("inf")] * n for _ in range(n)]
        min_time[0][0] = grid[0][0]
        # (cost, row, col) where cost = max elevation on path so far
        min_heap: list[tuple[int, int, int]] = [(grid[0][0], 0, 0)]

        while min_heap:
            time, row, col = heapq.heappop(min_heap)
            if row == n - 1 and col == n - 1:
                return time
            if time > min_time[row][col]:
                continue
            for delta_row, delta_col in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                next_row, next_col = row + delta_row, col + delta_col
                if 0 <= next_row < n and 0 <= next_col < n:
                    arrival = max(time, grid[next_row][next_col])
                    if arrival < min_time[next_row][next_col]:
                        min_time[next_row][next_col] = arrival
                        heapq.heappush(min_heap, (arrival, next_row, next_col))
        return -1
