from collections import deque

from leetcode_py import TreeNode


class Solution:
    # Time: O(n)
    # Space: O(w)
    def kth_largest_level_sum(self, root: TreeNode[int] | None, k: int) -> int:
        sums: list[int] = []
        queue = deque([root] if root is not None else [])
        while queue:
            level_sum = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                level_sum += node.val
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            sums.append(level_sum)
        if k > len(sums):
            return -1
        sums.sort(reverse=True)
        return sums[k - 1]
