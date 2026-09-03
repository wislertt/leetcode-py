class Solution:
    # Time: O(n^2) over the grid cells
    # Space: O(1) extra beyond the input
    def projection_area(self, grid: list[list[int]]) -> int:
        top = sum(1 for row in grid for cube in row if cube > 0)
        front = sum(max(row) for row in grid)
        side = sum(max(col) for col in zip(*grid, strict=True))
        return top + front + side
