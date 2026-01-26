from leetcode_py import ListNode


class Solution:
    # Time: O(n)
    # Space: O(1)
    def detect_cycle(self, head: ListNode[int] | None) -> ListNode[int] | None:
        if not head:
            return None

        slow: ListNode[int] | None = head
        fast: ListNode[int] | None = head

        # Phase 1: Detect if cycle exists using Floyd's algorithm
        has_cycle = False
        while fast and fast.next:
            assert slow is not None
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                has_cycle = True
                break

        if not has_cycle:
            return None

        # Phase 2: Find the start of the cycle
        slow = head
        assert fast is not None  # fast is guaranteed to be a valid node here
        while slow is not fast:
            assert slow is not None
            slow = slow.next
            assert fast.next is not None
            fast = fast.next

        return slow
