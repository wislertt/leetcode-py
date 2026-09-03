from leetcode_py import TreeNode


class Solution:
    # Time: O(n)
    # Space: O(h) for the recursion stack
    def min_camera_cover(self, root: TreeNode[int] | None) -> int:
        cameras = 0

        # Post-order status per subtree: 0 needs a camera, 1 covered, 2 holds a camera
        def dfs(node: TreeNode[int] | None) -> int:
            nonlocal cameras
            if node is None:
                return 1
            left = dfs(node.left)
            right = dfs(node.right)
            if left == 0 or right == 0:
                cameras += 1
                return 2
            if left == 2 or right == 2:
                return 1
            return 0

        if dfs(root) == 0:
            cameras += 1
        return cameras
