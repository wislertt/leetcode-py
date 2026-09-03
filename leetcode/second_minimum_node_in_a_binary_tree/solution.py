from leetcode_py import TreeNode


class Solution:
    # Time: O(n)
    # Space: O(h)
    def find_second_minimum_value(self, root: TreeNode[int] | None) -> int:
        if root is None:
            return -1
        return self._dfs(root, root.val)

    def _dfs(self, node: TreeNode[int] | None, smallest: int) -> int:
        if node is None:
            return -1
        if node.val > smallest:
            return node.val
        left = self._dfs(node.left, smallest)
        right = self._dfs(node.right, smallest)
        if left == -1:
            return right
        if right == -1:
            return left
        return min(left, right)
