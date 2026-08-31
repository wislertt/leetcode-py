from leetcode_py import TreeNode


class Solution:
    # Time: O(n^2) worst case for string building on a skewed tree
    # Space: O(n)
    def smallest_from_leaf(self, root: TreeNode[int] | None) -> str:
        best = ""

        def dfs(node: TreeNode[int] | None, path: str) -> None:
            nonlocal best
            if node is None:
                return
            path = chr(ord("a") + node.val) + path
            if node.left is None and node.right is None:
                if not best or path < best:
                    best = path
                return
            dfs(node.left, path)
            dfs(node.right, path)

        dfs(root, "")
        return best
