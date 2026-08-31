from leetcode_py import ListNode


class Solution:
    # Time: O(n)
    # Space: O(1)
    def remove_linked_list_elements(
        self, head: ListNode[int] | None, val: int
    ) -> ListNode[int] | None:
        dummy = ListNode[int](0)
        dummy.next = head
        current = dummy
        while current.next is not None:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        return dummy.next
