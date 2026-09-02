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
    # Time: O(n)
    # Space: O(log n) recursion depth
    def intersect(self, quad_tree1: Node, quad_tree2: Node) -> Node:
        if quad_tree1.isLeaf:
            return Node(True, True) if quad_tree1.val else quad_tree2
        if quad_tree2.isLeaf:
            return Node(True, True) if quad_tree2.val else quad_tree1
        quadrants = (
            (quad_tree1.topLeft, quad_tree2.topLeft),
            (quad_tree1.topRight, quad_tree2.topRight),
            (quad_tree1.bottomLeft, quad_tree2.bottomLeft),
            (quad_tree1.bottomRight, quad_tree2.bottomRight),
        )
        merged: list[Node] = []
        for left, right in quadrants:
            assert left is not None and right is not None
            merged.append(self.intersect(left, right))
        if all(child.isLeaf and child.val for child in merged):
            return Node(True, True)
        top_left, top_right, bottom_left, bottom_right = merged
        return Node(False, False, top_left, top_right, bottom_left, bottom_right)
