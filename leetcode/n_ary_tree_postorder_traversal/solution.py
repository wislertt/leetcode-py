from __future__ import annotations


class NaryNode:
    def __init__(self, val: int = 0, children: list[NaryNode] | None = None) -> None:
        self.val = val
        self.children = children if children is not None else []


class Solution:
    # Time: O(n)
    # Space: O(n)
    def postorder(self, root: NaryNode | None) -> list[int]:
        result: list[int] = []
        if root is None:
            return result
        stack = [root]
        while stack:
            node = stack.pop()
            result.append(node.val)
            stack.extend(node.children)
        # Reverse preorder (children visited right-to-left) equals postorder.
        result.reverse()
        return result
