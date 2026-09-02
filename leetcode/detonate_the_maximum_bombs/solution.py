class Solution:
    # Time: O(n^3) in the worst case (n BFS passes over an O(n^2) adjacency build)
    # Space: O(n^2)
    def maximum_detonation(self, bombs: list[list[int]]) -> int:
        n = len(bombs)
        adj: list[list[int]] = [[] for _ in range(n)]
        for i, (xi, yi, ri) in enumerate(bombs):
            for j, (xj, yj, _) in enumerate(bombs):
                if i != j and (xi - xj) ** 2 + (yi - yj) ** 2 <= ri * ri:
                    adj[i].append(j)

        def bfs(start: int) -> int:
            seen = [False] * n
            seen[start] = True
            stack = [start]
            count = 0
            while stack:
                node = stack.pop()
                count += 1
                for nxt in adj[node]:
                    if not seen[nxt]:
                        seen[nxt] = True
                        stack.append(nxt)
            return count

        return max(bfs(i) for i in range(n))
