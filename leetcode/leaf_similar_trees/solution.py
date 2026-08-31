from leetcode_py import TreeNode


class Solution:
    # Time: O(n + m)
    # Space: O(n + m)
    def leaf_similar(self, root1: TreeNode[int] | None, root2: TreeNode[int] | None) -> bool:
        def leaves(root: TreeNode[int] | None) -> list[int]:
            values: list[int] = []
            stack: list[TreeNode[int] | None] = [root]
            while stack:
                node = stack.pop()
                if not node:
                    continue
                if not node.left and not node.right:
                    values.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
            return values

        return leaves(root1) == leaves(root2)
