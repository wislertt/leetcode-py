from collections import deque

from leetcode_py import TreeNode


class Solution:
    # Time: O(n) — BFS visit plus one pass over the column span
    # Space: O(n) — queue and column buckets
    def vertical_order(self, root: TreeNode[int] | None) -> list[list[int]]:
        if root is None:
            return []

        columns: dict[int, list[int]] = {}
        queue: deque[tuple[TreeNode[int], int]] = deque([(root, 0)])
        min_col = max_col = 0
        while queue:
            node, col = queue.popleft()
            columns.setdefault(col, []).append(node.val)
            min_col = min(min_col, col)
            max_col = max(max_col, col)
            if node.left is not None:
                queue.append((node.left, col - 1))
            if node.right is not None:
                queue.append((node.right, col + 1))

        return [columns[col] for col in range(min_col, max_col + 1)]
