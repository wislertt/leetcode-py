class Solution:
    # Time: O(n)
    # Space: O(1)
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1

        t0, t1, t2 = 0, 1, 1
        for _ in range(3, n + 1):
            t0, t1, t2 = t1, t2, t0 + t1 + t2
        return t2
