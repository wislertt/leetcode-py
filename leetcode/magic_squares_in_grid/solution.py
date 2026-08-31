class Solution:
    # Time: O(rows * cols)
    # Space: O(1)
    def num_magic_squares_inside(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def is_magic(r: int, c: int) -> bool:
            # A 3x3 magic square over 1..9 always has center 5 and sum 15
            if grid[r + 1][c + 1] != 5:
                return False
            vals = [grid[r + i][c + j] for i in range(3) for j in range(3)]
            if sorted(vals) != list(range(1, 10)):
                return False
            if any(sum(grid[r + i][c : c + 3]) != 15 for i in range(3)):
                return False
            if any(sum(grid[r + i][c + j] for i in range(3)) != 15 for j in range(3)):
                return False
            return (
                grid[r][c] + grid[r + 1][c + 1] + grid[r + 2][c + 2] == 15
                and grid[r][c + 2] + grid[r + 1][c + 1] + grid[r + 2][c] == 15
            )

        return sum(is_magic(r, c) for r in range(rows - 2) for c in range(cols - 2))
