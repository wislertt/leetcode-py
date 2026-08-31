from leetcode_py import TreeNode


class BSTIterator:
    # Time: O(1) average per operation
    # Space: O(h)
    def __init__(self, root: TreeNode[int] | None) -> None:
        self._stack: list[TreeNode[int]] = []
        self._push_left(root)

    def _push_left(self, node: TreeNode[int] | None) -> None:
        while node is not None:
            self._stack.append(node)
            node = node.left

    # Time: O(1) average
    # Space: O(1)
    def next(self) -> int:
        node = self._stack.pop()
        self._push_left(node.right)
        return node.val

    # Time: O(1)
    # Space: O(1)
    def has_next(self) -> bool:
        return len(self._stack) > 0
