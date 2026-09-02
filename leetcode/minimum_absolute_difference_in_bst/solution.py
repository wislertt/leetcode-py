from leetcode_py import TreeNode


class Solution:
    # Time: O(n)
    # Space: O(h)
    def get_minimum_difference(self, root: TreeNode[int]) -> int:
        prev: int | None = None
        best = 10**5
        node: TreeNode[int] | None = root
        stack: list[TreeNode[int]] = []
        while stack or node is not None:
            while node is not None:
                stack.append(node)
                node = node.left
            node = stack.pop()
            if prev is not None:
                best = min(best, node.val - prev)
            prev = node.val
            node = node.right
        return best
