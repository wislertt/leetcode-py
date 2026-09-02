class Solution:
    # Time: O(n + m * alpha(m))
    # Space: O(n)
    def min_score(self, n: int, roads: list[list[int]]) -> int:
        parent = list(range(n + 1))

        def find(node: int) -> int:
            while parent[node] != node:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node

        for city_a, city_b, _ in roads:
            root_a, root_b = find(city_a), find(city_b)
            if root_a != root_b:
                parent[root_a] = root_b

        root = find(1)
        return min(dist for a, b, dist in roads if find(a) == root and find(b) == root)
