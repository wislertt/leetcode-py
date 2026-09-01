import heapq


class Solution:
    # Time: O((V + E) * log V)
    # Space: O(V + E)
    def max_probability(
        self, n: int, edges: list[list[int]], succ_prob: list[float], start_node: int, end_node: int
    ) -> float:
        adj: list[list[tuple[int, float]]] = [[] for _ in range(n)]
        for (a, b), p in zip(edges, succ_prob, strict=True):
            adj[a].append((b, p))
            adj[b].append((a, p))

        best = [0.0] * n
        best[start_node] = 1.0
        heap: list[tuple[float, int]] = [(-1.0, start_node)]
        while heap:
            neg, node = heapq.heappop(heap)
            cur = -neg
            if cur < best[node]:
                continue
            if node == end_node:
                return cur
            for nxt, p in adj[node]:
                cand = cur * p
                if cand > best[nxt]:
                    best[nxt] = cand
                    heapq.heappush(heap, (-cand, nxt))
        return best[end_node]
