from __future__ import annotations


class Node:
    def __init__(self, val: int = 0, children: list[Node] | None = None) -> None:
        self.val = val
        self.children = children if children is not None else []


class Solution:
    # Time: O(n)
    # Space: O(1)

    def find_root(self, tree: list[Node]) -> Node:
        # Every value appears once as a node and once more as a child if it is
        # not the root, so XOR-ing all node values with all child values leaves
        # exactly the root's value.
        x = 0
        for node in tree:
            x ^= node.val
            for child in node.children:
                x ^= child.val
        return next(node for node in tree if node.val == x)
