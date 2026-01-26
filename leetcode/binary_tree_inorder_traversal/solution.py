from leetcode_py import TreeNode


class Solution:
    # Time: O(n)
    # Space: O(h) where h is the height of the tree
    def inorder_traversal(self, root: TreeNode[int] | None) -> list[int]:
        result: list[int] = []
        stack: list[TreeNode[int]] = []
        current: TreeNode[int] | None = root

        while current or stack:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            result.append(current.val)
            current = current.right

        return result
