class Solution:
    # Time: O(m * n)
    # Space: O(r * c) for the output matrix
    def matrix_reshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        m, n = len(mat), len(mat[0])
        if m * n != r * c:
            return mat
        result: list[list[int]] = []
        row: list[int] = []
        for values in mat:
            for value in values:
                row.append(value)
                if len(row) == c:
                    result.append(row)
                    row = []
        return result
