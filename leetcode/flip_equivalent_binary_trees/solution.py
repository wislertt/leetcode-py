from leetcode_py import TreeNode


class Solution:
    # Time: O(n)
    # Space: O(h) where h is the tree height
    def flip_equiv(self, root1: TreeNode[int] | None, root2: TreeNode[int] | None) -> bool:
        if root1 is None or root2 is None:
            return root1 is root2
        if root1.val != root2.val:
            return False
        no_flip = self.flip_equiv(root1.left, root2.left) and self.flip_equiv(
            root1.right, root2.right
        )
        flip = self.flip_equiv(root1.left, root2.right) and self.flip_equiv(root1.right, root2.left)
        return no_flip or flip
