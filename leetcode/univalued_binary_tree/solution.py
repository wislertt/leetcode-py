from leetcode_py import TreeNode


class Solution:
    # Time: O(n)
    # Space: O(h)
    def is_unival_tree(self, root: TreeNode[int] | None) -> bool:
        if root is None:
            return True
        stack = [root]
        target = root.val
        while stack:
            node = stack.pop()
            if node.val != target:
                return False
            if node.left is not None:
                stack.append(node.left)
            if node.right is not None:
                stack.append(node.right)
        return True
