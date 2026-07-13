from leetcode_py import TreeNode


class Solution:
    # Time: O(n) — visits each node once in post-order
    # Space: O(h) recursion stack, h = tree height
    def remove_leaf_nodes(self, root: TreeNode[int] | None, target: int) -> TreeNode[int] | None:
        if root is None:
            return None

        root.left = self.remove_leaf_nodes(root.left, target)
        root.right = self.remove_leaf_nodes(root.right, target)

        # Post-order: decide after children are pruned, so a node whose children
        # were just removed can itself qualify as a target leaf.
        if root.left is None and root.right is None and root.val == target:
            return None
        return root
