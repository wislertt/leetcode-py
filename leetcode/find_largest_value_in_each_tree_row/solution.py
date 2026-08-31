from collections import deque

from leetcode_py import TreeNode


class Solution:
    # Time: O(n)
    # Space: O(n)
    def largest_values(self, root: TreeNode[int] | None) -> list[int]:
        if root is None:
            return []

        result: list[int] = []
        queue: deque[TreeNode[int]] = deque([root])
        while queue:
            result.append(max(node.val for node in queue))
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result
