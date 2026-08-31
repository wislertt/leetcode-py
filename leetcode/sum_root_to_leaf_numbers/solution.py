from leetcode_py import TreeNode


class Solution:
    # Time: O(n)
    # Space: O(h)
    def sum_numbers(self, root: TreeNode[int] | None) -> int:
        def dfs(node: TreeNode[int] | None, path_value: int) -> int:
            if node is None:
                return 0
            path_value = path_value * 10 + node.val
            if node.left is None and node.right is None:
                return path_value
            return dfs(node.left, path_value) + dfs(node.right, path_value)

        return dfs(root, 0)
