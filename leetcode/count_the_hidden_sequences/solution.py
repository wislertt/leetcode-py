class Solution:
    # Time: O(n)
    # Space: O(1)
    def numberOfArrays(  # noqa: N802
        self, differences: list[int], lower: int, upper: int
    ) -> int:
        offset = 0
        min_offset = 0
        max_offset = 0

        for difference in differences:
            offset += difference
            min_offset = min(min_offset, offset)
            max_offset = max(max_offset, offset)

        possible = (upper - lower) - (max_offset - min_offset) + 1
        return max(0, possible)
