class Solution:
    # Time: O(n)
    # Space: O(n)
    def min_time(self, n: int, edges: list[list[int]], has_apple: list[bool]) -> int:
        adj: list[list[int]] = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        seen = [False] * n
        parent = [-1] * n
        order = [0]
        seen[0] = True
        for u in order:
            for v in adj[u]:
                if not seen[v]:
                    seen[v] = True
                    parent[v] = u
                    order.append(v)

        subtree_has_apple = list(has_apple)
        total = 0
        for u in reversed(order):
            if u == 0:
                continue
            if subtree_has_apple[u]:
                total += 2
                subtree_has_apple[parent[u]] = True
        return total
