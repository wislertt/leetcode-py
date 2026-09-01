from collections import defaultdict, deque


class Solution:
    # Time: O(n)
    # Space: O(n)
    def tree_diameter(self, edges: list[list[int]]) -> int:
        if not edges:
            return 0
        graph: dict[int, list[int]] = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def bfs_farthest(src: int) -> tuple[int, int]:
            dist = {src: 0}
            queue: deque[int] = deque([src])
            far_node, far_dist = src, 0
            while queue:
                node = queue.popleft()
                for nxt in graph[node]:
                    if nxt not in dist:
                        dist[nxt] = dist[node] + 1
                        if dist[nxt] > far_dist:
                            far_dist = dist[nxt]
                            far_node = nxt
                        queue.append(nxt)
            return far_node, far_dist

        end, _ = bfs_farthest(edges[0][0])
        _, diameter = bfs_farthest(end)
        return diameter
