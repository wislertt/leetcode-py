from leetcode_py import ListNode


class Solution:
    # Time: O(n + m)
    # Space: O(1)
    def merge_in_between(
        self, list1: ListNode[int] | None, a: int, b: int, list2: ListNode[int] | None
    ) -> ListNode[int] | None:
        if list1 is None:
            return list2
        prev = list1
        for _ in range(a - 1):
            assert prev.next is not None
            prev = prev.next
        tail2 = list2
        while tail2 is not None and tail2.next is not None:
            tail2 = tail2.next
        after = prev
        for _ in range(b - a + 2):
            assert after.next is not None
            after = after.next
        prev.next = list2
        if tail2 is not None:
            tail2.next = after
        return list1
