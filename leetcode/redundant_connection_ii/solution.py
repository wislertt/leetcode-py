class Solution:
    # Time: O(n * alpha(n))
    # Space: O(n)
    def find_redundant_directed_connection(self, edges: list[list[int]]) -> list[int]:
        n = len(edges)
        parent = list(range(n + 1))
        dsu = list(range(n + 1))
        candidate_first: list[int] | None = None
        candidate_last: list[int] | None = None
        cycle_edge: list[int] | None = None

        def find(node: int) -> int:
            while dsu[node] != node:
                dsu[node] = dsu[dsu[node]]
                node = dsu[node]
            return node

        for u, v in edges:
            if parent[v] != v:
                candidate_first = [parent[v], v]
                candidate_last = [u, v]
                continue
            parent[v] = u
            root_u, root_v = find(u), find(v)
            if root_u == root_v:
                cycle_edge = [u, v]
            else:
                dsu[root_u] = root_v

        if candidate_first is None:
            assert cycle_edge is not None
            return cycle_edge
        if cycle_edge is not None:
            return candidate_first
        assert candidate_last is not None
        return candidate_last
