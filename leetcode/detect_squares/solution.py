from collections import Counter


class DetectSquares:
    # Time: O(1) per add
    # Space: O(n) for unique points
    def __init__(self) -> None:
        self.point_counts: Counter[tuple[int, int]] = Counter()

    # Time: O(1)
    # Space: O(1)
    def add(self, point: list[int]) -> None:
        self.point_counts[(point[0], point[1])] += 1

    # Time: O(n) - n unique points
    # Space: O(1)
    def count(self, point: list[int]) -> int:
        qx, qy = point
        total = 0

        for (px, py), count in self.point_counts.items():
            # Look for points on the diagonal: equal nonzero distance on both axes.
            if abs(px - qx) != abs(py - qy) or px == qx:
                continue
            total += count * self.point_counts[(px, qy)] * self.point_counts[(qx, py)]

        return total
