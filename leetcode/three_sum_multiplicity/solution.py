from collections import Counter
from math import comb


class Solution:
    # Time: O(n + V^2) where V = 101 distinct values
    # Space: O(V)
    def three_sum_multiplicity(self, arr: list[int], target: int) -> int:
        mod = 10**9 + 7
        count = Counter(arr)
        values = sorted(count)
        total = 0
        for i, x in enumerate(values):
            for y in values[i:]:
                z = target - x - y
                if z < y or z not in count:
                    continue
                if x == y == z:
                    total += comb(count[x], 3)
                elif x == y:
                    total += comb(count[x], 2) * count[z]
                elif y == z:
                    total += comb(count[y], 2) * count[x]
                else:
                    total += count[x] * count[y] * count[z]
        return total % mod
