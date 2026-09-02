from __future__ import annotations

from collections import deque


class NaryNode:
    def __init__(self, val: int = 0, children: list[NaryNode] | None = None) -> None:
        self.val = val
        self.children = children if children is not None else []


class Solution:
    # Time: O(n)
    # Space: O(w)
    def level_order(self, root: NaryNode | None) -> list[list[int]]:
        levels: list[list[int]] = []
        if root is None:
            return levels
        current: deque[NaryNode] = deque([root])
        while current:
            levels.append([node.val for node in current])
            nxt: deque[NaryNode] = deque()
            for node in current:
                nxt.extend(node.children)
            current = nxt
        return levels
