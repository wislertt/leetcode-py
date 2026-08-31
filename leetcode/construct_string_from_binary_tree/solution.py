from leetcode_py import TreeNode


class Solution:
    # Time: O(n)
    # Space: O(n)
    def tree2str(self, root: TreeNode[int] | None) -> str:
        if root is None:
            return ""
        left = self.tree2str(root.left)
        right = self.tree2str(root.right)
        if root.left is None and root.right is not None:
            return f"{root.val}()({right})"
        if root.right is not None:
            return f"{root.val}({left})({right})"
        if root.left is not None:
            return f"{root.val}({left})"
        return str(root.val)
