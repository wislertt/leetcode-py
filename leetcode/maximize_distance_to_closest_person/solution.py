class Solution:
    # Time: O(n)
    # Space: O(1)
    def max_dist_to_closest(self, seats: list[int]) -> int:
        best = 0
        prev = -1
        n = len(seats)
        for i, occupied in enumerate(seats):
            if occupied:
                best = i if prev < 0 else max(best, (i - prev) // 2)
                prev = i
        return max(best, n - 1 - prev)
