class Solution:
    # Time: O(n log n)
    # Space: O(n)
    def height_checker(self, heights: list[int]) -> int:
        expected = sorted(heights)
        return sum(a != b for a, b in zip(heights, expected, strict=True))
