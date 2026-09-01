from collections import deque


class Solution:
    # Time: O(n * (n + e)) where e = len(edges)
    # Space: O(n + e)

    def magnificent_sets(self, n: int, edges: list[list[int]]) -> int:
        adj: list[list[int]] = [[] for _ in range(n + 1)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        seen: list[bool] = [False] * (n + 1)
        total = 0
        for start in range(1, n + 1):
            if seen[start]:
                continue
            component = self._collect(start, adj, seen)
            best = 0
            for source in component:
                groups = self._max_groups(source, adj)
                if groups < 0:
                    return -1
                best = max(best, groups)
            total += best
        return total

    def _collect(self, start: int, adj: list[list[int]], seen: list[bool]) -> list[int]:
        component = [start]
        seen[start] = True
        stack = [start]
        while stack:
            node = stack.pop()
            for nxt in adj[node]:
                if not seen[nxt]:
                    seen[nxt] = True
                    component.append(nxt)
                    stack.append(nxt)
        return component

    def _max_groups(self, source: int, adj: list[list[int]]) -> int:
        # BFS layer count from source; -1 when an intra-layer edge breaks bipartiteness
        depth: dict[int, int] = {source: 0}
        queue: deque[int] = deque([source])
        max_depth = 0
        while queue:
            node = queue.popleft()
            for nxt in adj[node]:
                if nxt not in depth:
                    depth[nxt] = depth[node] + 1
                    max_depth = max(max_depth, depth[nxt])
                    queue.append(nxt)
                elif depth[nxt] == depth[node]:
                    return -1
        return max_depth + 1
