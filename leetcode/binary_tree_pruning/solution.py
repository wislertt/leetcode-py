from leetcode_py import TreeNode


class Solution:
    # Time: O(n)
    # Space: O(h)
    def prune_tree(self, root: TreeNode[int] | None) -> TreeNode[int] | None:
        if root is None:
            return None
        root.left = self.prune_tree(root.left)
        root.right = self.prune_tree(root.right)
        if root.val == 0 and root.left is None and root.right is None:
            return None
        return root
