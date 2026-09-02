class Solution:
    # Time: O(m log m)
    # Space: O(m)
    def check_valid_cuts(self, n: int, rectangles: list[list[int]]) -> bool:
        return self._has_two_gaps(rectangles, 0) or self._has_two_gaps(rectangles, 1)

    def _has_two_gaps(self, rectangles: list[list[int]], axis: int) -> bool:
        rects = sorted(rectangles, key=lambda rect: (rect[axis], rect[axis + 2]))
        gaps = 0
        end = rects[0][axis + 2]
        for rect in rects:
            if rect[axis] >= end:
                gaps += 1
                if gaps >= 2:
                    return True
            end = max(end, rect[axis + 2])
        return False
