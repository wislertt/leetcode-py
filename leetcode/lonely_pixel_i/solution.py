class Solution:
    # Time: O(m * n)
    # Space: O(m + n)
    def find_lonely_pixel(self, picture: list[list[str]]) -> int:
        if not picture:
            return 0
        m, n = len(picture), len(picture[0])
        row_counts = [row.count("B") for row in picture]
        col_counts = [sum(1 for r in range(m) if picture[r][c] == "B") for c in range(n)]
        return sum(
            1
            for r in range(m)
            for c in range(n)
            if picture[r][c] == "B" and row_counts[r] == 1 and col_counts[c] == 1
        )
