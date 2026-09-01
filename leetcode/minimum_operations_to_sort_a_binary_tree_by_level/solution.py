from leetcode_py import TreeNode


class Solution:
    # Time: O(n log n)
    # Space: O(n)
    def minimum_operations(self, root: TreeNode[int] | None) -> int:
        if root is None:
            return 0

        total = 0
        level = [root]
        while level:
            total += self._min_swaps([node.val for node in level])
            level = [child for node in level for child in (node.left, node.right) if child]
        return total

    def _min_swaps(self, vals: list[int]) -> int:
        order = sorted(range(len(vals)), key=lambda i: vals[i])
        seen = [False] * len(vals)
        swaps = 0
        for i in range(len(vals)):
            if seen[i] or order[i] == i:
                continue
            cycle = 0
            j = i
            while not seen[j]:
                seen[j] = True
                j = order[j]
                cycle += 1
            swaps += cycle - 1
        return swaps
