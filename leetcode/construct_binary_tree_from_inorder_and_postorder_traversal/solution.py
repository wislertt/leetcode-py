from leetcode_py import TreeNode


class Solution:
    # Time: O(n)
    # Space: O(n)
    def build_tree(self, inorder: list[int], postorder: list[int]) -> TreeNode[int] | None:
        indices: dict[int, int] = {value: i for i, value in enumerate(inorder)}

        def build(
            in_left: int, in_right: int, post_left: int, post_right: int
        ) -> TreeNode[int] | None:
            if in_left > in_right:
                return None
            root_value = postorder[post_right]
            root = TreeNode[int](root_value)
            mid = indices[root_value]
            left_size = mid - in_left
            root.left = build(in_left, mid - 1, post_left, post_left + left_size - 1)
            root.right = build(mid + 1, in_right, post_left + left_size, post_right - 1)
            return root

        return build(0, len(inorder) - 1, 0, len(postorder) - 1)
