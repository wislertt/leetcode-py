class Solution:
    # Time: O(m * n * max(m, n))
    # Space: O(m * n)
    def has_path(self, maze: list[list[int]], start: list[int], destination: list[int]) -> bool:
        m, n = len(maze), len(maze[0])
        dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
        queue = [tuple(start)]
        seen = {tuple(start)}
        while queue:
            r, c = queue.pop(0)
            if [r, c] == destination:
                return True
            for dr, dc in dirs:
                nr, nc = r, c
                while 0 <= nr + dr < m and 0 <= nc + dc < n and maze[nr + dr][nc + dc] == 0:
                    nr += dr
                    nc += dc
                if (nr, nc) not in seen:
                    seen.add((nr, nc))
                    queue.append((nr, nc))
        return False
