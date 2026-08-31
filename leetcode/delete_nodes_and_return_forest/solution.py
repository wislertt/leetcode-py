from leetcode_py import TreeNode


class Solution:
    # Time: O(n)
    # Space: O(n)
    def del_nodes(self, root: TreeNode[int] | None, to_delete: list[int]) -> list[TreeNode[int]]:
        delete = set(to_delete)
        forest: list[TreeNode[int]] = []

        def dfs(node: TreeNode[int] | None, is_root: bool) -> TreeNode[int] | None:
            if node is None:
                return None
            deleted = node.val in delete
            if is_root and not deleted:
                forest.append(node)
            node.left = dfs(node.left, deleted)
            node.right = dfs(node.right, deleted)
            return None if deleted else node

        dfs(root, True)
        return forest
