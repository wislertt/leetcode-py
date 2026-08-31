class Solution:
    # Time: O(n + e)
    # Space: O(n + e)
    def leads_to_destination(
        self, n: int, edges: list[list[int]], source: int, destination: int
    ) -> bool:
        graph: list[list[int]] = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
        if graph[destination]:
            return False

        state = [0] * n

        def dfs(i: int) -> bool:
            if state[i]:
                return state[i] == 2
            if not graph[i]:
                return i == destination
            state[i] = 1
            for j in graph[i]:
                if not dfs(j):
                    return False
            state[i] = 2
            return True

        return dfs(source)
