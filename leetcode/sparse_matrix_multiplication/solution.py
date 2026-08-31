class Solution:
    # Time: O(m * k * n) worst case, but skips zero entries of mat1 and mat2
    # Space: O(m * n)
    def multiply(self, mat1: list[list[int]], mat2: list[list[int]]) -> list[list[int]]:
        m, n = len(mat1), len(mat2[0])
        result = [[0] * n for _ in range(m)]
        # Pre-compute non-zero (column, value) pairs per row of mat2.
        mat2_nonzero = [[(j, val) for j, val in enumerate(row) if val != 0] for row in mat2]
        for i, row in enumerate(mat1):
            for t, mat1_val in enumerate(row):
                if mat1_val == 0:
                    continue
                for j, mat2_val in mat2_nonzero[t]:
                    result[i][j] += mat1_val * mat2_val
        return result
