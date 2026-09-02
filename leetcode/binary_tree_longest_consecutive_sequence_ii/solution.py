from leetcode_py import TreeNode


class Solution:
    # Time: O(n)
    # Space: O(h)
    def longest_consecutive(self, root: TreeNode[int] | None) -> int:
        best = 0

        def dfs(node: TreeNode[int] | None) -> tuple[int, int]:
            nonlocal best
            if node is None:
                return (0, 0)
            inc = dec = 1
            for child in (node.left, node.right):
                if child is None:
                    continue
                child_inc, child_dec = dfs(child)
                if child.val == node.val + 1:
                    inc = max(inc, child_inc + 1)
                if child.val == node.val - 1:
                    dec = max(dec, child_dec + 1)
            best = max(best, inc + dec - 1)
            return (inc, dec)

        dfs(root)
        return best
