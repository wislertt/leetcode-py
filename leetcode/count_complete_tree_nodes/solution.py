from leetcode_py import TreeNode


class Solution:
    # Time: O(log^2 n)
    # Space: O(1)
    def count_nodes(self, root: TreeNode[int] | None) -> int:
        if root is None:
            return 0

        left_depth = 0
        node = root
        while node.left is not None:
            left_depth += 1
            node = node.left

        def exists(index: int) -> bool:
            current = root
            for shift in range(left_depth - 1, -1, -1):
                if current is None:
                    return False
                current = current.right if (index >> shift) & 1 else current.left
            return current is not None

        low, high = 1, 1 << left_depth
        while low < high:
            mid = (low + high + 1) // 2
            if exists(mid - 1):
                low = mid
            else:
                high = mid - 1
        return (1 << left_depth) - 1 + low
