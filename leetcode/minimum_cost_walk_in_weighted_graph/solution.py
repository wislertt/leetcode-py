FULL_MASK = (1 << 17) - 1


class Solution:
    # Time: O((len(edges) + len(query)) * alpha(n))
    # Space: O(n)
    def minimum_cost(self, n: int, edges: list[list[int]], query: list[list[int]]) -> list[int]:
        # A walk may repeat edges, so within a connected component every edge can be
        # traversed, and extra edges only clear bits. The minimum cost for two nodes
        # in the same component is therefore the AND of all weights in it.
        parent = list(range(n))
        and_by_root = [FULL_MASK] * n

        def find(node: int) -> int:
            while parent[node] != node:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node

        for u, v, weight in edges:
            ru, rv = find(u), find(v)
            if ru == rv:
                and_by_root[ru] &= weight
            else:
                parent[ru] = rv
                and_by_root[rv] &= and_by_root[ru] & weight

        result: list[int] = []
        for start, end in query:
            if start == end:
                result.append(0)
                continue
            root = find(start)
            result.append(and_by_root[root] if root == find(end) else -1)
        return result
