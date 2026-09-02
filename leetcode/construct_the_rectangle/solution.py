import math


class Solution:
    # Time: O(sqrt(area))
    # Space: O(1)
    def construct_rectangle(self, area: int) -> list[int]:
        width = math.isqrt(area)
        while area % width != 0:
            width -= 1
        return [area // width, width]
