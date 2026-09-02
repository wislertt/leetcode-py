class Solution:
    # Time: O(n * b) where b is the bit width of the largest value (<= 24)
    # Space: O(1)
    def largest_combination(self, candidates: list[int]) -> int:
        best = 0
        for bit in range(24):
            count = 0
            for value in candidates:
                count += (value >> bit) & 1
            best = max(best, count)
        return best
