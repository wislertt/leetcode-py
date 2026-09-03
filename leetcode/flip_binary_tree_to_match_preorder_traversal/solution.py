from leetcode_py import TreeNode


class Solution:
    # Time: O(n)
    # Space: O(h)
    def flip_match_voyage(self, root: TreeNode[int] | None, voyage: list[int]) -> list[int]:
        flipped: list[int] = []
        idx = 0

        def dfs(node: TreeNode[int] | None) -> bool:
            nonlocal idx
            if node is None:
                return True
            if idx >= len(voyage) or node.val != voyage[idx]:
                return False
            idx += 1
            left, right = node.left, node.right
            if left is not None and right is not None:
                if idx >= len(voyage):
                    return False
                if left.val != voyage[idx] and right.val == voyage[idx]:
                    flipped.append(node.val)
                    left, right = right, left
            return dfs(left) and dfs(right)

        if root is None or not dfs(root) or idx != len(voyage):
            return [-1]
        return flipped
