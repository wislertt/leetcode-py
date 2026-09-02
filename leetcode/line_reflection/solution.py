class Solution:
    # Time: O(n)
    # Space: O(n)
    def is_reflected(self, points: list[list[int]]) -> bool:
        min_x, max_x = min(x for x, _ in points), max(x for x, _ in points)
        point_set = {(x, y) for x, y in points}
        s = min_x + max_x
        return all((s - x, y) in point_set for x, y in points)
