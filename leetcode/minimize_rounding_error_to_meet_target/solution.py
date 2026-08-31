from decimal import Decimal


class Solution:
    # Time: O(n log n)
    # Space: O(n)
    def minimize_error(self, prices: list[str], target: int) -> str:
        floor_sum = 0
        fracs: list[Decimal] = []
        for p in prices:
            d = Decimal(p)
            floor_sum += int(d)
            if frac := d - int(d):
                fracs.append(frac)
        if not floor_sum <= target <= floor_sum + len(fracs):
            return "-1"
        ceils = target - floor_sum
        fracs.sort(reverse=True)
        error = ceils - sum(fracs[:ceils]) + sum(fracs[ceils:])
        return f"{error:.3f}"
