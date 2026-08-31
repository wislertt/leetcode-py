from collections import deque

from leetcode_py import TreeNode


class Solution:
    # Time: O(n)
    # Space: O(n)
    def is_complete_tree(self, root: TreeNode[int] | None) -> bool:
        if root is None:
            return True
        queue: deque[TreeNode[int] | None] = deque([root])
        seen_hole = False
        while queue:
            node = queue.popleft()
            if node is None:
                seen_hole = True
                continue
            if seen_hole:
                # A node appeared after a gap: not complete
                return False
            queue.append(node.left)
            queue.append(node.right)
        return True
