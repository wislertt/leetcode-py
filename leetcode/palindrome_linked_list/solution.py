from leetcode_py import ListNode


class Solution:
    # Time: O(n) — find middle, reverse half, compare
    # Space: O(1) — in-place pointers
    def is_palindrome(self, head: ListNode[int] | None) -> bool:
        if not head or not head.next:
            return True

        # Slow/fast to reach the middle (slow lands on start of second half)
        slow: ListNode[int] | None = head
        fast: ListNode[int] | None = head
        while fast and fast.next:
            assert slow is not None
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half
        second_head = self._reverse(slow)

        # Compare both halves
        first: ListNode[int] | None = head
        second: ListNode[int] | None = second_head
        result = True
        while second:
            assert first is not None
            if first.val != second.val:
                result = False
                break
            first = first.next
            second = second.next
        return result

    @staticmethod
    def _reverse(head: ListNode[int] | None) -> ListNode[int] | None:
        prev: ListNode[int] | None = None
        current = head
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        return prev
