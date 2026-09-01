from math import isqrt


class Solution:
    # Time: O(m * log(min(ranks) * cars^2)) where m = len(ranks)
    # Space: O(1)
    def repair_cars(self, ranks: list[int], cars: int) -> int:
        lo, hi = 1, min(ranks) * cars * cars
        while lo < hi:
            mid = (lo + hi) // 2
            if sum(isqrt(mid // r) for r in ranks) >= cars:
                hi = mid
            else:
                lo = mid + 1
        return lo
