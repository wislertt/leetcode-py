class Solution:
    # Time: O(m*n + f log f) where f is the friend count
    # Space: O(f)
    def min_total_distance(self, grid: list[list[int]]) -> int:
        rows: list[int] = []
        cols: list[int] = []
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    rows.append(r)
                    cols.append(c)
        cols.sort()
        median_row = rows[len(rows) // 2]
        median_col = cols[len(cols) // 2]
        return sum(abs(r - median_row) for r in rows) + sum(abs(c - median_col) for c in cols)
