class Solution:
    # Time: O(n)
    # Space: O(n)
    def is_rectangle_cover(self, rectangles: list[list[int]]) -> bool:
        area = 0
        corners: set[tuple[int, int]] = set()
        min_x = min_y = 10**9
        max_x = max_y = -(10**9)
        for x, y, a, b in rectangles:
            min_x = min(min_x, x)
            min_y = min(min_y, y)
            max_x = max(max_x, a)
            max_y = max(max_y, b)
            area += (a - x) * (b - y)
            for corner in ((x, y), (a, y), (x, b), (a, b)):
                if corner in corners:
                    corners.remove(corner)
                else:
                    corners.add(corner)
        if area != (max_x - min_x) * (max_y - min_y):
            return False
        return corners == {(min_x, min_y), (max_x, min_y), (min_x, max_y), (max_x, max_y)}
