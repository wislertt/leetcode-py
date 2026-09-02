from leetcode_py import TreeNode


class Solution:
    # Time: O(n)
    # Space: O(h) recursion stack; no counter map, only the output list
    def find_mode(self, root: TreeNode[int] | None) -> list[int]:
        modes: list[int] = []
        max_count = 0
        count = 0
        prev: TreeNode[int] | None = None

        def inorder(node: TreeNode[int] | None) -> None:
            nonlocal max_count, count, prev
            if node is None:
                return
            inorder(node.left)
            if prev is not None and prev.val == node.val:
                count += 1
            else:
                count = 1
            if count > max_count:
                max_count = count
                modes.clear()
                modes.append(node.val)
            elif count == max_count:
                modes.append(node.val)
            prev = node
            inorder(node.right)

        inorder(root)
        return modes
