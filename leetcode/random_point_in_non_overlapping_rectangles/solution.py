import random
from bisect import bisect_right


class Solution:
    # Weight the rectangles by their integer-point counts with a prefix sum,
    # draw a uniform offset into the total, bisect to the owning rectangle and
    # map the leftover offset onto a (col, row) inside it. Every integer point
    # (perimeter included) gets exactly one offset, so points are uniform.
    # Time: __init__ O(n), pick O(log n)
    # Space: O(n)
    def __init__(self, rects: list[list[int]]) -> None:
        self._rects = rects
        self._prefix: list[int] = []
        total = 0
        for a, b, x, y in rects:
            total += (x - a + 1) * (y - b + 1)
            self._prefix.append(total)
        self._total = total

    def pick(self) -> list[int]:
        target = random.randrange(self._total)
        idx = bisect_right(self._prefix, target)
        base = self._prefix[idx - 1] if idx else 0
        a, b, x, _ = self._rects[idx]
        width = x - a + 1
        offset = target - base
        return [a + offset % width, b + offset // width]
