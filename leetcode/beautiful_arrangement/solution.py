class Solution:
    # Time: O(n * 2^n)
    # Space: O(2^n)
    def count_arrangement(self, n: int) -> int:
        full = (1 << n) - 1
        memo: dict[int, int] = {}

        def count(mask: int) -> int:
            if mask == full:
                return 1
            if mask in memo:
                return memo[mask]
            pos = mask.bit_count() + 1
            total = 0
            for value in range(1, n + 1):
                bit = 1 << (value - 1)
                if not mask & bit and (value % pos == 0 or pos % value == 0):
                    total += count(mask | bit)
            memo[mask] = total
            return total

        return count(0)
