class Solution:
    # Time: O(n)
    # Space: O(1)
    def fib(self, n: int) -> int:
        prev, curr = 0, 1
        for _ in range(n):
            prev, curr = curr, prev + curr
        return prev
