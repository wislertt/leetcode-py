from leetcode_py import TreeNode


class Solution:
    # Time: O(n)
    # Space: O(1)
    def recover_tree(self, root: TreeNode[int] | None) -> None:
        first: TreeNode[int] | None = None
        second: TreeNode[int] | None = None
        prev: TreeNode[int] | None = None

        current = root
        while current is not None:
            if current.left is None:
                if prev is not None and prev.val > current.val:
                    if first is None:
                        first = prev
                    second = current
                prev = current
                current = current.right
            else:
                predecessor = current.left
                while predecessor.right is not None and predecessor.right is not current:
                    predecessor = predecessor.right
                if predecessor.right is None:
                    predecessor.right = current
                    current = current.left
                else:
                    predecessor.right = None
                    if prev is not None and prev.val > current.val:
                        if first is None:
                            first = prev
                        second = current
                    prev = current
                    current = current.right

        if first is not None and second is not None:
            first.val, second.val = second.val, first.val
