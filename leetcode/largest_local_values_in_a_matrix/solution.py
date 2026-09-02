class Solution:
    # Time: O(n^2) - each of the (n - 2)^2 windows scans a fixed 3 x 3 area
    # Space: O(1) extra - excluding the (n - 2) x (n - 2) output matrix
    def largest_local(self, grid: list[list[int]]) -> list[list[int]]:
        n = len(grid)
        return [
            [max(grid[i + a][j + b] for a in range(3) for b in range(3)) for j in range(n - 2)]
            for i in range(n - 2)
        ]
