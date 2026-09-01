import heapq


class Solution:
    # Time: O(m*n*log(m*n) + k*log k)
    # Space: O(m*n)
    def max_points(self, grid: list[list[int]], queries: list[int]) -> list[int]:
        rows, cols = len(grid), len(grid[0])
        visited = [[False] * cols for _ in range(rows)]
        visited[0][0] = True
        heap: list[tuple[int, int, int]] = [(grid[0][0], 0, 0)]
        count = 0
        counts: dict[int, int] = {}
        for query in sorted(set(queries)):
            while heap and heap[0][0] < query:
                _, i, j = heapq.heappop(heap)
                count += 1
                for ni, nj in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                    if 0 <= ni < rows and 0 <= nj < cols and not visited[ni][nj]:
                        visited[ni][nj] = True
                        heapq.heappush(heap, (grid[ni][nj], ni, nj))
            counts[query] = count
        return [counts[query] for query in queries]
