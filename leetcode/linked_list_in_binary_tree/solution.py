from leetcode_py import ListNode, TreeNode


class Solution:
    # Time: O(n * m) worst case (n tree nodes, m list length)
    # Space: O(h) recursion depth
    def is_sub_path(self, head: ListNode[int] | None, root: TreeNode[int] | None) -> bool:
        if root is None:
            return False

        def match(node: TreeNode[int] | None, cur: ListNode[int] | None) -> bool:
            if cur is None:
                return True
            if node is None or node.val != cur.val:
                return False
            return match(node.left, cur.next) or match(node.right, cur.next)

        def dfs(node: TreeNode[int] | None) -> bool:
            if node is None:
                return False
            return match(node, head) or dfs(node.left) or dfs(node.right)

        return dfs(root)
