from leetcode_py import TreeNode


class Solution:
    # Time: O(n * d^2) where d = distance (each leaf-depth list holds at most d entries)
    # Space: O(n)
    def count_pairs(self, root: TreeNode[int] | None, distance: int) -> int:
        total = 0

        def dfs(node: TreeNode[int] | None) -> list[int]:
            nonlocal total
            if node is None:
                return []
            if node.left is None and node.right is None:
                return [1]
            left = dfs(node.left)
            right = dfs(node.right)
            for left_depth in left:
                for right_depth in right:
                    if left_depth + right_depth <= distance:
                        total += 1
            return [depth + 1 for depth in left + right if depth + 1 < distance]

        dfs(root)
        return total
