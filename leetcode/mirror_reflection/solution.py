from math import gcd


class Solution:
    # Time: O(log(min(p, q)))
    # Space: O(1)
    def mirror_reflection(self, p: int, q: int) -> int:
        g = gcd(p, q)
        heights, crossings = q // g, p // g
        if heights % 2 == 0:
            return 0
        return 2 if crossings % 2 == 0 else 1
