from collections import deque


class Solution:
    # Time: O(n + e)
    # Space: O(n + e)
    def shortest_alternating_paths(
        self, n: int, red_edges: list[list[int]], blue_edges: list[list[int]]
    ) -> list[int]:
        adj: list[dict[str, list[int]]] = [{"r": [], "b": []} for _ in range(n)]
        for a, b in red_edges:
            adj[a]["r"].append(b)
        for a, b in blue_edges:
            adj[a]["b"].append(b)

        ans = [-1] * n
        dist: dict[tuple[int, str], int] = {(0, "r"): 0, (0, "b"): 0}
        queue: deque[tuple[int, str]] = deque([(0, "r"), (0, "b")])
        while queue:
            node, color = queue.popleft()
            if ans[node] == -1:
                ans[node] = dist[(node, color)]
            nxt = "b" if color == "r" else "r"
            for nb in adj[node][nxt]:
                if (nb, nxt) not in dist:
                    dist[(nb, nxt)] = dist[(node, color)] + 1
                    queue.append((nb, nxt))
        return ans
