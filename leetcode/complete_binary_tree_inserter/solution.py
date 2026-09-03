from collections import deque

from leetcode_py import TreeNode


class CBTInserter:
    # Time: __init__ O(n), insert O(1), get_root O(1)
    # Space: O(n)
    def __init__(self, root: TreeNode[int] | None) -> None:
        self.root = root
        self.candidates: deque[TreeNode[int]] = deque()
        if root is None:
            return
        queue: deque[TreeNode[int]] = deque([root])
        while queue:
            node = queue.popleft()
            if node.left is None or node.right is None:
                self.candidates.append(node)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

    def insert(self, val: int) -> int:
        parent = self.candidates[0]
        node: TreeNode[int] = TreeNode(val)
        if parent.left is None:
            parent.left = node
        else:
            parent.right = node
            self.candidates.popleft()
        self.candidates.append(node)
        return parent.val

    def get_root(self) -> TreeNode[int] | None:
        return self.root
