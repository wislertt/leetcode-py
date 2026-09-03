import heapq


class Solution:
    # Time: O(E log V)
    # Space: O(V + E)
    def reachable_nodes(self, edges: list[list[int]], max_moves: int, n: int) -> int:
        adj: list[list[tuple[int, int]]] = [[] for _ in range(n)]
        for u, v, cnt in edges:
            adj[u].append((v, cnt))
            adj[v].append((u, cnt))

        unreachable = max_moves + 1
        dist = [unreachable] * n
        dist[0] = 0
        heap: list[tuple[int, int]] = [(0, 0)]
        while heap:
            d, node = heapq.heappop(heap)
            if d > dist[node]:
                continue
            for nxt, cnt in adj[node]:
                nd = d + cnt + 1
                if nd < dist[nxt]:
                    dist[nxt] = nd
                    heapq.heappush(heap, (nd, nxt))

        reachable = sum(1 for d in dist if d <= max_moves)
        for u, v, cnt in edges:
            head = max(0, max_moves - dist[u])
            tail = max(0, max_moves - dist[v])
            reachable += min(cnt, head + tail)
        return reachable
