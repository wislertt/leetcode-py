class Solution:
    # Time: O(m + n)
    # Space: O(1)
    def search_matrix(self, matrix: list[list[int]], target: int) -> bool:
        row, col = 0, len(matrix[0]) - 1
        while row < len(matrix) and col >= 0:
            val = matrix[row][col]
            if val == target:
                return True
            if val > target:
                col -= 1
            else:
                row += 1
        return False
