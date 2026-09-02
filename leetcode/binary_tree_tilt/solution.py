from leetcode_py import TreeNode


class Solution:
    # Time: O(n)
    # Space: O(h) for the recursion stack
    def find_tilt(self, root: TreeNode[int] | None) -> int:
        total = 0

        def dfs(node: TreeNode[int] | None) -> int:
            nonlocal total
            if node is None:
                return 0
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)
            total += abs(left_sum - right_sum)
            return left_sum + right_sum + node.val

        dfs(root)
        return total
