class Solution:
    # Time: O(rows^2 * cols)
    # Space: O(cols)
    def num_submatrix_sum_target(self, matrix: list[list[int]], target: int) -> int:
        rows, cols = len(matrix), len(matrix[0])
        count = 0
        for top in range(rows):
            col_sums = [0] * cols
            for bottom in range(top, rows):
                for c in range(cols):
                    col_sums[c] += matrix[bottom][c]
                prefix: dict[int, int] = {0: 1}
                running = 0
                for s in col_sums:
                    running += s
                    count += prefix.get(running - target, 0)
                    prefix[running] = prefix.get(running, 0) + 1
        return count
