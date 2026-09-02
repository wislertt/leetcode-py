class Solution:
    # Time: O(n^2)
    # Space: O(1)
    def max_matrix_sum(self, matrix: list[list[int]]) -> int:
        total = 0
        neg_count = 0
        min_abs = 10**9
        for row in matrix:
            for value in row:
                total += abs(value)
                neg_count += value < 0
                min_abs = min(min_abs, abs(value))
        if neg_count % 2:
            total -= 2 * min_abs
        return total
