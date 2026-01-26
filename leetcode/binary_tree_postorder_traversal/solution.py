from leetcode_py import TreeNode


class Solution:
    # Time: O(n)
    # Space: O(h) where h is the height of the tree
    def postorder_traversal(self, root: TreeNode[int] | None) -> list[int]:
        if not root:
            return []

        result: list[int] = []
        stack: list[TreeNode[int]] = [root]

        while stack:
            node = stack.pop()
            result.append(node.val)

            # Push left first, then right (so right is processed first)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        # Reverse to get postorder (left, right, root)
        return result[::-1]
