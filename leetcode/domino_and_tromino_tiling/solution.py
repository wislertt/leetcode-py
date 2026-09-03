class Solution:
    # Time: O(n)
    # Space: O(1)
    def num_tilings(self, n: int) -> int:
        mod = 1_000_000_007
        # f(i): ways to fully tile a 2 x i board; recurrence f(i) = 2f(i-1) + f(i-3)
        f0, f1, f2 = 1, 1, 2  # f(0), f(1), f(2)
        if n <= 2:
            return (f0, f1, f2)[n]
        for _ in range(3, n + 1):
            f0, f1, f2 = f1, f2, (2 * f2 + f0) % mod
        return f2
