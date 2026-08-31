class Solution:
    # Time: O(n^2)
    # Space: O(1) excluding the output matrix
    def generate_matrix(self, n: int) -> list[list[int]]:
        matrix = [[0] * n for _ in range(n)]
        top, bottom = 0, n - 1
        left, right = 0, n - 1
        value = 1

        while top <= bottom and left <= right:
            # Move right along the top row
            for col in range(left, right + 1):
                matrix[top][col] = value
                value += 1
            top += 1

            # Move down along the right column
            for row in range(top, bottom + 1):
                matrix[row][right] = value
                value += 1
            right -= 1

            # Move left along the bottom row
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    matrix[bottom][col] = value
                    value += 1
                bottom -= 1

            # Move up along the left column
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    matrix[row][left] = value
                    value += 1
                left += 1

        return matrix
