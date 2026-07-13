import heapq


class Solution:
    # Time: O(rows * cols * log(rows * cols))
    # Space: O(rows * cols)
    def minimum_effort_path(self, heights: list[list[int]]) -> int:
        rows = len(heights)
        cols = len(heights[0])

        efforts = [[float("inf")] * cols for _ in range(rows)]
        efforts[0][0] = 0

        heap: list[tuple[int, int, int]] = [(0, 0, 0)]

        while heap:
            effort, row, col = heapq.heappop(heap)

            if row == rows - 1 and col == cols - 1:
                return effort

            if effort > efforts[row][col]:
                continue

            for drow, dcol in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                new_row, new_col = row + drow, col + dcol
                if 0 <= new_row < rows and 0 <= new_col < cols:
                    new_effort = max(effort, abs(heights[row][col] - heights[new_row][new_col]))
                    if new_effort < efforts[new_row][new_col]:
                        efforts[new_row][new_col] = new_effort
                        heapq.heappush(heap, (new_effort, new_row, new_col))

        return 0
