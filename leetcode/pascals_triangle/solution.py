class Solution:
    # Time: O(n^2)
    # Space: O(1) excluding output
    def generate(self, num_rows: int) -> list[list[int]]:
        triangle: list[list[int]] = [[1]]
        for _ in range(1, num_rows):
            previous = triangle[-1]
            row = [1] + [previous[i] + previous[i + 1] for i in range(len(previous) - 1)] + [1]
            triangle.append(row)
        return triangle
