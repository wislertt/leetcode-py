from leetcode_py import TreeNode


class Solution:
    # Time: O(n)
    # Space: O(1)
    def upside_down_binary_tree(self, root: TreeNode[int] | None) -> TreeNode[int] | None:
        curr = root
        prev: TreeNode[int] | None = None
        prev_right: TreeNode[int] | None = None
        while curr is not None:
            next_curr = curr.left
            orig_right = curr.right
            curr.left = prev_right
            curr.right = prev
            prev_right = orig_right
            prev = curr
            curr = next_curr
        return prev
