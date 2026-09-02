class Solution:
    # Time: O(m * n log n)
    # Space: O(n)
    def largest_submatrix(self, matrix: list[list[int]]) -> int:
        n = len(matrix[0])
        heights = [0] * n
        best = 0
        for row in matrix:
            for j, val in enumerate(row):
                heights[j] = heights[j] + 1 if val else 0
            sorted_heights = sorted(heights, reverse=True)
            for i, h in enumerate(sorted_heights):
                best = max(best, h * (i + 1))
        return best
