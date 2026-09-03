from leetcode_py import TreeNode


class Solution:
    # Time: O(n) single DFS over all nodes
    # Space: O(h) recursion stack, h = tree height
    def subtree_with_all_deepest(self, root: TreeNode[int] | None) -> TreeNode[int] | None:
        if root is None:
            return None

        def dfs(node: TreeNode[int]) -> tuple[int, TreeNode[int]]:
            left = dfs(node.left) if node.left else (0, node)
            right = dfs(node.right) if node.right else (0, node)
            if left[0] > right[0]:
                return left[0] + 1, left[1]
            if left[0] < right[0]:
                return right[0] + 1, right[1]
            return left[0] + 1, node

        return dfs(root)[1]
