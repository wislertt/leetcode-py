class Solution:
    # Time: O(n + e * alpha(n))
    # Space: O(n)
    def count_complete_components(self, n: int, edges: list[list[int]]) -> int:
        parent = list(range(n))
        size = [1] * n
        edge_count = [0] * n

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        for a, b in edges:
            ra, rb = find(a), find(b)
            if ra != rb:
                if size[ra] < size[rb]:
                    ra, rb = rb, ra
                parent[rb] = ra
                size[ra] += size[rb]
                edge_count[ra] += edge_count[rb] + 1
            else:
                edge_count[ra] += 1

        complete = 0
        for v in range(n):
            if find(v) == v and edge_count[v] == size[v] * (size[v] - 1) // 2:
                complete += 1
        return complete
