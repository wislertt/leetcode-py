class Solution:
    # Time: O(b), b = number of differing bits (<= 31)
    # Space: O(1)
    def hamming_distance(self, x: int, y: int) -> int:
        return (x ^ y).bit_count()
