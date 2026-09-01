from collections import deque

from leetcode_py import TreeNode


class Solution:
    # Time: O(n)
    # Space: O(w) for the level queue, w = 2^depth at the deepest level
    def reverse_odd_levels(self, root: TreeNode[int] | None) -> TreeNode[int] | None:
        if root is None:
            return None
        queue: deque[TreeNode[int]] = deque([root])
        depth = 0
        while queue:
            level = list(queue)
            if depth % 2 == 1:
                left = 0
                right = len(level) - 1
                while left < right:
                    level[left].val, level[right].val = level[right].val, level[left].val
                    left += 1
                    right -= 1
            queue = deque(
                child for node in level for child in (node.left, node.right) if child is not None
            )
            depth += 1
        return root
