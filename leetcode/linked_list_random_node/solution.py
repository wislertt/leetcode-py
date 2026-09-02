import random

from leetcode_py import ListNode


class Solution:
    # Time: init O(1), get_random O(n)
    # Space: O(1)
    def __init__(self, head: ListNode[int] | None) -> None:
        self.head = head

    def get_random(self) -> int:
        node = self.head
        assert node is not None
        reservoir = node.val
        current = node.next
        seen = 2
        while current is not None:
            if random.randint(1, seen) == 1:
                reservoir = current.val
            current = current.next
            seen += 1
        return reservoir
