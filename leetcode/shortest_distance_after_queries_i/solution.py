from collections import deque


class Solution:
    # Time: O(n + q * k) where k is the number of distance decreases, q = len(queries)
    # Space: O(n + q)
    def shortest_distance_after_queries(self, n: int, queries: list[list[int]]) -> list[int]:
        adj: list[list[int]] = [[i + 1] for i in range(n - 1)]
        adj.append([])
        dist = list(range(n))
        result: list[int] = []

        for u, v in queries:
            adj[u].append(v)
            if dist[u] + 1 >= dist[v]:
                result.append(dist[n - 1])
                continue

            dist[v] = dist[u] + 1
            queue: deque[int] = deque([v])
            while queue:
                cur = queue.popleft()
                for nxt in adj[cur]:
                    if dist[cur] + 1 < dist[nxt]:
                        dist[nxt] = dist[cur] + 1
                        queue.append(nxt)
            result.append(dist[n - 1])

        return result
