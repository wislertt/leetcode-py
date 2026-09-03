class Solution:
    # Time: O(n * alpha(n))
    # Space: O(n)
    def remove_stones(self, stones: list[list[int]]) -> int:
        parent: dict[tuple[str, int], tuple[str, int]] = {}

        def find(node: tuple[str, int]) -> tuple[str, int]:
            root = node
            while parent[root] != root:
                root = parent[root]
            while parent[node] != root:
                parent[node], node = root, parent[node]
            return root

        def union(a: tuple[str, int], b: tuple[str, int]) -> None:
            root_a, root_b = find(a), find(b)
            if root_a != root_b:
                parent[root_b] = root_a

        for x, y in stones:
            parent.setdefault(("r", x), ("r", x))
            parent.setdefault(("c", y), ("c", y))
            union(("r", x), ("c", y))

        roots = {find(("r", x)) for x, _ in stones}
        return len(stones) - len(roots)
