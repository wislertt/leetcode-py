class Solution:
    # Time: O(1)
    # Space: O(1)
    def is_rectangle_overlap(self, rec1: list[int], rec2: list[int]) -> bool:
        overlap_x = max(rec1[0], rec2[0]) < min(rec1[2], rec2[2])
        overlap_y = max(rec1[1], rec2[1]) < min(rec1[3], rec2[3])
        return overlap_x and overlap_y
