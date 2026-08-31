from leetcode_py import TreeNode


class Solution:
    # Time: O(n)
    # Space: O(n)
    def construct_from_pre_post(
        self, preorder: list[int], postorder: list[int]
    ) -> TreeNode[int] | None:
        index = {value: i for i, value in enumerate(postorder)}
        self._pre_index = 0
        return self._build(preorder, index, 0, len(postorder) - 1)

    def _build(
        self, preorder: list[int], index: dict[int, int], lo: int, hi: int
    ) -> TreeNode[int] | None:
        if lo > hi:
            return None
        node = TreeNode(preorder[self._pre_index])
        self._pre_index += 1
        if lo < hi:
            left_size = index[preorder[self._pre_index]] - lo + 1
            node.left = self._build(preorder, index, lo, lo + left_size - 1)
            node.right = self._build(preorder, index, lo + left_size, hi - 1)
        return node
