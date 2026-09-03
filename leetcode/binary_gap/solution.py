class Solution:
    # Time: O(log n)
    # Space: O(1)
    def binary_gap(self, n: int) -> int:
        best = 0
        prev = -1
        i = 0
        while n:
            if n & 1:
                if prev >= 0:
                    best = max(best, i - prev)
                prev = i
            n >>= 1
            i += 1
        return best
