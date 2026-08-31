from leetcode_py import TreeNode


class Solution:
    # Time: O(n)
    # Space: O(h)
    def has_path_sum(self, root: TreeNode[int] | None, target_sum: int) -> bool:
        if root is None:
            return False
        remaining = target_sum - root.val
        if root.left is None and root.right is None:
            return remaining == 0
        return self.has_path_sum(root.left, remaining) or self.has_path_sum(root.right, remaining)
