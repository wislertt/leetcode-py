class Solution:
    # Time: O(n log n)
    # Space: O(1) excluding sort space
    def find_min_arrow_shots(self, points: list[list[int]]) -> int:
        points.sort(key=lambda point: point[1])

        arrows = 1
        arrow_pos = points[0][1]
        for start, end in points[1:]:
            if start > arrow_pos:
                arrows += 1
                arrow_pos = end
        return arrows
