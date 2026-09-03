class Solution:
    # Time: O(n + e) per path, O(2^n) total in the worst case
    # Space: O(n) recursion depth excluding the output
    def all_paths_source_target(self, graph: list[list[int]]) -> list[list[int]]:
        target = len(graph) - 1
        paths: list[list[int]] = []
        path = [0]

        def dfs(node: int) -> None:
            if node == target:
                paths.append(path[:])
                return
            for nxt in graph[node]:
                path.append(nxt)
                dfs(nxt)
                path.pop()

        dfs(0)
        return paths
