from leetcode_py import TreeNode


class Solution:
    # Time: O(h) where h is the height of the tree
    # Space: O(h) recursion stack
    def delete_node(self, root: TreeNode[int] | None, key: int) -> TreeNode[int] | None:
        if root is None:
            return None

        if key < root.val:
            root.left = self.delete_node(root.left, key)
        elif key > root.val:
            root.right = self.delete_node(root.right, key)
        else:
            # Node found: handle deletion by child count.
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            # Two children: replace value with inorder successor, delete successor.
            successor = root.right
            while successor.left is not None:
                successor = successor.left
            root.val = successor.val
            root.right = self.delete_node(root.right, successor.val)
        return root
