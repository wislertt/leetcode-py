from collections import deque

from leetcode_py import TreeNode


class Solution:
    # Time: O(n)
    # Space: O(w) where w is the maximum width of the tree
    def min_depth(self, root: TreeNode[int] | None) -> int:
        if root is None:
            return 0
        queue: deque[TreeNode[int]] = deque([root])
        depth = 1
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left is None and node.right is None:
                    return depth
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            depth += 1
        return depth
