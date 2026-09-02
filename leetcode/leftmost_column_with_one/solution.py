class BinaryMatrix:
    # Test-harness API: backs the interactive get/dimensions interface with the matrix
    def __init__(self, mat: list[list[int]]) -> None:
        self.mat = mat
        self.calls = 0

    def get(self, row: int, col: int) -> int:
        self.calls += 1
        return self.mat[row][col]

    def dimensions(self) -> list[int]:
        return [len(self.mat), len(self.mat[0])]


class Solution:
    # Time: O(rows + cols)
    # Space: O(1)
    def leftmost_column_with_one(self, binary_matrix: BinaryMatrix) -> int:
        rows, cols = binary_matrix.dimensions()
        row, col = 0, cols - 1
        result = -1
        while row < rows and col >= 0:
            if binary_matrix.get(row, col) == 1:
                result = col
                col -= 1
            else:
                row += 1
        return result
