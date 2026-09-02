from collections import deque

from leetcode_py import TreeNode


class Solution:
    # Time: O(n)
    # Space: O(n)
    def find_closest_leaf(self, root: TreeNode[int] | None, k: int) -> int:
        assert root is not None
        parent: dict[int, TreeNode[int] | None] = {id(root): None}
        q: deque[TreeNode[int]] = deque([root])
        target: TreeNode[int] | None = None
        while q:
            node = q.popleft()
            if node.val == k:
                target = node
            for child in (node.left, node.right):
                if child is not None:
                    parent[id(child)] = node
                    q.append(child)
        assert target is not None
        dist: dict[int, int] = {id(target): 0}
        q = deque([target])
        while q:
            node = q.popleft()
            if node.left is None and node.right is None:
                return node.val
            for nxt in (parent[id(node)], node.left, node.right):
                if nxt is not None and id(nxt) not in dist:
                    dist[id(nxt)] = dist[id(node)] + 1
                    q.append(nxt)
        return root.val
