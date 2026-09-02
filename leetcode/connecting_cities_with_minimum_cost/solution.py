class Solution:
    # Time: O(m log m) where m = len(connections)
    # Space: O(n)
    def minimum_cost(self, n: int, connections: list[list[int]]) -> int:
        parent = list(range(n + 1))
        rank = [0] * (n + 1)

        def find(node: int) -> int:
            root = node
            while parent[root] != root:
                root = parent[root]
            while parent[node] != root:
                parent[node], node = root, parent[node]
            return root

        total = 0
        edges_used = 0
        for x, y, cost in sorted(connections, key=lambda edge: edge[2]):
            rx, ry = find(x), find(y)
            if rx == ry:
                continue
            if rank[rx] < rank[ry]:
                rx, ry = ry, rx
            parent[ry] = rx
            if rank[rx] == rank[ry]:
                rank[rx] += 1
            total += cost
            edges_used += 1
            if edges_used == n - 1:
                return total
        return total if edges_used == n - 1 else -1
