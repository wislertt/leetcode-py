from leetcode_py import TreeNode


class Solution:
    # Time: O(h)
    # Space: O(1)
    def inorder_successor(
        self, root: TreeNode[int] | None, p: TreeNode[int]
    ) -> TreeNode[int] | None:
        # If p has a right subtree, successor is leftmost node of that subtree.
        # Otherwise, successor is the lowest ancestor for which p lies in its
        # left subtree. Track candidate successor while walking down.
        successor = None
        while root:
            if p.val < root.val:
                successor = root
                root = root.left
            else:
                root = root.right
        return successor
