class NumMatrix:
    # Time: O(m * n) precompute, O(1) per query
    # Space: O(m * n)
    def __init__(self, matrix: list[list[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0]) if rows else 0
        # prefix[r][c] = sum of matrix[0..r-1][0..c-1] (1-indexed).
        self.prefix = [[0] * (cols + 1) for _ in range(rows + 1)]
        for r in range(rows):
            for c in range(cols):
                self.prefix[r + 1][c + 1] = (
                    matrix[r][c] + self.prefix[r][c + 1] + self.prefix[r + 1][c] - self.prefix[r][c]
                )

    def sum_region(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (
            self.prefix[row2 + 1][col2 + 1]
            - self.prefix[row1][col2 + 1]
            - self.prefix[row2 + 1][col1]
            + self.prefix[row1][col1]
        )
