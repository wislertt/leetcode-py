class Solution:
    # Time: O(n) where n = len(b)
    # Space: O(1)
    def super_pow(self, a: int, b: list[int]) -> int:
        mod = 1337
        result = 1
        a %= mod
        for digit in b:
            result = (pow(result, 10, mod) * pow(a, digit, mod)) % mod
        return result
