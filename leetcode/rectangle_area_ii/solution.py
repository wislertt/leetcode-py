class Solution:
    # Time: O(n^2) cells per sweep with n <= 200 rectangles, so ~10^5 cell updates
    # Space: O(n^2) for the compressed coverage grid
    def rectangle_area(self, rectangles: list[list[int]]) -> int:
        mod = 1_000_000_007
        xs = sorted({r[0] for r in rectangles} | {r[2] for r in rectangles})
        ys = sorted({r[1] for r in rectangles} | {r[3] for r in rectangles})
        x_index = {x: i for i, x in enumerate(xs)}
        y_index = {y: i for i, y in enumerate(ys)}
        covered = [[False] * (len(ys) - 1) for _ in range(len(xs) - 1)]
        for x1, y1, x2, y2 in rectangles:
            for i in range(x_index[x1], x_index[x2]):
                row = covered[i]
                for j in range(y_index[y1], y_index[y2]):
                    row[j] = True
        total = 0
        for i in range(len(xs) - 1):
            width = xs[i + 1] - xs[i]
            row = covered[i]
            for j in range(len(ys) - 1):
                if row[j]:
                    total += width * (ys[j + 1] - ys[j])
        return total % mod
