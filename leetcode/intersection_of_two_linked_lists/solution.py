from leetcode_py import ListNode


class Solution:
    # Time: O(m + n)
    # Space: O(1)
    def get_intersection_node(
        self, head_a: ListNode[int] | None, head_b: ListNode[int] | None
    ) -> ListNode[int] | None:
        pointer_a: ListNode[int] | None = head_a
        pointer_b: ListNode[int] | None = head_b
        while pointer_a is not pointer_b:
            pointer_a = pointer_a.next if pointer_a is not None else head_b
            pointer_b = pointer_b.next if pointer_b is not None else head_a
        return pointer_a
