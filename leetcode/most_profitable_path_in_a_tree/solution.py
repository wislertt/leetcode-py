class Solution:
    # Time: O(n)
    # Space: O(n)
    def most_profitable_path(self, edges: list[list[int]], bob: int, amount: list[int]) -> int:
        n = len(amount)
        adj: list[list[int]] = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        depth = [0] * n
        parent = [-1] * n
        order = [0]
        for u in order:
            for v in adj[u]:
                if v != parent[u]:
                    parent[v] = u
                    depth[v] = depth[u] + 1
                    order.append(v)

        bob_time: dict[int, int] = {}
        node, t = bob, 0
        while True:
            bob_time[node] = t
            if node == 0:
                break
            node = parent[node]
            t += 1

        gain = [0] * n
        for u in reversed(order):
            child_best = max((gain[v] for v in adj[u] if v != parent[u]), default=0)
            gate = amount[u]
            bt = bob_time.get(u, -1)
            if bt == -1 or bt > depth[u]:
                pass
            elif bt == depth[u]:
                gate = amount[u] // 2
            else:
                gate = 0
            gain[u] = gate + child_best
        return gain[0]
