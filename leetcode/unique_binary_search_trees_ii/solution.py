from leetcode_py import TreeNode


class Solution:
    # Time: O(4^n / sqrt(n) * n)
    # Space: O(4^n / sqrt(n) * n)
    def generate_trees(self, n: int) -> list[TreeNode[int] | None]:
        def build(start: int, end: int) -> list[TreeNode[int] | None]:
            if start > end:
                return [None]
            trees: list[TreeNode[int] | None] = []
            for root_val in range(start, end + 1):
                for left in build(start, root_val - 1):
                    for right in build(root_val + 1, end):
                        root = TreeNode[int](root_val)
                        root.left = left
                        root.right = right
                        trees.append(root)
            return trees

        return build(1, n)
