from leetcode_py import TreeNode


class Solution:
    # Time: O(n), each node is visited a constant number of times
    # Space: O(1), pointers are rewired in place
    def flatten(self, root: TreeNode[int] | None) -> None:
        current = root
        while current is not None:
            if current.left is not None:
                predecessor = current.left
                while predecessor.right is not None:
                    predecessor = predecessor.right
                predecessor.right = current.right
                current.right = current.left
                current.left = None
            current = current.right
