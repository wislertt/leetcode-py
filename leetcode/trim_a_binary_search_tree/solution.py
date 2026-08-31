from leetcode_py import TreeNode


class Solution:
    # Time: O(n)
    # Space: O(h)
    def trim_bst(self, root: TreeNode[int] | None, low: int, high: int) -> TreeNode[int] | None:
        if root is None:
            return None
        if root.val < low:
            return self.trim_bst(root.right, low, high)
        if root.val > high:
            return self.trim_bst(root.left, low, high)
        root.left = self.trim_bst(root.left, low, high)
        root.right = self.trim_bst(root.right, low, high)
        return root
