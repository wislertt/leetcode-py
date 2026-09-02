from __future__ import annotations

from collections import deque


class NaryNode:
    def __init__(self, val: int = 0, children: list[NaryNode] | None = None) -> None:
        self.val = val
        self.children = children if children is not None else []


class Solution:
    # Time: O(n)
    # Space: O(n)
    def clone_tree(self, root: NaryNode | None) -> NaryNode | None:
        if root is None:
            return None
        clones: dict[NaryNode, NaryNode] = {root: NaryNode(root.val)}
        queue: deque[NaryNode] = deque([root])
        while queue:
            node = queue.popleft()
            for child in node.children:
                clones[child] = NaryNode(child.val)
                clones[node].children.append(clones[child])
                queue.append(child)
        return clones[root]
