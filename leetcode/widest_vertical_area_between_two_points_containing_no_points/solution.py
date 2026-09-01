from itertools import pairwise


class Solution:
    # Time: O(n log n)
    # Space: O(n) for the sorted x-coordinates
    def max_width_of_vertical_area(self, points: list[list[int]]) -> int:
        return max(curr - prev for prev, curr in pairwise(sorted(x for x, _ in points)))
