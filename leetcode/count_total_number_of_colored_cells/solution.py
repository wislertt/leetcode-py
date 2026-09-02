class Solution:
    # Time: O(1)
    # Space: O(1)
    def colored_cells(self, n: int) -> int:
        return 2 * n * n - 2 * n + 1
