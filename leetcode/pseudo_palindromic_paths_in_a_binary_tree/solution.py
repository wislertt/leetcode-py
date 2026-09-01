from leetcode_py import TreeNode


class Solution:
    # Time: O(n)
    # Space: O(h)
    def pseudo_palindromic_paths(self, root: TreeNode[int] | None) -> int:
        if root is None:
            return 0
        total = 0
        stack: list[tuple[TreeNode[int], int]] = [(root, 1 << root.val)]
        while stack:
            node, mask = stack.pop()
            if node.left is None and node.right is None:
                if mask & (mask - 1) == 0:
                    total += 1
                continue
            if node.left is not None:
                stack.append((node.left, mask ^ (1 << node.left.val)))
            if node.right is not None:
                stack.append((node.right, mask ^ (1 << node.right.val)))
        return total
