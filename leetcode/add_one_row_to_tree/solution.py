from collections import deque

from leetcode_py import TreeNode


class Solution:
    # Time: O(n)
    # Space: O(w) where w is the maximum width of the tree
    def add_one_row(self, root: TreeNode[int] | None, val: int, depth: int) -> TreeNode[int] | None:
        if depth == 1:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root

        queue: deque[TreeNode[int]] = deque()
        if root is not None:
            queue.append(root)

        current_depth = 1
        while queue and current_depth < depth - 1:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            current_depth += 1

        for parent in queue:
            left = TreeNode(val)
            left.left = parent.left
            parent.left = left

            right = TreeNode(val)
            right.right = parent.right
            parent.right = right

        return root
