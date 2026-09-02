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
        current = root
        while current is not None:
            # Build the next level using the already-linked current level.
            level_head: Node | None = None
            level_tail: Node | None = None
            while current is not None:
                for child in (current.left, current.right):
                    if child is None:
                        continue
                    if level_tail is None:
                        level_head = child
                    else:
                        level_tail.next = child
                    level_tail = child
                current = current.next
            current = level_head
        return root
