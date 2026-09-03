from leetcode_py import TreeNode


class Solution:
    # Time: O(n log n)
    # Space: O(n)
    def vertical_traversal(self, root: TreeNode[int] | None) -> list[list[int]]:
        nodes: list[tuple[int, int, int]] = []

        def dfs(node: TreeNode[int] | None, row: int, col: int) -> None:
            if node is None:
                return
            nodes.append((col, row, node.val))
            dfs(node.left, row + 1, col - 1)
            dfs(node.right, row + 1, col + 1)

        dfs(root, 0, 0)
        nodes.sort()

        columns: dict[int, list[int]] = {}
        for col, _row, val in nodes:
            columns.setdefault(col, []).append(val)
        return [columns[col] for col in sorted(columns)]
