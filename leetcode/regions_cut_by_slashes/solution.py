class Solution:
    # Time: O(n^2 * alpha(n^2))
    # Space: O(n^2)
    def regions_by_slashes(self, grid: list[str]) -> int:
        n = len(grid)
        parent = list(range(4 * n * n))

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a: int, b: int) -> bool:
            ra, rb = find(a), find(b)
            if ra == rb:
                return False
            parent[ra] = rb
            return True

        def node(i: int, j: int, part: int) -> int:
            return 4 * (i * n + j) + part

        regions = 4 * n * n
        for i, row in enumerate(grid):
            for j, char in enumerate(row):
                if char == "/":
                    regions -= int(union(node(i, j, 0), node(i, j, 3)))
                    regions -= int(union(node(i, j, 1), node(i, j, 2)))
                elif char == "\\":
                    regions -= int(union(node(i, j, 0), node(i, j, 1)))
                    regions -= int(union(node(i, j, 2), node(i, j, 3)))
                else:
                    regions -= int(union(node(i, j, 0), node(i, j, 1)))
                    regions -= int(union(node(i, j, 1), node(i, j, 2)))
                    regions -= int(union(node(i, j, 2), node(i, j, 3)))
                if j + 1 < n:
                    regions -= int(union(node(i, j, 1), node(i, j + 1, 3)))
                if i + 1 < n:
                    regions -= int(union(node(i, j, 2), node(i + 1, j, 0)))
        return regions
