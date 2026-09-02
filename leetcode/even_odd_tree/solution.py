from leetcode_py import TreeNode


class Solution:
    # Time: O(n)
    # Space: O(w) where w is the max level width
    def is_even_odd_tree(self, root: TreeNode[int] | None) -> bool:
        if root is None:
            return False
        level = [root]
        depth = 0
        while level:
            prev = None
            for node in level:
                val = node.val
                if depth % 2 == 0:
                    if val % 2 == 0:
                        return False
                    if prev is not None and val <= prev:
                        return False
                else:
                    if val % 2 == 1:
                        return False
                    if prev is not None and val >= prev:
                        return False
                prev = val
            level = [child for node in level for child in (node.left, node.right) if child]
            depth += 1
        return True
