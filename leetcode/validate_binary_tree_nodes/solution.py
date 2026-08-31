class Solution:
    # Time: O(n)
    # Space: O(n)
    def validate_binary_tree_nodes(
        self, n: int, left_child: list[int], right_child: list[int]
    ) -> bool:
        # A valid binary tree: exactly one root (in-degree 0), every other
        # node has in-degree 1, and all nodes are reachable from the root.
        indegree = [0] * n
        for child in left_child + right_child:
            if child == -1:
                continue
            indegree[child] += 1
            if indegree[child] > 1:
                return False

        roots = [i for i in range(n) if indegree[i] == 0]
        if len(roots) != 1:
            return False

        seen = [False] * n
        stack = [roots[0]]
        count = 0
        while stack:
            node = stack.pop()
            if seen[node]:
                return False
            seen[node] = True
            count += 1
            for child in (left_child[node], right_child[node]):
                if child != -1:
                    stack.append(child)
        return count == n
