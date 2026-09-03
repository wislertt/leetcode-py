from leetcode_py import TreeNode


class Solution:
    # Time: O(h) where h is the tree height
    # Space: O(1)
    def search_bst(self, root: TreeNode[int] | None, val: int) -> TreeNode[int] | None:
        node = root
        while node is not None:
            if val == node.val:
                return node
            node = node.left if val < node.val else node.right
        return None
