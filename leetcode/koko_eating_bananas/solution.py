import math


class Solution:
    # Time: O(n log m) where n = piles, m = max(piles)
    # Space: O(1)
    def min_eating_speed(self, piles: list[int], h: int) -> int:
        left, right = 1, max(piles)
        result = right
        while left <= right:
            speed = (left + right) // 2
            hours_needed = sum(math.ceil(pile / speed) for pile in piles)
            if hours_needed <= h:
                result = speed  # speed works, try slower
                right = speed - 1
            else:
                left = speed + 1  # too slow, eat faster
        return result
