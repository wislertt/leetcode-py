class Solution:
    # Time: O(1) - always 6 pairwise distances over 4 fixed points
    # Space: O(1)
    def valid_square(self, p1: list[int], p2: list[int], p3: list[int], p4: list[int]) -> bool:
        pts = (p1, p2, p3, p4)
        dists = sorted(
            (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 for i, a in enumerate(pts) for b in pts[i + 1 :]
        )
        return 0 < dists[0] == dists[3] and dists[4] == dists[5] == 2 * dists[0]
