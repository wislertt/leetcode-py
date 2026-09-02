class Solution:
    # Time: O(n)
    # Space: O(n)
    def max_sum_distinct_triplet(self, x: list[int], y: list[int]) -> int:
        best: dict[int, int] = {}
        for xi, yi in zip(x, y, strict=True):
            if yi > best.get(xi, 0):
                best[xi] = yi
        if len(best) < 3:
            return -1
        return sum(sorted(best.values(), reverse=True)[:3])
