from functools import cache


class Solution:
    # Time: O(n^2) after scaling n down to units of 25 mL, capped by the
    # shortcut that treats n >= 5000 as an immediate A loss
    # Space: O(n^2) for the memo table
    def soup_servings(self, n: int) -> float:
        units = (n + 24) // 25
        if units >= 200:
            return 1.0

        @cache
        def dp(soup_a: int, soup_b: int) -> float:
            if soup_a <= 0 and soup_b <= 0:
                return 0.5
            if soup_a <= 0:
                return 1.0
            if soup_b <= 0:
                return 0.0
            return (
                dp(soup_a - 4, soup_b)
                + dp(soup_a - 3, soup_b - 1)
                + dp(soup_a - 2, soup_b - 2)
                + dp(soup_a - 1, soup_b - 3)
            ) / 4

        return dp(units, units)
