class Solution:
    # Time: O(max(rows, cols)^2)
    # Space: O(1) excluding output
    def spiral_matrix_iii(
        self, rows: int, cols: int, r_start: int, c_start: int
    ) -> list[list[int]]:
        result = [[r_start, c_start]]
        r, c, steps, direction = r_start, c_start, 1, 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while len(result) < rows * cols:
            for _ in range(2):
                dr, dc = directions[direction]
                for _ in range(steps):
                    r, c = r + dr, c + dc
                    if 0 <= r < rows and 0 <= c < cols:
                        result.append([r, c])
                direction = (direction + 1) % 4
            steps += 1
        return result
