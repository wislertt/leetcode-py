class Solution:
    # Time: O(rows * cols^2)
    # Space: O(cols^2)
    def cherry_pickup(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        cols_sq = cols * cols
        # -1 marks unreachable (col, col) state pairs.
        prev = [-1] * cols_sq
        prev[cols - 1] = grid[0][0] + grid[0][cols - 1]
        for row in range(1, rows):
            cur = [-1] * cols_sq
            row_grid = grid[row]
            for c1 in range(cols):
                for c2 in range(cols):
                    best = -1
                    for d1 in (-1, 0, 1):
                        p1 = c1 + d1
                        if p1 < 0 or p1 >= cols:
                            continue
                        for d2 in (-1, 0, 1):
                            p2 = c2 + d2
                            if p2 < 0 or p2 >= cols:
                                continue
                            val = prev[p1 * cols + p2]
                            if val > best:
                                best = val
                    if best < 0:
                        continue
                    gain = row_grid[c1] + (row_grid[c2] if c1 != c2 else 0)
                    cur[c1 * cols + c2] = best + gain
            prev = cur
        return max(prev)
