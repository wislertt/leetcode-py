from leetcode_py import TreeNode


class Solution:
    # Time: O(n)
    # Space: O(n)
    def find_target(self, root: TreeNode[int] | None, k: int) -> bool:
        seen: set[int] = set()

        def dfs(node: TreeNode[int] | None) -> bool:
            if node is None:
                return False
            if k - node.val in seen:
                return True
            seen.add(node.val)
            return dfs(node.left) or dfs(node.right)

        return dfs(root)
