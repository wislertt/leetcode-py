from leetcode_py import ListNode


class Solution:
    # Time: O(n) — find middle, reverse second half, walk pairs
    # Space: O(1) — in-place pointer reversal
    def pair_sum(self, head: ListNode[int] | None) -> int:
        # Slow/fast pointers: slow lands on the start of the second half
        slow: ListNode[int] | None = head
        fast: ListNode[int] | None = head
        while fast and fast.next:
            assert slow is not None
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half in place
        prev: ListNode[int] | None = None
        current: ListNode[int] | None = slow
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt

        # Walk both halves from the ends inward
        best = 0
        first: ListNode[int] | None = head
        second: ListNode[int] | None = prev
        while second:
            assert first is not None
            best = max(best, first.val + second.val)
            first = first.next
            second = second.next
        return best
