from leetcode_py import TreeNode


class Solution:
    # Time: O(n)
    # Space: O(n)
    def count_unival_subtrees(self, root: TreeNode[int] | None) -> int:
        count = 0

        def is_unival(node: TreeNode[int] | None) -> bool:
            nonlocal count
            if node is None:
                return True
            left_unival = is_unival(node.left)
            right_unival = is_unival(node.right)
            if not left_unival or not right_unival:
                return False
            if node.left is not None and node.left.val != node.val:
                return False
            if node.right is not None and node.right.val != node.val:
                return False
            count += 1
            return True

        is_unival(root)
        return count
