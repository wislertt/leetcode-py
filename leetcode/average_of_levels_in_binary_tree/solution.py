from collections import deque

from leetcode_py import TreeNode


class Solution:
    # Time: O(n)
    # Space: O(w) where w is the maximum width of the tree
    def average_of_levels(self, root: TreeNode[int] | None) -> list[float]:
        if root is None:
            return []
        result: list[float] = []
        queue = deque([root])
        while queue:
            level_size = len(queue)
            level_sum = 0
            for _ in range(level_size):
                node = queue.popleft()
                level_sum += node.val
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            result.append(level_sum / level_size)
        return result
