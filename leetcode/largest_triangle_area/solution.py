from itertools import combinations


class Solution:
    # Time: O(n^3)
    # Space: O(1)
    def largest_triangle_area(self, points: list[list[int]]) -> float:
        best = 0.0
        for (ax, ay), (bx, by), (cx, cy) in combinations(points, 3):
            area = abs((bx - ax) * (cy - ay) - (by - ay) * (cx - ax)) / 2
            best = max(best, area)
        return best
