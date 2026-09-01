from leetcode_py import TreeNode


class Solution:
    # Time: O(n)
    # Space: O(h)
    def evaluate_tree(self, root: TreeNode[int] | None) -> bool:
        if root is None:
            return False
        if root.left is None and root.right is None:
            return root.val == 1
        left = self.evaluate_tree(root.left)
        right = self.evaluate_tree(root.right)
        return (left or right) if root.val == 2 else (left and right)
