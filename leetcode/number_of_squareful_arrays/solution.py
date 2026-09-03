from collections import Counter
from functools import cache
from math import isqrt


class Solution:
    # Time: O(k^2 * 2^n) where k is the number of distinct values (k <= n <= 12)
    # Space: O(k * 2^n) for the memo table over (last value, used-element mask)
    def num_squareful_perms(self, nums: list[int]) -> int:
        n = len(nums)
        counts = Counter(nums)
        values = sorted(counts)
        positions = {
            value: sum(1 << i for i, x in enumerate(nums) if x == value) for value in values
        }

        def is_square(x: int) -> bool:
            root = isqrt(x)
            return root * root == x

        neighbors = {value: [b for b in values if is_square(value + b)] for value in values}

        @cache
        def dfs(last: int, mask: int) -> int:
            if mask == (1 << n) - 1:
                return 1
            total = 0
            for neighbor in neighbors[last]:
                if (mask & positions[neighbor]).bit_count() == counts[neighbor]:
                    continue
                free = positions[neighbor] & ~mask
                pick = (free & -free).bit_length() - 1
                total += dfs(neighbor, mask | (1 << pick))
            return total

        return sum(dfs(value, positions[value] & -positions[value]) for value in values)
