from leetcode_py import TreeNode


class Solution:
    # Time: O(n) over the traversal length
    # Space: O(depth) for the node stack
    def recover_from_preorder(self, traversal: str) -> TreeNode[int] | None:
        i = 0
        n = len(traversal)
        stack: list[TreeNode[int]] = []
        while i < n:
            depth = 0
            while i < n and traversal[i] == "-":
                depth += 1
                i += 1
            value = 0
            while i < n and traversal[i].isdigit():
                value = value * 10 + int(traversal[i])
                i += 1
            node: TreeNode[int] = TreeNode(value)
            while len(stack) > depth:
                stack.pop()
            if stack:
                if stack[-1].left is None:
                    stack[-1].left = node
                else:
                    stack[-1].right = node
            stack.append(node)
        return stack[0]
