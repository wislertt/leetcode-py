from math import gcd


class Solution:
    # Time: O(n * log(max(width, height)))
    # Space: O(n)
    def interchangeable_rectangles(self, rectangles: list[list[int]]) -> int:
        counts: dict[tuple[int, int], int] = {}
        pairs = 0
        for width, height in rectangles:
            divisor = gcd(width, height)
            ratio = (width // divisor, height // divisor)
            pairs += counts.get(ratio, 0)
            counts[ratio] = counts.get(ratio, 0) + 1
        return pairs
