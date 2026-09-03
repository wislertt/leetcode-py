from collections import deque


class Solution:
    # Time: O(m * n * 2^k)
    # Space: O(m * n * 2^k)
    def shortest_path_all_keys(self, grid: list[str]) -> int:
        m, n = len(grid), len(grid[0])
        keys = 0
        start_r = start_c = 0
        for r in range(m):
            for c in range(n):
                ch = grid[r][c]
                if ch == "@":
                    start_r, start_c = r, c
                elif ch.islower():
                    keys |= 1 << (ord(ch) - ord("a"))

        queue: deque[tuple[int, int, int]] = deque([(start_r, start_c, 0)])
        seen = {(start_r, start_c, 0)}
        moves = 0
        while queue:
            for _ in range(len(queue)):
                r, c, held = queue.popleft()
                if held == keys:
                    return moves
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = r + dr, c + dc
                    if not (0 <= nr < m and 0 <= nc < n):
                        continue
                    ch = grid[nr][nc]
                    if ch == "#":
                        continue
                    if ch.isupper() and not held & (1 << (ord(ch.lower()) - ord("a"))):
                        continue
                    nxt = held | (1 << (ord(ch) - ord("a"))) if ch.islower() else held
                    state = (nr, nc, nxt)
                    if state not in seen:
                        seen.add(state)
                        queue.append(state)
            moves += 1
        return -1
