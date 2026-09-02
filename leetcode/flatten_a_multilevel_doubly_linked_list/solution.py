from __future__ import annotations


class Node:
    def __init__(
        self,
        val: int = 0,
        prev: Node | None = None,
        next: Node | None = None,
        child: Node | None = None,
    ) -> None:
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    # Time: O(n) per level splice, O(n * depth) worst case
    # Space: O(1)
    def flatten(self, head: Node | None) -> Node | None:
        node = head
        while node is not None:
            if node.child is None:
                node = node.next
                continue
            child = node.child
            node.child = None
            nxt = node.next
            node.next = child
            child.prev = node
            tail = child
            while tail.next is not None:
                tail = tail.next
            tail.next = nxt
            if nxt is not None:
                nxt.prev = tail
            node = child
        return head
