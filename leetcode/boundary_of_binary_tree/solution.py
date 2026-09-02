from leetcode_py import TreeNode


class Solution:
    # Time: O(n)
    # Space: O(n)
    def boundary_of_binary_tree(self, root: TreeNode[int] | None) -> list[int]:
        if root is None:
            return []

        def is_leaf(node: TreeNode[int] | None) -> bool:
            return node is not None and node.left is None and node.right is None

        vals = [root.val]

        cur = root.left
        while cur is not None and not is_leaf(cur):
            vals.append(cur.val)
            cur = cur.left if cur.left is not None else cur.right

        leaves: list[int] = []
        stack = [root]
        while stack:
            node = stack.pop()
            if is_leaf(node) and node is not root:
                leaves.append(node.val)
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)
        vals.extend(leaves)

        right: list[int] = []
        cur = root.right
        while cur is not None and not is_leaf(cur):
            right.append(cur.val)
            cur = cur.right if cur.right is not None else cur.left
        vals.extend(reversed(right))
        return vals
