from __future__ import annotations


class NaryNode:
    def __init__(self, val: int = 0, children: list[NaryNode] | None = None) -> None:
        self.val = val
        self.children = children if children is not None else []


class Solution:
    # Time: O(n)
    # Space: O(h)
    def diameter(self, root: NaryNode | None) -> int:
        ans = 0

        def dfs(node: NaryNode | None) -> int:
            nonlocal ans
            if node is None:
                return 0
            first = second = 0
            for child in node.children:
                depth = dfs(child)
                if depth > first:
                    second, first = first, depth
                elif depth > second:
                    second = depth
            ans = max(ans, first + second)
            return 1 + first

        dfs(root)
        return ans
