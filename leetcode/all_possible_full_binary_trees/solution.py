from functools import cache

from leetcode_py import TreeNode


class Solution:
    # Time: O(Catalan(n/2) * n)
    # Space: O(Catalan(n/2) * n)
    def all_possible_fbt(self, n: int) -> list[TreeNode[int] | None]:
        @cache
        def build(count: int) -> list[TreeNode[int] | None]:
            if count == 1:
                return [TreeNode(0)]
            trees: list[TreeNode[int] | None] = []
            for left_count in range(1, count - 1, 2):
                for left in build(left_count):
                    for right in build(count - 1 - left_count):
                        root = TreeNode(0)
                        root.left = left
                        root.right = right
                        trees.append(root)
            return trees

        if n % 2 == 0:
            return []
        return build(n)
