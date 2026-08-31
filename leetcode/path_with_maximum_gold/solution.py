class Solution:
    # Time: O(25 * 4^25) worst case, bounded by gold cells
    # Space: O(rows * cols)
    def get_maximum_gold(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def dfs(row: int, col: int) -> int:
            if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == 0:
                return 0
            gold = grid[row][col]
            grid[row][col] = 0
            best = gold + max(
                dfs(row + 1, col),
                dfs(row - 1, col),
                dfs(row, col + 1),
                dfs(row, col - 1),
            )
            grid[row][col] = gold
            return best

        return max((dfs(row, col) for row in range(rows) for col in range(cols)), default=0)
