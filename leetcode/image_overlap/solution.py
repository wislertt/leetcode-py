from collections import Counter


class Solution:
    # Time: O(n^4) where n is the image size (pairs of 1 bits across both images)
    # Space: O(n^2) for the shift counter
    def largest_overlap(self, img1: list[list[int]], img2: list[list[int]]) -> int:
        ones1 = [(i, j) for i, row in enumerate(img1) for j, val in enumerate(row) if val]
        ones2 = [(i, j) for i, row in enumerate(img2) for j, val in enumerate(row) if val]
        shifts: Counter[tuple[int, int]] = Counter()
        best = 0
        for i1, j1 in ones1:
            for i2, j2 in ones2:
                shift = (i2 - i1, j2 - j1)
                shifts[shift] += 1
                best = max(best, shifts[shift])
        return best
