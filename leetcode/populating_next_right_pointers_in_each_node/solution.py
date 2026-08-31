from __future__ import annotations


class Node:
    def __init__(
        self,
        val: int = 0,
        left: Node | None = None,
        right: Node | None = None,
        next: Node | None = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    # Time: O(n)
    # Space: O(1)
    def connect(self, root: Node | None) -> Node | None:
        leftmost = root
        while leftmost is not None and leftmost.left is not None:
            head = leftmost
            while head is not None:
                left = head.left
                right = head.right
                assert left is not None and right is not None
                left.next = right
                if head.next is not None:
                    right.next = head.next.left
                head = head.next
            leftmost = leftmost.left
        return root
