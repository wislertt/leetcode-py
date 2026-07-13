from leetcode_py import ListNode


class Solution:
    # Time: O(n) — single pass to close ring then cut
    # Space: O(1)
    def rotate_right(self, head: ListNode[int] | None, k: int) -> ListNode[int] | None:
        if not head or not head.next or k == 0:
            return head

        # Count length and close the list into a ring
        tail = head
        length = 1
        while tail.next:
            tail = tail.next
            length += 1
        tail.next = head

        # Effective rotations; new tail is at (length - k % length) steps from head
        k %= length
        steps_to_new_tail = length - k
        new_tail = head
        for _ in range(steps_to_new_tail - 1):
            assert new_tail.next is not None
            new_tail = new_tail.next
        assert new_tail.next is not None
        new_head = new_tail.next
        new_tail.next = None
        return new_head
