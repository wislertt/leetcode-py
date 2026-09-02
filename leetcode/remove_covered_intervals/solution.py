class Solution:
    def remove_covered_intervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda interval: (interval[0], -interval[1]))
        count = 0
        best_end = -1
        for _, right in intervals:
            if right > best_end:
                count += 1
                best_end = right
        return count
