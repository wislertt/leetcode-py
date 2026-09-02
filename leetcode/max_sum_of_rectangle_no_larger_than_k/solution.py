from bisect import bisect_left, insort


class Solution:
    # Time: O(m^2 * n * log n)
    # Space: O(n)
    def max_sum_submatrix(self, matrix: list[list[int]], k: int) -> int:
        rows, cols = len(matrix), len(matrix[0])
        best = -(10**9)
        for top in range(rows):
            col_sums = [0] * cols
            for bottom in range(top, rows):
                row = matrix[bottom]
                for c in range(cols):
                    col_sums[c] += row[c]
                sorted_sums = [0]
                running = 0
                for s in col_sums:
                    running += s
                    i = bisect_left(sorted_sums, running - k)
                    if i < len(sorted_sums):
                        best = max(best, running - sorted_sums[i])
                    insort(sorted_sums, running)
        return best
