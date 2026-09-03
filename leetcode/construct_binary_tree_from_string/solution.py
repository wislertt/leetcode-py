from leetcode_py import TreeNode


class Solution:
    # Time: O(n)
    # Space: O(h) for the recursion stack, where h is the tree height
    def str2tree(self, s: str) -> TreeNode[int] | None:
        if not s:
            return None

        def parse(i: int) -> tuple[TreeNode[int], int]:
            start = i
            if s[i] == "-":
                i += 1
            while i < len(s) and s[i].isdigit():
                i += 1
            node = TreeNode(int(s[start:i]))
            if i < len(s) and s[i] == "(":
                node.left, i = parse(i + 1)
                i += 1  # closing paren of the left subtree
                if i < len(s) and s[i] == "(":
                    node.right, i = parse(i + 1)
                    i += 1  # closing paren of the right subtree
            return node, i

        root, _ = parse(0)
        return root
