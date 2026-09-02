from __future__ import annotations


class Node:
    def __init__(self, val: int = 0, next: Node | None = None) -> None:
        self.val = val
        self.next: Node = next if next is not None else self


class Solution:
    # Time: O(n)
    # Space: O(1)
    def insert(self, head: Node | None, insert_val: int) -> Node:
        node = Node(insert_val)
        if head is None:
            return node
        prev, curr = head, head.next
        while curr is not head:
            if prev.val <= insert_val <= curr.val or (
                prev.val > curr.val and (insert_val >= prev.val or insert_val <= curr.val)
            ):
                break
            prev, curr = curr, curr.next
        prev.next = node
        node.next = curr
        return head
