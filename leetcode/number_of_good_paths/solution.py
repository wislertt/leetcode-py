class Solution:
    # Time: O(n log n + e * alpha(n)) for sorting the nodes and unioning edges
    # Space: O(n) for the parent, size, adjacency and active arrays
    def number_of_good_paths(self, vals: list[int], edges: list[list[int]]) -> int:
        n = len(vals)
        parent = list(range(n))
        size = [1] * n
        active = [False] * n

        adj: list[list[int]] = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a: int, b: int) -> None:
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            if size[ra] < size[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            size[ra] += size[rb]

        # Every single node is a good path on its own.
        result = n

        # Grow the forest from low values to high values: paths whose maximum
        # value is v are only complete once every node with value <= v exists.
        order = sorted(range(n), key=lambda i: vals[i])
        i = 0
        while i < n:
            j = i
            while j < n and vals[order[j]] == vals[order[i]]:
                j += 1
            group = order[i:j]

            for node in group:
                active[node] = True
            for node in group:
                for nxt in adj[node]:
                    if active[nxt]:
                        union(node, nxt)

            # Every pair of value-v nodes sharing a component gives one path.
            counts: dict[int, int] = {}
            for node in group:
                root = find(node)
                counts[root] = counts.get(root, 0) + 1
            for c in counts.values():
                result += c * (c - 1) // 2

            i = j
        return result
