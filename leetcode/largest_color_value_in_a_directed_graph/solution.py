class Solution:
    # Time: O(n + m) with a constant factor of 26 colors
    # Space: O(n)
    def largest_path_value(self, colors: str, edges: list[list[int]]) -> int:
        n = len(colors)
        adj: list[list[int]] = [[] for _ in range(n)]
        indegree = [0] * n
        for src, dst in edges:
            adj[src].append(dst)
            indegree[dst] += 1

        counts = [[0] * 26 for _ in range(n)]
        for node in range(n):
            counts[node][ord(colors[node]) - 97] = 1
        queue = [node for node in range(n) if indegree[node] == 0]
        processed = 0
        best = 0

        while queue:
            node = queue.pop()
            processed += 1
            node_counts = counts[node]
            local_best = max(node_counts)
            if local_best > best:
                best = local_best
            for nxt in adj[node]:
                nxt_counts = counts[nxt]
                nxt_color = ord(colors[nxt]) - 97
                for c in range(26):
                    cand = node_counts[c] + (1 if c == nxt_color else 0)
                    if cand > nxt_counts[c]:
                        nxt_counts[c] = cand
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    queue.append(nxt)

        return best if processed == n else -1
