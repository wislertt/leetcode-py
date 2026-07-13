from leetcode_py import TreeNode


class Solution:
    # Time: O(n) — each element becomes one node
    # Space: O(log n) recursion stack for a balanced build
    def sorted_array_to_bst(self, nums: list[int]) -> TreeNode[int] | None:
        def build(left: int, right: int) -> TreeNode[int] | None:
            if left > right:
                return None
            mid = (left + right) // 2
            node = TreeNode[int](nums[mid])
            node.left = build(left, mid - 1)
            node.right = build(mid + 1, right)
            return node

        return build(0, len(nums) - 1)
