from leetcode_py import ListNode


class Solution:
    # Time: O(n)
    # Space: O(1)
    def remove_nodes(self, head: ListNode[int] | None) -> ListNode[int] | None:
        # Reverse the list so that "greater to the right" becomes "greater already kept".
        prev: ListNode[int] | None = None
        node = head
        while node is not None:
            nxt = node.next
            node.next = prev
            prev = node
            node = nxt

        cur = prev
        while cur is not None:
            nxt = cur.next
            if nxt is None:
                break
            if nxt.val < cur.val:
                cur.next = nxt.next
            else:
                cur = nxt

        # Reverse back to restore left-to-right order.
        result: ListNode[int] | None = None
        node = prev
        while node is not None:
            nxt = node.next
            node.next = result
            result = node
            node = nxt
        return result
