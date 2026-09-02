from leetcode_py import TreeNode


class Solution:
    # Time: O(n * d) where d is the average path length
    # Space: O(h) for the recursion stack, excluding the output
    def binary_tree_paths(self, root: TreeNode[int] | None) -> list[str]:
        paths: list[str] = []

        def dfs(node: TreeNode[int] | None, path: list[str]) -> None:
            if node is None:
                return
            path.append(str(node.val))
            if node.left is None and node.right is None:
                paths.append("->".join(path))
            else:
                dfs(node.left, path)
                dfs(node.right, path)
            path.pop()

        dfs(root, [])
        return paths
