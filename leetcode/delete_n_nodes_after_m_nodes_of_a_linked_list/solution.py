from leetcode_py import ListNode


class Solution:
    # Time: O(len(head))
    # Space: O(1)
    def delete_nodes(self, head: ListNode[int] | None, m: int, n: int) -> ListNode[int] | None:
        pre = head
        while pre:
            for _ in range(m - 1):
                if pre.next:
                    pre = pre.next
            cur = pre
            for _ in range(n):
                if cur.next:
                    cur = cur.next
            pre.next = cur.next
            pre = pre.next
        return head
