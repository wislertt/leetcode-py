class Solution:
    # Time: O(n)
    # Space: O(n)
    def minimum_fuel_cost(self, roads: list[list[int]], seats: int) -> int:
        n = len(roads) + 1
        if n == 1:
            return 0

        adj: list[list[int]] = [[] for _ in range(n)]
        for a, b in roads:
            adj[a].append(b)
            adj[b].append(a)

        # Iterative BFS from the capital (n up to 1e5 rules out recursion).
        parent = [-1] * n
        order = [0]
        for u in order:
            for v in adj[u]:
                if v != parent[u]:
                    parent[v] = u
                    order.append(v)

        total = 0
        size = [1] * n
        for u in reversed(order):
            p = parent[u]
            if p != -1:
                size[p] += size[u]
                total += (size[u] + seats - 1) // seats
        return total
