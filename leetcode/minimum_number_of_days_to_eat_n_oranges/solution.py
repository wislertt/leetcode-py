from functools import cache


class Solution:
    # Time: O(log^2 n)
    # Space: O(log^2 n)
    def min_days(self, n: int) -> int:
        @cache
        def eat(remaining: int) -> int:
            if remaining <= 1:
                return remaining
            by_two = remaining % 2 + 1 + eat(remaining // 2)
            by_three = remaining % 3 + 1 + eat(remaining // 3)
            return min(by_two, by_three)

        return eat(n)
