from collections import Counter

from leetcode_py import TreeNode


class Solution:
    # Time: O(n^2) worst case for string serializations
    # Space: O(n^2)
    def find_duplicate_subtrees(self, root: TreeNode[int] | None) -> list[TreeNode[int] | None]:
        counts: Counter[str] = Counter()
        result: list[TreeNode[int] | None] = []

        def serialize(node: TreeNode[int] | None) -> str:
            if node is None:
                return "#"
            key = f"{node.val},{serialize(node.left)},{serialize(node.right)}"
            counts[key] += 1
            if counts[key] == 2:
                result.append(node)
            return key

        serialize(root)
        return result
