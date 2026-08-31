from leetcode_py import TreeNode


class Solution:
    # Time: O(h) where h is the tree height
    # Space: O(1)
    def closest_value(self, root: TreeNode[int], target: float) -> int:
        closest = root.val
        node: TreeNode[int] | None = root
        while node is not None:
            if abs(node.val - target) < abs(closest - target) or (
                abs(node.val - target) == abs(closest - target) and node.val < closest
            ):
                closest = node.val
            node = node.left if target < node.val else node.right
        return closest
