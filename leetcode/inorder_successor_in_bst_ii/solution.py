from __future__ import annotations


class Node:
    def __init__(self, val: int = 0) -> None:
        self.val = val
        self.left: Node | None = None
        self.right: Node | None = None
        self.parent: Node | None = None


class Solution:
    # Time: O(h)
    # Space: O(1)
    def inorder_successor(self, node: Node) -> Node | None:
        if node.right is not None:
            succ = node.right
            while succ.left is not None:
                succ = succ.left
            return succ
        child = node
        parent = node.parent
        while parent is not None and parent.right is child:
            child = parent
            parent = parent.parent
        return parent
