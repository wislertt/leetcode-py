class Solution:
    # Time: O(sum k_x^2) where k_x = points sharing the same x, at most O(n^2)
    # Space: O(n)
    def min_area_rect(self, points: list[list[int]]) -> int:
        columns: dict[int, list[int]] = {}
        for x, y in points:
            columns.setdefault(x, []).append(y)

        last_x: dict[tuple[int, int], int] = {}
        result = 0
        for x in sorted(columns):
            ys = sorted(columns[x])
            for i, y1 in enumerate(ys):
                for y2 in ys[i + 1 :]:
                    pair = (y1, y2)
                    prev_x = last_x.get(pair)
                    if prev_x is not None:
                        area = (x - prev_x) * (y2 - y1)
                        if result == 0 or area < result:
                            result = area
                    last_x[pair] = x
        return result
