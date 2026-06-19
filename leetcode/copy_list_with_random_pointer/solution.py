from __future__ import annotations


class Node:
    def __init__(self, x: int, next: Node | None = None, random: Node | None = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    # Time: O(n)
    # Space: O(1) extra (interweaves clones into the original list)
    def copy_random_list(self, head: Node | None) -> Node | None:
        if head is None:
            return None

        # Phase 1: insert each clone right after its original node
        current: Node | None = head
        while current is not None:
            nxt = current.next
            clone = Node(current.val, nxt)
            current.next = clone
            current = nxt

        # Phase 2: wire each clone's random from its original's random
        current = head
        while current is not None:
            clone = current.next
            assert clone is not None
            if current.random is not None:
                rand_clone = current.random.next
                assert rand_clone is not None
                clone.random = rand_clone
            current = clone.next

        # Phase 3: detach clones, restore the original, return the copy head
        current = head
        copy_head = head.next
        while current is not None:
            clone = current.next
            assert clone is not None
            current.next = clone.next
            tail = clone.next
            clone.next = tail.next if tail is not None else None
            current = current.next

        return copy_head
