from leetcode_py import TreeNode


class Solution:
    # Time: O(n) — each node visited once
    # Space: O(h) — recursion depth equals tree height
    def longest_consecutive(self, root: TreeNode[int] | None) -> int:
        def dfs(node: TreeNode[int] | None, parent_val: int | None, length: int) -> int:
            if node is None:
                return length
            length = length + 1 if parent_val is not None and node.val - parent_val == 1 else 1
            return max(
                length,
                dfs(node.left, node.val, length),
                dfs(node.right, node.val, length),
            )

        return dfs(root, None, 0)
