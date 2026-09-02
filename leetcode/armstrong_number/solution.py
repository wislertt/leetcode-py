class Solution:
    # Time: O(log n)
    # Space: O(1)
    def is_armstrong(self, n: int) -> bool:
        digits = str(n)
        k = len(digits)
        return sum(int(d) ** k for d in digits) == n
