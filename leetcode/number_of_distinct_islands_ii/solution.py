class Solution:
    # Time: O(m * n * log(m * n))
    # Space: O(m * n)
    def num_distinct_islands_ii(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        seen = [[False] * n for _ in range(m)]

        def dfs(i: int, j: int, shape: list[tuple[int, int]]) -> None:
            if not (0 <= i < m and 0 <= j < n) or seen[i][j] or grid[i][j] == 0:
                return
            seen[i][j] = True
            shape.append((i, j))
            for a, b in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                dfs(i + a, j + b, shape)

        def normalize(shape: list[tuple[int, int]]) -> tuple[tuple[int, int], ...]:
            variants: list[list[tuple[int, int]]] = [[] for _ in range(8)]
            for i, j in shape:
                variants[0].append((i, j))
                variants[1].append((i, -j))
                variants[2].append((-i, j))
                variants[3].append((-i, -j))
                variants[4].append((j, i))
                variants[5].append((j, -i))
                variants[6].append((-j, i))
                variants[7].append((-j, -i))
            norm = []
            for e in variants:
                e.sort()
                x0, y0 = e[0]
                norm.append(tuple((x - x0, y - y0) for x, y in e))
            norm.sort()
            return norm[0]

        islands: set[tuple[tuple[int, int], ...]] = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] and not seen[i][j]:
                    shape: list[tuple[int, int]] = []
                    dfs(i, j, shape)
                    islands.add(normalize(shape))
        return len(islands)
