from leetcode_py import TreeNode


class Solution:
    # Time: O(n)
    # Space: O(n)
    def check_equal_tree(self, root: TreeNode[int] | None) -> bool:
        if root is None:
            return False
        # Iterative postorder: cutting the edge above `node` leaves a piece whose
        # sum is that node's subtree sum, so every non-root node is a candidate.
        # TreeNode is unhashable, so sums are keyed by identity instead of node.
        sums: dict[int, int] = {}
        order: list[TreeNode[int]] = []
        stack: list[tuple[TreeNode[int] | None, bool]] = [(root, False)]
        while stack:
            node, expanded = stack.pop()
            if node is None:
                continue
            if not expanded:
                stack.append((node, True))
                stack.append((node.left, False))
                stack.append((node.right, False))
                continue
            left = sums[id(node.left)] if node.left is not None else 0
            right = sums[id(node.right)] if node.right is not None else 0
            sums[id(node)] = left + right + node.val
            order.append(node)
        total = sums[id(root)]
        if total % 2 != 0:
            return False
        half = total // 2
        return any(sums[id(node)] == half for node in order[:-1])
