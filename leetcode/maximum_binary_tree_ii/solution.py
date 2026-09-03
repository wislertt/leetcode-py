from leetcode_py import TreeNode


class Solution:
    # Time: O(h) where h is the tree height, O(n) worst case
    # Space: O(h) recursion stack, O(n) worst case
    def insert_into_max_tree(self, root: TreeNode[int] | None, val: int) -> TreeNode[int] | None:
        if root is None or val > root.val:
            return TreeNode(val, root, None)
        root.right = self.insert_into_max_tree(root.right, val)
        return root
