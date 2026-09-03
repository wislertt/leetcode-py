from collections import defaultdict


class Solution:
    # Time: O(m * n^2)
    # Space: O(m * n)
    def find_black_pixel(self, picture: list[list[str]], target: int) -> int:
        row_counts = [row.count("B") for row in picture]
        cols: dict[int, list[int]] = defaultdict(list)
        for i, row in enumerate(picture):
            for j, pixel in enumerate(row):
                if pixel == "B":
                    cols[j].append(i)

        result = 0
        for rows in cols.values():
            if row_counts[rows[0]] != target or len(rows) != target:
                continue
            if all(picture[r] == picture[rows[0]] for r in rows):
                result += target
        return result
