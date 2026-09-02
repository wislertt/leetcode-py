class Solution:
    # Time: O(n * log(max - min))
    # Space: O(1)
    def kth_smallest(self, matrix: list[list[int]], k: int) -> int:
        def count_at_most(target: int) -> int:
            count = 0
            row, col = len(matrix) - 1, 0
            while row >= 0 and col < len(matrix):
                if matrix[row][col] <= target:
                    count += row + 1
                    col += 1
                else:
                    row -= 1
            return count

        lo, hi = matrix[0][0], matrix[-1][-1]
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if count_at_most(mid) < k:
                lo = mid + 1
            else:
                hi = mid
        return lo
