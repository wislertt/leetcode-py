from leetcode_py import TreeNode


class Solution:
    # Time: O(n) — post-order pass carrying (is_bst, size, min, max)
    # Space: O(h) — recursion depth equals tree height
    def largest_bst_subtree(self, root: TreeNode[int] | None) -> int:
        def dfs(node: TreeNode[int] | None) -> tuple[bool, int, int | None, int | None]:
            if node is None:
                return True, 0, None, None
            left_bst, left_size, left_min, left_max = dfs(node.left)
            right_bst, right_size, right_min, right_max = dfs(node.right)
            if (
                left_bst
                and right_bst
                and (left_max is None or left_max < node.val)
                and (right_min is None or right_min > node.val)
            ):
                return (
                    True,
                    1 + left_size + right_size,
                    left_min if left_min is not None else node.val,
                    right_max if right_max is not None else node.val,
                )
            return False, max(left_size, right_size), None, None

        return dfs(root)[1]
