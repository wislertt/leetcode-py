class Solution:
    # Time: O(m log m + n log n) — binary search for each bounding edge
    # Space: O(1)
    def min_area(self, image: list[list[str]], x: int, y: int) -> int:
        m, n = len(image), len(image[0])

        def row_has_black(r: int) -> bool:
            return "1" in image[r]

        def col_has_black(c: int) -> bool:
            return any(row[c] == "1" for row in image)

        lo, hi = 0, x
        while lo < hi:
            mid = (lo + hi) // 2
            if row_has_black(mid):
                hi = mid
            else:
                lo = mid + 1
        top = lo

        lo, hi = x, m - 1
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if row_has_black(mid):
                lo = mid
            else:
                hi = mid - 1
        bottom = lo

        lo, hi = 0, y
        while lo < hi:
            mid = (lo + hi) // 2
            if col_has_black(mid):
                hi = mid
            else:
                lo = mid + 1
        left = lo

        lo, hi = y, n - 1
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if col_has_black(mid):
                lo = mid
            else:
                hi = mid - 1
        right = lo

        return (bottom - top + 1) * (right - left + 1)
