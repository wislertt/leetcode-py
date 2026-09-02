class Solution:
    # Time: O(n log n)
    # Space: O(n) for sorting
    def count_days(self, days: int, meetings: list[list[int]]) -> int:
        meetings.sort()
        free = 0
        last = 0
        for start, end in meetings:
            if start > last:
                free += start - last - 1
            last = max(last, end)
        return free + days - last
