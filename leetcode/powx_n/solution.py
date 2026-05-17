class Solution:
    # Time: O(log n)
    # Space: O(log n)
    def my_pow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        if n < 0:
            return 1.0 / self.my_pow(x, -n)
        if n % 2 == 0:
            half = self.my_pow(x, n // 2)
            return half * half
        return x * self.my_pow(x, n - 1)
