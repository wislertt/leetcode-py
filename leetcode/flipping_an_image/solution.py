class Solution:
    # Time: O(n^2)
    # Space: O(1) extra (output not counted)
    def flip_and_invert_image(self, image: list[list[int]]) -> list[list[int]]:
        for row in image:
            left, right = 0, len(row) - 1
            while left < right:
                row[left], row[right] = 1 - row[right], 1 - row[left]
                left += 1
                right -= 1
            if left == right:
                row[left] = 1 - row[left]
        return image
