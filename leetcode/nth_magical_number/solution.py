from math import gcd


class Solution:
    # Time: O(log(n * min(a, b)))
    # Space: O(1)
    def nth_magical_number(self, n: int, a: int, b: int) -> int:
        mod = 10**9 + 7
        lcm = a * b // gcd(a, b)

        def count(x: int) -> int:
            return x // a + x // b - x // lcm

        low, high = 1, n * min(a, b)
        while low < high:
            mid = (low + high) // 2
            if count(mid) >= n:
                high = mid
            else:
                low = mid + 1
        return low % mod
