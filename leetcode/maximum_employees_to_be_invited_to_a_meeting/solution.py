from collections import deque


class Solution:
    # Time: O(n)
    # Space: O(n)
    def maximum_invitations(self, favorite: list[int]) -> int:
        n = len(favorite)
        depth = [1] * n
        indegree = [0] * n
        for fav in favorite:
            indegree[fav] += 1

        # Peel off chain nodes so only cycle nodes keep indegree > 0, recording
        # for each cycle node the longest chain of excluded employees hanging
        # off it (depth counts the cycle node itself).
        queue = deque(i for i in range(n) if indegree[i] == 0)
        in_cycle = [True] * n
        while queue:
            node = queue.popleft()
            in_cycle[node] = False
            nxt = favorite[node]
            depth[nxt] = max(depth[nxt], depth[node] + 1)
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                queue.append(nxt)

        visited = [False] * n
        best_cycle = 0
        pair_total = 0
        for start in range(n):
            if not in_cycle[start] or visited[start]:
                continue
            length = 0
            node = start
            while not visited[node]:
                visited[node] = True
                node = favorite[node]
                length += 1
            if length == 2:
                # Mutual pairs can all sit together if their chains face them.
                pair_total += depth[start] + depth[favorite[start]]
            else:
                best_cycle = max(best_cycle, length)
        return max(best_cycle, pair_total)
