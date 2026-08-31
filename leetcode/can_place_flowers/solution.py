class Solution:
    # Time: O(m) where m = len(flowerbed)
    # Space: O(m)
    def can_place_flowers(self, flowerbed: list[int], n: int) -> bool:
        planted = 0
        bed = flowerbed[:]
        for i, plot in enumerate(bed):
            left_empty = i == 0 or bed[i - 1] == 0
            right_empty = i == len(bed) - 1 or bed[i + 1] == 0
            if plot == 0 and left_empty and right_empty:
                bed[i] = 1
                planted += 1
        return planted >= n
