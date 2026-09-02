from __future__ import annotations


class NaryNode:
    def __init__(self, val: int = 0, children: list[NaryNode] | None = None) -> None:
        self.val = val
        self.children = children if children is not None else []


class Solution:
    # Time: O(n)
    # Space: O(w)
    def max_depth(self, root: NaryNode | None) -> int:
        if root is None:
            return 0
        depth = 0
        level: list[NaryNode] = [root]
        while level:
            depth += 1
            next_level: list[NaryNode] = []
            for node in level:
                next_level.extend(node.children)
            level = next_level
        return depth
