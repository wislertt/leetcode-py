from leetcode_py import ListNode


class Solution:
    # Time: O(n)
    # Space: O(1)
    def nodes_between_critical_points(self, head: ListNode[int] | None) -> list[int]:
        first = prev = 0
        min_gap = 10**6
        count = 0
        pos = 1
        if head is None or head.next is None or head.next.next is None:
            return [-1, -1]
        prev_val = head.val
        curr = head.next
        while curr.next is not None:
            next_val = curr.next.val
            if (curr.val > prev_val and curr.val > next_val) or (
                curr.val < prev_val and curr.val < next_val
            ):
                if count == 0:
                    first = pos
                else:
                    min_gap = min(min_gap, pos - prev)
                prev = pos
                count += 1
            prev_val = curr.val
            curr = curr.next
            pos += 1
        if count < 2:
            return [-1, -1]
        return [min_gap, prev - first]
