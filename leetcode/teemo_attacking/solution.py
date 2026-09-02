class Solution:
    # Time: O(n)
    # Space: O(1)
    def find_poisoned_duration(self, time_series: list[int], duration: int) -> int:
        total = 0
        for i, t in enumerate(time_series):
            if i + 1 < len(time_series):
                total += min(duration, time_series[i + 1] - t)
            else:
                total += duration
        return total
