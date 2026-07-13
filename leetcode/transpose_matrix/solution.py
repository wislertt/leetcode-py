class Solution:
    # Time: O(m * n)
    # Space: O(m * n)
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        rows = len(matrix)
        cols = len(matrix[0])
        return [[matrix[row][col] for row in range(rows)] for col in range(cols)]
