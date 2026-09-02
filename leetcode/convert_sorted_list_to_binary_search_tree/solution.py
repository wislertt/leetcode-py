from leetcode_py import ListNode, TreeNode


class Solution:
    # Time: O(n) - each list node is visited once, in the same order the
    # in-order traversal consumes them.
    # Space: O(log n) - recursion depth equals the tree height.
    def sorted_list_to_bst(self, head: ListNode[int] | None) -> TreeNode[int] | None:
        size = 0
        node = head
        while node is not None:
            size += 1
            node = node.next

        cursor = head

        def build(lo: int, hi: int) -> TreeNode[int] | None:
            nonlocal cursor
            if lo > hi:
                return None
            mid = (lo + hi) // 2
            left = build(lo, mid - 1)
            cur = cursor
            assert cur is not None
            cursor = cur.next
            return TreeNode(cur.val, left, build(mid + 1, hi))

        return build(0, size - 1)
