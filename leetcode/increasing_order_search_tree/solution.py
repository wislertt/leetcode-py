from leetcode_py import TreeNode


class Solution:
    # Time: O(n) each node is pushed and popped exactly once
    # Space: O(n) for the node list plus the stack of left-spine ancestors
    def increasing_bst(self, root: TreeNode[int] | None) -> TreeNode[int] | None:
        nodes: list[TreeNode[int]] = []
        stack: list[TreeNode[int]] = []
        current = root

        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            nodes.append(current)
            current = current.right

        for i, node in enumerate(nodes):
            node.left = None
            node.right = nodes[i + 1] if i + 1 < len(nodes) else None

        return nodes[0] if nodes else None
