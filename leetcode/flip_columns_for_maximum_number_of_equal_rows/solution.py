class Solution:
    # Time: O(m * n)
    # Space: O(m * n)
    def max_equal_rows_after_flips(self, matrix: list[list[int]]) -> int:
        counts: dict[tuple[int, ...], int] = {}
        for row in matrix:
            key = tuple(row) if row[0] == 0 else tuple(1 - x for x in row)
            counts[key] = counts.get(key, 0) + 1
        return max(counts.values())
