class Solution:
    # Time: O(n)
    # Space: O(1)
    def min_distance(
        self, height: int, width: int, tree: list[int], squirrel: list[int], nuts: list[list[int]]
    ) -> int:
        tr, tc = tree
        sr, sc = squirrel
        to_tree = [abs(r - tr) + abs(c - tc) for r, c in nuts]
        total = 2 * sum(to_tree)
        return min(
            total - a + abs(r - sr) + abs(c - sc) for a, (r, c) in zip(to_tree, nuts, strict=True)
        )
