from leetcode_py import ListNode


class Solution:
    # Time: O(n log n) — bottom-up merge sort, log n passes each O(n)
    # Space: O(1) — iterative, pointers only
    def sort_list(self, head: ListNode[int] | None) -> ListNode[int] | None:
        if not head or not head.next:
            return head

        # Find length
        length = 0
        node = head
        while node:
            length += 1
            node = node.next

        dummy: ListNode[int] = ListNode[int](0)
        dummy.next = head
        size = 1
        while size < length:
            curr = dummy.next
            tail = dummy
            while curr:
                left = curr
                right = self._split(left, size)
                curr = self._split(right, size) if right else None
                tail = self._merge(left, right, tail)
            size *= 2
        return dummy.next

    @staticmethod
    def _split(head: ListNode[int] | None, size: int) -> ListNode[int] | None:
        """Cut after `size` nodes; return the head of the second half."""
        for _ in range(size - 1):
            if head is None or head.next is None:
                break
            head = head.next
        if head is None:
            return None
        nxt = head.next
        head.next = None
        return nxt

    @staticmethod
    def _merge(
        left: ListNode[int] | None, right: ListNode[int] | None, tail: ListNode[int]
    ) -> ListNode[int]:
        """Merge two sorted lists onto tail; return the new tail."""
        while left and right:
            if left.val <= right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next
        tail.next = left if left else right
        while tail.next:
            assert tail.next is not None
            tail = tail.next
        return tail
