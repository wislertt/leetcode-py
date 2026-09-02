class Solution:
    # Time: O(rows * cols)
    # Space: O(cols)
    def maximal_rectangle(self, matrix: list[list[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        cols = len(matrix[0])
        heights = [0] * cols
        best = 0
        for row in matrix:
            for j, val in enumerate(row):
                heights[j] = heights[j] + 1 if val == "1" else 0
            best = max(best, self.largest_rectangle_area(heights))
        return best

    def largest_rectangle_area(self, heights: list[int]) -> int:
        stack: list[int] = []
        best = 0
        extended = [*heights, 0]
        for i, h in enumerate(extended):
            while stack and extended[stack[-1]] >= h:
                height = extended[stack.pop()]
                left = stack[-1] if stack else -1
                best = max(best, height * (i - left - 1))
            stack.append(i)
        return best
