import heapq


class Solution:
    # Time: O(m * n * max(m, n) * log(m * n))
    # Space: O(m * n)
    def shortest_distance(
        self, maze: list[list[int]], start: list[int], destination: list[int]
    ) -> int:
        m, n = len(maze), len(maze[0])
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
        goal = (destination[0], destination[1])
        dist = {(start[0], start[1]): 0}
        heap = [(0, start[0], start[1])]
        while heap:
            d, r, c = heapq.heappop(heap)
            if (r, c) == goal:
                return d
            if d > dist.get((r, c), 10**9):
                continue
            for dr, dc in dirs:
                nr, nc, steps = r, c, 0
                while 0 <= nr + dr < m and 0 <= nc + dc < n and maze[nr + dr][nc + dc] == 0:
                    nr += dr
                    nc += dc
                    steps += 1
                if d + steps < dist.get((nr, nc), 10**9):
                    dist[(nr, nc)] = d + steps
                    heapq.heappush(heap, (d + steps, nr, nc))
        return -1
