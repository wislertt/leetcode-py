class Solution:
    # Time: O(n)
    # Space: O(1) extra (output excluded)
    def remove_interval(
        self, intervals: list[list[int]], to_be_removed: list[int]
    ) -> list[list[int]]:
        start, end = to_be_removed
        result: list[list[int]] = []
        for a, b in intervals:
            if a >= end or b <= start:
                result.append([a, b])
                continue
            if a < start:
                result.append([a, start])
            if b > end:
                result.append([end, b])
        return result
