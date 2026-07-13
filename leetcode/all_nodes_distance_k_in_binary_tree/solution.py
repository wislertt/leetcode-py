from collections import deque

from leetcode_py import TreeNode


class Solution:
    # Treat tree as undirected graph: build parent map via DFS, then BFS from
    # the target node expanding to left child, right child, and parent.
    # Time: O(n)
    # Space: O(n)
    def distance_k(self, root: TreeNode[int] | None, target: int, k: int) -> list[int]:
        parent: dict[int, TreeNode[int] | None] = {}
        target_node: TreeNode[int] | None = None

        def dfs(node: TreeNode[int] | None, par: TreeNode[int] | None) -> None:
            nonlocal target_node
            if node is None:
                return
            parent[node.val] = par
            if node.val == target:
                target_node = node
            dfs(node.left, node)
            dfs(node.right, node)

        dfs(root, None)

        if target_node is None:
            return []

        visited: set[int] = {target}
        queue: deque[tuple[TreeNode[int], int]] = deque([(target_node, 0)])
        result: list[int] = []

        while queue:
            node, dist = queue.popleft()
            if dist == k:
                result.append(node.val)
                continue
            for neighbor in (node.left, node.right, parent[node.val]):
                if neighbor is not None and neighbor.val not in visited:
                    visited.add(neighbor.val)
                    queue.append((neighbor, dist + 1))

        return result
