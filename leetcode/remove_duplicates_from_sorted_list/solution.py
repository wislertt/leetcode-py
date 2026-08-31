from leetcode_py import ListNode


class Solution:
    # Time: O(n)
    # Space: O(1)
    def delete_duplicates(self, head: ListNode[int] | None) -> ListNode[int] | None:
        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head
