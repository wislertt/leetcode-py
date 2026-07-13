class Solution:
    # Time: O(n log n) where n is total number of intervals
    # Space: O(n)
    def employee_free_time(self, schedule: list[list[list[int]]]) -> list[list[int]]:
        # Flatten all intervals across employees, then merge overlapping ones.
        # Gaps between consecutive merged intervals are the common free time.
        intervals: list[list[int]] = [
            [start, end] for employee in schedule for start, end in employee
        ]
        intervals.sort()

        merged: list[list[int]] = []
        for start, end in intervals:
            if merged and start <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], end)
            else:
                merged.append([start, end])

        free: list[list[int]] = []
        for i in range(1, len(merged)):
            if merged[i - 1][1] < merged[i][0]:
                free.append([merged[i - 1][1], merged[i][0]])
        return free
