class Solution:
    # Time: O((V + E) * Q) where V = variables, E = equations, Q = queries
    # Space: O(V + E) for the graph
    def calc_equation(
        self, equations: list[list[str]], values: list[float], queries: list[list[str]]
    ) -> list[float]:
        # Build weighted graph: adj[a][b] = a / b
        graph: dict[str, dict[str, float]] = {}
        for (a, b), value in zip(equations, values, strict=True):
            graph.setdefault(a, {})[b] = value
            graph.setdefault(b, {})[a] = 1.0 / value

        def bfs(start: str, target: str) -> float:
            if start not in graph or target not in graph:
                return -1.0
            if start == target:
                return 1.0
            queue = [(start, 1.0)]
            seen = {start}
            for node, product in queue:
                for neighbor, weight in graph[node].items():
                    if neighbor == target:
                        return product * weight
                    if neighbor not in seen:
                        seen.add(neighbor)
                        queue.append((neighbor, product * weight))
            return -1.0

        return [bfs(c, d) for c, d in queries]
