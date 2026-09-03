from leetcode_py import TreeNode


class Solution:
    # Time: O(n + m * n) where n is the number of nodes and m is the tree height
    # Space: O(m * n) for the result matrix
    def print_tree(self, root: TreeNode[int] | None) -> list[list[str]]:
        def height(node: TreeNode[int] | None) -> int:
            if node is None:
                return -1
            return 1 + max(height(node.left), height(node.right))

        h = height(root)
        rows, cols = h + 1, 2 ** (h + 1) - 1
        res: list[list[str]] = [[""] * cols for _ in range(rows)]
        if root is None:
            return res

        def place(node: TreeNode[int] | None, r: int, c: int) -> None:
            if node is None:
                return
            res[r][c] = str(node.val)
            place(node.left, r + 1, c - 2 ** (h - r - 1))
            place(node.right, r + 1, c + 2 ** (h - r - 1))

        place(root, 0, (cols - 1) // 2)
        return res
