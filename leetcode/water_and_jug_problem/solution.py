from math import gcd


class Solution:
    # Time: O(log(min(x, y)))
    # Space: O(1)
    def can_measure_water(self, x: int, y: int, target: int) -> bool:
        if target > x + y:
            return False
        return target % gcd(x, y) == 0
