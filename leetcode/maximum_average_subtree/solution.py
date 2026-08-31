from leetcode_py import TreeNode


class Solution:
    # Time: O(n)
    # Space: O(h) for the recursion stack
    def maximum_average_subtree(self, root: TreeNode[int] | None) -> float:
        ans = 0.0

        def dfs(node: TreeNode[int] | None) -> tuple[int, int]:
            nonlocal ans
            if node is None:
                return 0, 0
            left_sum, left_n = dfs(node.left)
            right_sum, right_n = dfs(node.right)
            total = node.val + left_sum + right_sum
            count = 1 + left_n + right_n
            ans = max(ans, total / count)
            return total, count

        dfs(root)
        return ans
