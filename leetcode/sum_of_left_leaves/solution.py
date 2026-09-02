from leetcode_py import TreeNode


class Solution:
    # Time: O(n)
    # Space: O(h)
    def sum_of_left_leaves(self, root: TreeNode[int] | None) -> int:
        if root is None:
            return 0
        if root.left is not None and root.left.left is None and root.left.right is None:
            return root.left.val + self.sum_of_left_leaves(root.right)
        return self.sum_of_left_leaves(root.left) + self.sum_of_left_leaves(root.right)
