from leetcode_py import TreeNode


class Solution:
    # Time: O(n) — each node visited once
    # Space: O(h) recursion stack, h = tree height
    def is_symmetric(self, root: TreeNode[int] | None) -> bool:
        def mirror(a: TreeNode[int] | None, b: TreeNode[int] | None) -> bool:
            if a is None or b is None:
                return a is b
            return a.val == b.val and mirror(a.left, b.right) and mirror(a.right, b.left)

        return mirror(root.left, root.right) if root else True
