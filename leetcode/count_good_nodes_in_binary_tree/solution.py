from leetcode_py import TreeNode


class Solution:
    # Time: O(n)
    # Space: O(h) - recursion stack, h = tree height
    def good_nodes(self, root: TreeNode[int] | None) -> int:
        if root is None:
            return 0

        def dfs(node: TreeNode[int], max_so_far: int) -> int:
            good = 1 if node.val >= max_so_far else 0
            next_max = max(max_so_far, node.val)
            total = good
            if node.left is not None:
                total += dfs(node.left, next_max)
            if node.right is not None:
                total += dfs(node.right, next_max)
            return total

        return dfs(root, root.val)
