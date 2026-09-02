from __future__ import annotations


class Node:
    def __init__(self, val: int = 0) -> None:
        self.val = val
        self.left: Node | None = None
        self.right: Node | None = None
        self.parent: Node | None = None


class Solution:
    # Time: O(h) where h is the height of the tree
    # Space: O(1)
    def lowest_common_ancestor(self, p: Node, q: Node) -> Node:
        a: Node | None = p
        b: Node | None = q
        while a is not b:
            a = q if a.parent is None else a.parent
            b = p if b.parent is None else b.parent
        assert a is not None
        return a
