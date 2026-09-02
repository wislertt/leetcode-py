from leetcode_py import ListNode


class Solution:
    # Time: O(n) where n is the number of nodes in the input list
    # Space: O(1), nodes are merged in place
    def merge_nodes(self, head: ListNode[int] | None) -> ListNode[int] | None:
        if head is None:
            return None
        tail = head
        node = head.next
        total = 0
        first = True
        while node is not None:
            if node.val == 0:
                if first:
                    head.val = total
                    first = False
                else:
                    nxt = tail.next
                    assert nxt is not None
                    nxt.val = total
                    tail = nxt
                total = 0
            else:
                total += node.val
            node = node.next
        tail.next = None
        return head
