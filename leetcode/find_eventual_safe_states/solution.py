from collections import deque


class Solution:
    # Time: O(n + e)
    # Space: O(n + e)
    def eventual_safe_nodes(self, graph: list[list[int]]) -> list[int]:
        n = len(graph)
        # Trim nodes in reverse topological order: a node is safe once all
        # its outgoing edges point at confirmed safe nodes
        out_degree = [len(edges) for edges in graph]
        reverse: list[list[int]] = [[] for _ in range(n)]
        for u, edges in enumerate(graph):
            for v in edges:
                reverse[v].append(u)

        queue = deque(i for i in range(n) if out_degree[i] == 0)
        safe = [False] * n
        while queue:
            v = queue.popleft()
            safe[v] = True
            for u in reverse[v]:
                out_degree[u] -= 1
                if out_degree[u] == 0:
                    queue.append(u)
        return [i for i in range(n) if safe[i]]
