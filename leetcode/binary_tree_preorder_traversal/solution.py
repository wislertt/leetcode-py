from leetcode_py import TreeNode


class Solution:
    # Time: O(n)
    # Space: O(h) where h is the height of the tree
    def preorder_traversal(self, root: TreeNode[int] | None) -> list[int]:
        if not root:
            return []

        result: list[int] = []
        stack: list[TreeNode[int]] = [root]

        while stack:
            node = stack.pop()
            result.append(node.val)

            # Push right first, then left (so left is processed first)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return result
