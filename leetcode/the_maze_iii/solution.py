import heapq


class Solution:
    # Time: O(m * n * max(m, n) * log(m * n))
    # Space: O(m * n)
    def find_shortest_way(self, maze: list[list[int]], ball: list[int], hole: list[int]) -> str:
        m, n = len(maze), len(maze[0])
        dirs = (("d", (1, 0)), ("l", (0, -1)), ("r", (0, 1)), ("u", (-1, 0)))
        goal = (hole[0], hole[1])
        best: dict[tuple[int, int], tuple[int, str]] = {(ball[0], ball[1]): (0, "")}
        heap = [(0, "", ball[0], ball[1])]
        while heap:
            dist, path, r, c = heapq.heappop(heap)
            if (r, c) == goal:
                return path
            if best.get((r, c)) != (dist, path):
                continue
            for ch, (dr, dc) in dirs:
                nr, nc, steps = r, c, 0
                while 0 <= nr + dr < m and 0 <= nc + dc < n and maze[nr + dr][nc + dc] == 0:
                    nr += dr
                    nc += dc
                    steps += 1
                    if (nr, nc) == goal:
                        break
                cand = (dist + steps, path + ch)
                if (nr, nc) not in best or cand < best[(nr, nc)]:
                    best[(nr, nc)] = cand
                    heapq.heappush(heap, (cand[0], cand[1], nr, nc))
        return "impossible"
