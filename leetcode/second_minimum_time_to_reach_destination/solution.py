from collections import deque


class Solution:
    # Time: O(n + m) BFS plus O(second_path_length) for the signal simulation
    # Space: O(n + m)
    def second_minimum(self, n: int, edges: list[list[int]], time: int, change: int) -> int:
        adj: list[list[int]] = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # two smallest distinct arrival edge-counts per vertex (BFS order)
        dists: list[list[int]] = [[] for _ in range(n + 1)]
        dists[1].append(0)
        queue: deque[tuple[int, int]] = deque([(1, 0)])
        while queue:
            node, steps = queue.popleft()
            for nb in adj[node]:
                nxt = steps + 1
                if len(dists[nb]) < 2 and nxt not in dists[nb]:
                    dists[nb].append(nxt)
                    queue.append((nb, nxt))

        elapsed = 0
        for _ in range(dists[n][1]):
            if (elapsed // change) % 2 == 1:
                elapsed = (elapsed // change + 1) * change
            elapsed += time
        return elapsed
