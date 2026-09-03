class Solution:
    # Time: O(rows * cols + len(hits) * alpha(rows * cols))
    # Space: O(rows * cols)
    def hit_bricks(self, grid: list[list[int]], hits: list[list[int]]) -> list[int]:
        rows, cols = len(grid), len(grid[0])
        # Work on a grid with every hit brick already erased, then re-add them in
        # reverse: erasures are hard to undo, additions are just unions.
        remaining = [row[:] for row in grid]
        for row, col in hits:
            remaining[row][col] = 0

        top = rows * cols
        parent = list(range(top + 1))
        size = [1] * (top + 1)

        def find(node: int) -> int:
            while parent[node] != node:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node

        def union(left: int, right: int) -> None:
            root_left, root_right = find(left), find(right)
            if root_left == root_right:
                return
            if size[root_left] < size[root_right]:
                root_left, root_right = root_right, root_left
            parent[root_right] = root_left
            size[root_left] += size[root_right]

        def stable_bricks() -> int:
            # Bricks attached to the virtual top node (the node itself adds 1).
            return size[find(top)] - 1

        def add_brick(row: int, col: int) -> None:
            node = row * cols + col
            if row == 0:
                union(node, top)
            for d_row, d_col in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                n_row, n_col = row + d_row, col + d_col
                if 0 <= n_row < rows and 0 <= n_col < cols and remaining[n_row][n_col]:
                    union(node, n_row * cols + n_col)

        for row in range(rows):
            for col in range(cols):
                if remaining[row][col]:
                    add_brick(row, col)

        results: list[int] = []
        for row, col in reversed(hits):
            if grid[row][col] == 0:
                results.append(0)  # erasure on an empty cell, nothing drops
                continue
            before = stable_bricks()
            add_brick(row, col)
            remaining[row][col] = 1
            after = stable_bricks()
            # Re-adding the hit brick itself accounts for one of the newcomers.
            results.append(max(0, after - before - 1))
        results.reverse()
        return results
