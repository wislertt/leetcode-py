from leetcode_py import TreeNode


class Solution:
    # Time: O(n)
    # Space: O(h) recursion stack
    def tree_to_doubly_list(self, root: TreeNode[int] | None) -> TreeNode[int] | None:
        if root is None:
            return None
        first: TreeNode[int] | None = None
        last: TreeNode[int] | None = None

        def link(node: TreeNode[int]) -> None:
            nonlocal first, last
            if last is not None:
                last.right = node
                node.left = last
            else:
                first = node
            last = node

        def dfs(node: TreeNode[int] | None) -> None:
            if node is None:
                return
            dfs(node.left)
            link(node)
            dfs(node.right)

        dfs(root)
        assert last is not None and first is not None
        last.right = first
        first.left = last
        return first
