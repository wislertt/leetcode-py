from leetcode_py import TreeNode


class Solution:
    # Time: O(n) - each index is pushed and popped at most once
    # Space: O(n) - stack holds the right spine of the tree
    def construct_maximum_binary_tree(self, nums: list[int]) -> TreeNode[int] | None:
        stack: list[TreeNode[int]] = []
        for num in nums:
            node = TreeNode(num)
            while stack and stack[-1].val < num:
                node.left = stack.pop()
            if stack:
                stack[-1].right = node
            stack.append(node)
        return stack[0] if stack else None
