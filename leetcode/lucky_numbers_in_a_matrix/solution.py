class Solution:
    # Time: O(m * n)
    # Space: O(n)
    def lucky_numbers(self, matrix: list[list[int]]) -> list[int]:
        col_max = [max(col) for col in zip(*matrix, strict=True)]
        return [row_min for row in matrix if (row_min := min(row)) in col_max]
