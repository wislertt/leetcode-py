class Solution:
    # Time: O(n * alpha(n)) ≈ O(n) where alpha is inverse Ackermann
    # Space: O(n)
    def find_redundant_connection(self, edges: list[list[int]]) -> list[int]:
        parent: list[int] = list(range(len(edges) + 1))
        rank: list[int] = [0] * (len(edges) + 1)

        def find(node: int) -> int:
            # Path compression
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]

        def union(node_a: int, node_b: int) -> bool:
            root_a, root_b = find(node_a), find(node_b)
            if root_a == root_b:
                return False  # Already connected → cycle
            # Union by rank
            if rank[root_a] < rank[root_b]:
                parent[root_a] = root_b
            elif rank[root_a] > rank[root_b]:
                parent[root_b] = root_a
            else:
                parent[root_b] = root_a
                rank[root_a] += 1
            return True

        for node_a, node_b in edges:
            if not union(node_a, node_b):
                return [node_a, node_b]
        return []
