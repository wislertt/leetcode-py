from collections import Counter

from leetcode_py import TreeNode


class Solution:
    # Time: O(n), each node visited once; result collection O(distinct sums)
    # Space: O(n) for the recursion stack and the counter
    def find_frequent_tree_sum(self, root: TreeNode[int] | None) -> list[int]:
        counts: Counter[int] = Counter()

        def dfs(node: TreeNode[int] | None) -> int:
            if node is None:
                return 0
            total = node.val + dfs(node.left) + dfs(node.right)
            counts[total] += 1
            return total

        dfs(root)
        top = max(counts.values())
        return [total for total, count in counts.items() if count == top]
