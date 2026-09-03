from leetcode_py import TreeNode


class Solution:
    # Time: O(n)
    # Space: O(h)
    def longest_univalue_path(self, root: TreeNode[int] | None) -> int:
        # Iterative post-order: depth can reach 1000, so avoid recursion limits.
        best = 0
        stack: list[tuple[TreeNode[int] | None, bool]] = [(root, False)] if root else []
        arrow: dict[int, int] = {}
        while stack:
            node, processed = stack.pop()
            if node is None:
                continue
            if not processed:
                stack.append((node, True))
                stack.append((node.left, False))
                stack.append((node.right, False))
                continue
            left = 0
            left_child = node.left
            if left_child is not None and left_child.val == node.val:
                left = arrow[id(left_child)] + 1
            right = 0
            right_child = node.right
            if right_child is not None and right_child.val == node.val:
                right = arrow[id(right_child)] + 1
            arrow[id(node)] = max(left, right)
            best = max(best, left + right)
        return best
