from __future__ import annotations


class NaryNode:
    def __init__(self, val: int = 0, children: list[NaryNode] | None = None) -> None:
        self.val = val
        self.children = children if children is not None else []


class Solution:
    # Time: O(n)
    # Space: O(n)
    def preorder(self, root: NaryNode | None) -> list[int]:
        if root is None:
            return []
        result: list[int] = []
        stack: list[NaryNode] = [root]
        while stack:
            node = stack.pop()
            result.append(node.val)
            stack.extend(reversed(node.children))
        return result
