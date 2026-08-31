from leetcode_py import TreeNode


class Solution:
    # Time: O(n)
    # Space: O(n)
    def distribute_coins(self, root: TreeNode[int] | None) -> int:
        moves = 0

        def dfs(node: TreeNode[int] | None) -> int:
            nonlocal moves
            if node is None:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            moves += abs(left) + abs(right)
            return node.val + left + right - 1

        dfs(root)
        return moves
