from leetcode_py import TreeNode


class Solution:
    # Time: O(n)
    # Space: O(h)
    def rob(self, root: TreeNode[int] | None) -> int:
        def dfs(node: TreeNode[int] | None) -> tuple[int, int]:
            # Returns (max if rob node, max if skip node).
            if node is None:
                return 0, 0
            left_rob, left_skip = dfs(node.left)
            right_rob, right_skip = dfs(node.right)
            rob = node.val + left_skip + right_skip
            skip = max(left_rob, left_skip) + max(right_rob, right_skip)
            return rob, skip

        return max(dfs(root))
