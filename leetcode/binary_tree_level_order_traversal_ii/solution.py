from leetcode_py import TreeNode


class Solution:
    # Time: O(n)
    # Space: O(n)
    def level_order_bottom(self, root: TreeNode[int] | None) -> list[list[int]]:
        levels: list[list[int]] = []
        frontier = [root] if root is not None else []
        while frontier:
            levels.append([node.val for node in frontier])
            frontier = [
                child for node in frontier for child in (node.left, node.right) if child is not None
            ]
        levels.reverse()
        return levels
