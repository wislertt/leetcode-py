import bisect


class Solution:
    # Time: O(n log n)
    # Space: O(n)
    def find_right_interval(self, intervals: list[list[int]]) -> list[int]:
        sorted_starts = sorted((interval[0], i) for i, interval in enumerate(intervals))
        starts = [start for start, _ in sorted_starts]
        result: list[int] = []
        for interval in intervals:
            pos = bisect.bisect_left(starts, interval[1])
            result.append(sorted_starts[pos][1] if pos < len(starts) else -1)
        return result
