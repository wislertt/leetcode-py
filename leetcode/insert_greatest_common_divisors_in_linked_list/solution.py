from math import gcd

from leetcode_py import ListNode


class Solution:
    # Time: O(n)
    # Space: O(1)
    def insert_greatest_common_divisors(self, head: ListNode[int] | None) -> ListNode[int] | None:
        current = head
        while current and current.next:
            inserted = ListNode[int](gcd(current.val, current.next.val))
            inserted.next = current.next
            current.next = inserted
            current = inserted.next
        return head
