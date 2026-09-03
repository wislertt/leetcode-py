from itertools import permutations


class Solution:
    # Time: O(4! * 4)
    # Space: O(1)
    def largest_time_from_digits(self, arr: list[int]) -> str:
        best = ""
        for h1, h2, m1, m2 in permutations(arr):
            hour = h1 * 10 + h2
            minute = m1 * 10 + m2
            if hour < 24 and minute < 60:
                candidate = f"{hour:02d}:{minute:02d}"
                if candidate > best:
                    best = candidate
        return best
