from leetcode_py import TreeNode


class Solution:
    # Time: O(n)
    # Space: O(h) where h is the tree height
    def range_sum_bst(self, root: TreeNode[int] | None, low: int, high: int) -> int:
        if root is None:
            return 0
        if root.val < low:
            # Entire left subtree is below the range
            return self.range_sum_bst(root.right, low, high)
        if root.val > high:
            # Entire right subtree is above the range
            return self.range_sum_bst(root.left, low, high)
        return (
            root.val
            + self.range_sum_bst(root.left, low, high)
            + self.range_sum_bst(root.right, low, high)
        )
