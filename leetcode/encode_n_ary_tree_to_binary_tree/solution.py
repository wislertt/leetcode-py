from __future__ import annotations

from leetcode_py import TreeNode


class Node:
    def __init__(self, val: int = 0, children: list[Node] | None = None) -> None:
        self.val = val
        self.children = children if children is not None else []


class Codec:
    # Time: O(n) for encode and decode
    # Space: O(n)
    # Encoding: left child = first child, right child = next sibling
    def __init__(self) -> None:
        pass

    def encode(self, root: Node | None) -> TreeNode[int] | None:
        if root is None:
            return None
        bnode = TreeNode[int](root.val)
        prev: TreeNode[int] | None = None
        for child in root.children:
            child_b = self.encode(child)
            if prev is None:
                bnode.left = child_b
            else:
                prev.right = child_b
            prev = child_b
        return bnode

    def decode(self, data: TreeNode[int] | None) -> Node | None:
        if data is None:
            return None
        node = Node(data.val)
        children: list[Node] = []
        cur = data.left
        while cur is not None:
            child = self.decode(cur)
            assert child is not None
            children.append(child)
            cur = cur.right
        node.children = children
        return node
