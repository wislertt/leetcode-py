from collections import deque

from leetcode_py import TreeNode


class Solution:
    # Time: O(n) — each node processed once
    # Space: O(n) — queue holds widest level
    def zigzag_level_order(self, root: TreeNode[int] | None) -> list[list[int]]:
        if not root:
            return []

        result: list[list[int]] = []
        queue: deque[TreeNode[int]] = deque([root])
        left_to_right = True

        while queue:
            level: deque[int] = deque()
            for _ in range(len(queue)):
                node = queue.popleft()
                if left_to_right:
                    level.append(node.val)
                else:
                    level.appendleft(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(list(level))
            left_to_right = not left_to_right

        return result
