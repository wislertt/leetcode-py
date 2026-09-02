from leetcode_py import ListNode


class Solution:
    # Time: O(n)
    # Space: O(1)
    def swap_nodes(self, head: ListNode[int] | None, k: int) -> ListNode[int] | None:
        if head is None:
            return head

        n = 1
        node = head
        while node.next is not None:
            node = node.next
            n += 1

        first = head
        for _ in range(k - 1):
            if first.next is None:
                break
            first = first.next

        second = head
        for _ in range(n - k):
            if second.next is None:
                break
            second = second.next

        first.val, second.val = second.val, first.val
        return head
