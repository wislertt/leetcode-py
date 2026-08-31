from collections import deque

from leetcode_py import TreeNode


class Solution:
    # Time: O(n)
    # Space: O(n)
    def find_bottom_left_value(self, root: TreeNode[int]) -> int:
        queue: deque[TreeNode[int]] = deque([root])
        leftmost = root.val
        while queue:
            leftmost = queue[0].val
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return leftmost
