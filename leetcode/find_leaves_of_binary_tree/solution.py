from leetcode_py import TreeNode


class Solution:
    # Time: O(n) — every node visited once
    # Space: O(h) — recursion depth equals tree height
    def find_leaves(self, root: TreeNode[int] | None) -> list[list[int]]:
        result: list[list[int]] = []

        def height(node: TreeNode[int] | None) -> int:
            if node is None:
                return 0
            h = 1 + max(height(node.left), height(node.right))
            while len(result) < h:
                result.append([])
            result[h - 1].append(node.val)
            return h

        height(root)
        return result
