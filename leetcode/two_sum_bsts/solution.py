from leetcode_py import TreeNode


class Solution:
    # Time: O(m + n)
    # Space: O(m + n)
    def two_sum_bsts(
        self, root1: TreeNode[int] | None, root2: TreeNode[int] | None, target: int
    ) -> bool:
        def inorder(root: TreeNode[int] | None, out: list[int]) -> None:
            if root is None:
                return
            inorder(root.left, out)
            out.append(root.val)
            inorder(root.right, out)

        nums1: list[int] = []
        nums2: list[int] = []
        inorder(root1, nums1)
        inorder(root2, nums2)
        i, j = 0, len(nums2) - 1
        while i < len(nums1) and j >= 0:
            total = nums1[i] + nums2[j]
            if total == target:
                return True
            if total < target:
                i += 1
            else:
                j -= 1
        return False
