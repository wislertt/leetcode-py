from leetcode_py import TreeNode


class Solution:
    # Time: O(n) - single traversal of the tree
    # Space: O(h) - recursion stack, h is the tree height
    def is_cousins(self, root: TreeNode[int] | None, x: int, y: int) -> bool:
        info: dict[int, tuple[int, int | None]] = {}

        def dfs(node: TreeNode[int] | None, parent: int | None, depth: int) -> None:
            if node is None:
                return
            info[node.val] = (depth, parent)
            dfs(node.left, node.val, depth + 1)
            dfs(node.right, node.val, depth + 1)

        if root is None:
            return False
        dfs(root, None, 0)
        dx, px = info[x]
        dy, py = info[y]
        return dx == dy and px != py
