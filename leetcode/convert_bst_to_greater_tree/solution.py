from leetcode_py import TreeNode


class Solution:
    # Time: O(n)
    # Space: O(h) recursion stack
    def convert_bst(self, root: TreeNode[int] | None) -> TreeNode[int] | None:
        def reverse_inorder(node: TreeNode[int] | None) -> None:
            nonlocal total
            if node is None:
                return
            reverse_inorder(node.right)
            total += node.val
            node.val = total
            reverse_inorder(node.left)

        total = 0
        reverse_inorder(root)
        return root
