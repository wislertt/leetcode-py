class Solution:
    # Time: O(rows * cols) - each cell is filled at most once by the two-pointer sweep
    # Space: O(1) extra (the output matrix is not counted)
    def restore_matrix(self, row_sum: list[int], col_sum: list[int]) -> list[list[int]]:
        rs = list(row_sum)
        cs = list(col_sum)
        rows, cols = len(rs), len(cs)
        matrix = [[0] * cols for _ in range(rows)]
        r = 0
        c = 0
        while r < rows and c < cols:
            value = min(rs[r], cs[c])
            matrix[r][c] = value
            rs[r] -= value
            cs[c] -= value
            if rs[r] == 0:
                r += 1
            if cs[c] == 0:
                c += 1
        return matrix
