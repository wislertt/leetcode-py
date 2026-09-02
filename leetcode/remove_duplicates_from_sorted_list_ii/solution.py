from leetcode_py import ListNode


class Solution:
    # Time: O(n)
    # Space: O(1)
    def delete_duplicates(self, head: ListNode[int] | None) -> ListNode[int] | None:
        dummy: ListNode[int] = ListNode(0)
        dummy.next = head
        prev = dummy

        while head is not None:
            if head.next is not None and head.val == head.next.val:
                dup = head.val
                while head is not None and head.val == dup:
                    head = head.next
                prev.next = head
            else:
                prev = head
                head = head.next

        return dummy.next
