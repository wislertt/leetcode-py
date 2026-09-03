from collections import Counter
from functools import reduce
from math import gcd


class Solution:
    # Time: O(n + k log m) where k is distinct values, m is max count
    # Space: O(k)
    def has_group_size_x(self, deck: list[int]) -> bool:
        counts = list(Counter(deck).values())
        return reduce(gcd, counts) > 1
