from leetcode_py import ListNode


class Solution:
    # Time: O(n^2)
    # Space: O(1)
    def insertion_sort_list(self, head: ListNode[int] | None) -> ListNode[int] | None:
        dummy = ListNode[int](0)
        dummy.next = head
        current = head
        while current is not None and current.next is not None:
            next_node = current.next
            if current.val <= next_node.val:
                current = current.next
                continue
            current.next = next_node.next
            prev = dummy
            while prev.next is not None and prev.next.val < next_node.val:
                prev = prev.next
            next_node.next = prev.next
            prev.next = next_node
        return dummy.next
