class Solution:
    # Time: O(n^2)
    # Space: O(n^2)
    def find_missing_and_repeated_values(self, grid: list[list[int]]) -> list[int]:
        n = len(grid)
        counts: dict[int, int] = {}
        repeated = 0
        for row in grid:
            for val in row:
                if val in counts:
                    repeated = val
                counts[val] = counts.get(val, 0) + 1
        total = n * n
        missing = total * (total + 1) // 2 - sum(counts)
        return [repeated, missing]
