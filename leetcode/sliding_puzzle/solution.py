from collections import deque


class Solution:
    # Time: O((n * m)!) states, each expanded once
    # Space: O((n * m)!)
    def sliding_puzzle(self, board: list[list[int]]) -> int:
        target = (1, 2, 3, 4, 5, 0)
        start = tuple(x for row in board for x in row)
        neighbors = ((1, 3), (0, 2, 4), (1, 5), (0, 4), (1, 3, 5), (2, 4))

        queue = deque([(start, start.index(0), 0)])
        seen = {start}
        while queue:
            state, zero, moves = queue.popleft()
            if state == target:
                return moves
            for nz in neighbors[zero]:
                nxt = list(state)
                nxt[zero], nxt[nz] = nxt[nz], nxt[zero]
                ns = tuple(nxt)
                if ns not in seen:
                    seen.add(ns)
                    queue.append((ns, nz, moves + 1))
        return -1
