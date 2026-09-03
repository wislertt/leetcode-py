from collections import deque


class Solution:
    # Time: O(n + E)
    # Space: O(n + E)
    def possible_bipartition(self, n: int, dislikes: list[list[int]]) -> bool:
        adj: list[list[int]] = [[] for _ in range(n + 1)]
        for a, b in dislikes:
            adj[a].append(b)
            adj[b].append(a)

        color = [0] * (n + 1)
        for start in range(1, n + 1):
            if color[start] != 0:
                continue
            color[start] = 1
            queue = deque([start])
            while queue:
                person = queue.popleft()
                for other in adj[person]:
                    if color[other] == 0:
                        color[other] = -color[person]
                        queue.append(other)
                    elif color[other] == color[person]:
                        return False
        return True
