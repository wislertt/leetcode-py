class Solution:
    # Time: O(m*n log(m*n))
    # Space: O(m*n)
    def min_operations(self, grid: list[list[int]], x: int) -> int:
        vals = [v for row in grid for v in row]
        rem = vals[0] % x
        if any(v % x != rem for v in vals):
            return -1
        vals.sort()
        median = vals[len(vals) // 2]
        return sum(abs(v - median) // x for v in vals)
