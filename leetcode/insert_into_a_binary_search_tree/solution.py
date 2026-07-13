from leetcode_py import TreeNode


class Solution:
    # Time: O(h)
    # Space: O(1)
    def insert_into_bst(self, root: TreeNode[int] | None, val: int) -> TreeNode[int] | None:
        node = TreeNode(val)
        if root is None:
            return node

        current = root
        while True:
            if val < current.val:
                if current.left is None:
                    current.left = node
                    return root
                current = current.left
            else:
                if current.right is None:
                    current.right = node
                    return root
                current = current.right
