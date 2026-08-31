from leetcode_py import TreeNode


class Solution:
    # Time: O(n) where n is the smaller tree's node count
    # Space: O(h)
    def merge_trees(
        self, root1: TreeNode[int] | None, root2: TreeNode[int] | None
    ) -> TreeNode[int] | None:
        if root1 is None:
            return root2
        if root2 is None:
            return root1
        root1.val += root2.val
        root1.left = self.merge_trees(root1.left, root2.left)
        root1.right = self.merge_trees(root1.right, root2.right)
        return root1
