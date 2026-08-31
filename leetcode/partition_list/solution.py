from leetcode_py import ListNode


class Solution:
    # Time: O(n)
    # Space: O(1)
    def partition(self, head: ListNode[int] | None, x: int) -> ListNode[int] | None:
        before_head = before = ListNode[int](0)
        after_head = after = ListNode[int](0)
        current = head
        while current:
            if current.val < x:
                before.next = current
                before = before.next
            else:
                after.next = current
                after = after.next
            current = current.next
        after.next = None
        before.next = after_head.next
        return before_head.next
