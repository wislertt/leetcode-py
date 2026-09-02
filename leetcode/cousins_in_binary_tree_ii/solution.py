from collections import deque

from leetcode_py import TreeNode


class Solution:
    # Time: O(n)
    # Space: O(n)
    def replace_value_in_tree(self, root: TreeNode[int] | None) -> TreeNode[int] | None:
        if root is None:
            return None

        queue: deque[TreeNode[int]] = deque([root])
        root.val = 0

        while queue:
            next_sum = 0
            for node in queue:
                for child in (node.left, node.right):
                    if child is not None:
                        next_sum += child.val

            for _ in range(len(queue)):
                node = queue.popleft()
                left, right = node.left, node.right
                child_sum = 0
                if left is not None:
                    child_sum += left.val
                if right is not None:
                    child_sum += right.val
                for child in (left, right):
                    if child is not None:
                        child.val = next_sum - child_sum
                        queue.append(child)

        return root
