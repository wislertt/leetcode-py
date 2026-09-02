from collections import deque


class Solution:
    # Time: O(n + m)
    # Space: O(n + m)
    def minimum_diameter_after_merge(self, edges1: list[list[int]], edges2: list[list[int]]) -> int:
        d1 = self._diameter(len(edges1) + 1, edges1)
        d2 = self._diameter(len(edges2) + 1, edges2)
        return max(d1, d2, (d1 + 1) // 2 + (d2 + 1) // 2 + 1)

    def _diameter(self, n: int, edges: list[list[int]]) -> int:
        adj: list[list[int]] = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        def farthest(src: int) -> tuple[int, int]:
            dist = [-1] * n
            dist[src] = 0
            queue = deque([src])
            last = src
            while queue:
                node = queue.popleft()
                last = node
                for nxt in adj[node]:
                    if dist[nxt] == -1:
                        dist[nxt] = dist[node] + 1
                        queue.append(nxt)
            return last, dist[last]

        endpoint, _ = farthest(0)
        _, diameter = farthest(endpoint)
        return diameter
