from leetcode_py import TreeNode


class Solution:
    # Time: O(log n) average, O(n) worst case (one node per tree level)
    # Space: O(log n) average, O(n) worst case (recursion stack)
    def split_bst(self, root: TreeNode[int] | None, target: int) -> list[TreeNode[int] | None]:
        if root is None:
            return [None, None]
        if root.val <= target:
            smaller, larger = self.split_bst(root.right, target)
            root.right = smaller
            return [root, larger]
        smaller, larger = self.split_bst(root.left, target)
        root.left = larger
        return [smaller, root]
