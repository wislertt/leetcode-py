from collections import defaultdict


class Solution:
    # Time: O(n^2)
    # Space: O(n)
    def number_of_boomerangs(self, points: list[list[int]]) -> int:
        total = 0
        for i, (xi, yi) in enumerate(points):
            dist_counts: dict[int, int] = defaultdict(int)
            for j, (xj, yj) in enumerate(points):
                if j == i:
                    continue
                dist_counts[(xj - xi) ** 2 + (yj - yi) ** 2] += 1
            total += sum(count * (count - 1) for count in dist_counts.values())
        return total
