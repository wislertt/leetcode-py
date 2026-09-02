class Solution:
    # Time: O(n)
    # Space: O(1)
    def grid_game(self, grid: list[list[int]]) -> int:
        top = sum(grid[0])
        bottom = 0
        best = None
        for t, b in zip(grid[0], grid[1], strict=True):
            top -= t
            second = max(top, bottom)
            if best is None or second < best:
                best = second
            bottom += b
        return best if best is not None else 0
