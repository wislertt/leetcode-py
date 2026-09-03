from collections import defaultdict
from itertools import combinations


class Solution:
    # Time: O(n^2 + sum(g^2)) over diagonal groups
    # Space: O(n^2)
    def min_area_free_rect(self, points: list[list[int]]) -> float:
        pts = [complex(x, y) for x, y in points]
        groups: dict[tuple[complex, float], list[tuple[complex, complex]]] = defaultdict(list)
        for p1, p2 in combinations(pts, 2):
            center = (p1 + p2) / 2
            diag_sq = abs(p1 - p2) ** 2
            groups[(center, diag_sq)].append((p1, p2))
        best = float("inf")
        for diags in groups.values():
            for (p1, p2), (p3, _p4) in combinations(diags, 2):
                area = abs(p1 - p3) * abs(p2 - p3)
                best = min(best, area)
        return best if best != float("inf") else 0.0
