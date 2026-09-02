from leetcode_py import ListNode


class Solution:
    # Time: O(1)
    # Space: O(1)
    def delete_node(self, node: ListNode[int]) -> None:
        # Given node is never the tail, so copy the successor into it and skip it
        nxt = node.next
        if nxt is None:
            return
        node.val = nxt.val
        node.next = nxt.next
