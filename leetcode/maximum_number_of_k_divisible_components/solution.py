class Solution:
    # Time: O(n)
    # Space: O(n)
    def max_k_divisible_components(
        self, n: int, edges: list[list[int]], values: list[int], k: int
    ) -> int:
        adj: list[list[int]] = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        # Iterative post-order DFS from node 0 (n up to 3 * 10^4, avoid recursion).
        parent = [-1] * n
        order = [0]
        parent[0] = 0
        for node in order:
            for nxt in adj[node]:
                if parent[nxt] == -1:
                    parent[nxt] = node
                    order.append(nxt)

        subtree = values[:]
        count = 0
        for node in reversed(order):
            if subtree[node] % k == 0:
                count += 1
            else:
                subtree[parent[node]] += subtree[node]
        return count
