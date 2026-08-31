class Solution:
    # Time: O(n log n)
    # Space: O(n)
    def find_min_difference(self, time_points: list[str]) -> int:
        minutes = sorted(int(t[:2]) * 60 + int(t[3:]) for t in time_points)
        best = 24 * 60 - (minutes[-1] - minutes[0])
        for i in range(len(minutes) - 1):
            best = min(best, minutes[i + 1] - minutes[i])
        return best
