class DSU:
    def __init__(self, size: int) -> None:
        self.parent = list(range(size))

    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a: int, b: int) -> bool:
        root_a, root_b = self.find(a), self.find(b)
        if root_a == root_b:
            return False
        self.parent[root_a] = root_b
        return True


class Solution:
    # Time: O(e * alpha(n))
    # Space: O(n)
    def max_num_edges_to_remove(self, n: int, edges: list[list[int]]) -> int:
        alice = DSU(n + 1)
        bob = DSU(n + 1)
        kept = 0

        for edge_type, u, v in edges:
            if edge_type == 3:
                merged_alice = alice.union(u, v)
                merged_bob = bob.union(u, v)
                if merged_alice or merged_bob:
                    kept += 1

        for edge_type, u, v in edges:
            merged = (edge_type == 1 and alice.union(u, v)) or (edge_type == 2 and bob.union(u, v))
            if merged:
                kept += 1

        if len({alice.find(node) for node in range(1, n + 1)}) > 1:
            return -1
        if len({bob.find(node) for node in range(1, n + 1)}) > 1:
            return -1
        return len(edges) - kept
