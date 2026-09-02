import math


class Solution:
    # Time: O(n^2)
    # Space: O(n)
    def get_permutation(self, n: int, k: int) -> str:
        digits = [str(i) for i in range(1, n + 1)]
        remaining = k - 1
        parts: list[str] = []
        for i in range(n, 0, -1):
            block_size = math.factorial(i - 1)
            idx, remaining = divmod(remaining, block_size)
            parts.append(digits.pop(idx))
        return "".join(parts)
