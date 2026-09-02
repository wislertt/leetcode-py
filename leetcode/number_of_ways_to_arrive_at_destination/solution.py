import heapq


class Solution:
    # Time: O((n + m) log n) where m = len(roads)
    # Space: O(n + m)
    def count_paths(self, n: int, roads: list[list[int]]) -> int:
        mod = 1_000_000_007
        adj: list[list[tuple[int, int]]] = [[] for _ in range(n)]
        for u, v, t in roads:
            adj[u].append((v, t))
            adj[v].append((u, t))

        # max path cost is n * max(time) <= 200 * 10^9, far below the sentinel
        inf = 1 << 62
        dist = [inf] * n
        ways = [0] * n
        dist[0] = 0
        ways[0] = 1
        heap: list[tuple[int, int]] = [(0, 0)]
        while heap:
            d, node = heapq.heappop(heap)
            if d > dist[node]:
                continue
            for nxt, t in adj[node]:
                nd = d + t
                if nd < dist[nxt]:
                    dist[nxt] = nd
                    ways[nxt] = ways[node]
                    heapq.heappush(heap, (nd, nxt))
                elif nd == dist[nxt]:
                    ways[nxt] = (ways[nxt] + ways[node]) % mod
        return ways[n - 1]
