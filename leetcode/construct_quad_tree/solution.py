from __future__ import annotations


# ruff: noqa: N803
class Node:
    def __init__(
        self,
        val: bool,
        isLeaf: bool,
        topLeft: Node | None = None,
        topRight: Node | None = None,
        bottomLeft: Node | None = None,
        bottomRight: Node | None = None,
    ) -> None:
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    # Time: O(n^2) every cell visited once per level, log n levels
    # Space: O(log n) recursion depth (tree height)
    def construct(self, grid: list[list[int]]) -> Node:
        def build(row: int, col: int, size: int) -> Node:
            first = grid[row][col]
            uniform = True
            for r in range(row, row + size):
                for c in range(col, col + size):
                    if grid[r][c] != first:
                        uniform = False
                        break
                if not uniform:
                    break
            if uniform:
                return Node(val=bool(first), isLeaf=True)
            half = size // 2
            return Node(
                val=True,
                isLeaf=False,
                topLeft=build(row, col, half),
                topRight=build(row, col + half, half),
                bottomLeft=build(row + half, col, half),
                bottomRight=build(row + half, col + half, half),
            )

        return build(0, 0, len(grid))
